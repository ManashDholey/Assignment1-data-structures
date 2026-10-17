import codecs
import itertools
import re
import sys
from urllib.parse import urlparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os
from pathlib import Path
import unicodedata
import argparse
import json

_REPORT_LINES = []
POSITIVE_WORDS =[]
NEGATIVE_WORDS =[]
PRIMARY, ACCENT, GREEN, RED, GRAY = "#2F5D8A", "#E07B39", "#5B9E7A", "#C0504D", "#8C8C8C"
VOWELS = set("aeiou")
def report(msg=""):
    """Print a line and keep it for summary.txt."""
    print(msg)
    _REPORT_LINES.append(str(msg))
def read_with_encoding_fallback(filepath):
    """
    Read a text file using Python file I/O and work out its encoding.

    The file is read as bytes and decoded in this order:
      1. ASCII    (pure 7-bit text; also valid UTF-8)
      2. UTF-8    (with BOM handling)
      3. cp1252 / latin-1 as last-resort fallbacks for legacy files

    Returns
    -------
    (text, encoding_label) : tuple[str, str]
    """
    with open(filepath, "rb") as f:
        raw = f.read()

    candidates = ["ascii", "utf-8-sig" if raw.startswith(codecs.BOM_UTF8) else "utf-8",
                  "cp1252", "latin-1"]
    for enc in candidates:
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue  # latin-1 can decode any byte, so the loop always ends
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text, enc

def load_text(inputs):
    paths = []
    i = 0
    for item in inputs:
        script_dir = Path(__file__).resolve().parent
        if i < 10:
            file_path = script_dir / f"{item}/00{i}.txt"
        elif i < 100:
            file_path = script_dir / f"{item}/0{i}.txt"
        else:
            file_path = script_dir / f"{item}/{i}.txt"
        i += 1
        p = Path(file_path)
        if p.is_dir():
            paths.extend(sorted(p.rglob("*.txt")))
        elif p.is_file():
            paths.append(p)
        else:
            matches = sorted(Path().glob(item))
            if not matches:
                report(f"  [warning] not found: {item}")
                paths.extend(m for m in matches if m.is_file())
    docs = []
    for path in paths:
        try:
            text, enc = read_with_encoding_fallback(path)
        except (OSError, PermissionError) as exc:
            report(f"  [warning] could not read {path}: {exc}")
            continue
        if not text.strip():
            report(f"  [warning] empty file skipped: {path}")
            continue
        docs.append({"filename": path.name, "path": str(path), "category": path.parent.name,
                         "encoding": enc, "raw": text})
    return docs
    

def extract_emails(text):
    """Extract email addresses and keep the same schema as the other pattern extractors."""
    matches = re.findall(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", text)
    unique = sorted(set(matches))
    return {"total": len(matches), "matches": matches, "unique": unique,
            "unique_count": len(unique)}


def calculete_word_frequencies(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)


def plot_word_frequencies(word_freq, top_n=20):
    most_common_words = word_freq.most_common(top_n)
    words, frequencies = zip(*most_common_words)
    plt.bar(words, frequencies)
    plt.xlabel("Words")
    plt.ylabel("Frequencies")
    plt.title(f"Top {top_n} Word Frequencies")
    plt.show()

# ---------------------------------------------------------------------------
# Tokenisation, cleaning, sentence splitting
# ---------------------------------------------------------------------------
PHONE_RE = re.compile(
    r"(?<![\w+])(?:\+?1[\s.-]?)?(?:\(\d{3}\)\s?|\d{3}[\s.-])\d{3}[\s.-]\d{4}(?!\d)")

HASHTAG_RE = re.compile(r"(?<![\w&#])#[A-Za-z_]\w*")
_LETTER = r"[^\W\d_]"  # any Unicode letter
WORD_RE = re.compile(rf"{_LETTER}+(?:'{_LETTER}+)*")
_URL_RE = re.compile(r"(?:https?://|www\.)[^\s<>\"'\])]+", re.I)
_EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
_MENTION_RE = re.compile(r"(?<![\w.@])@([A-Za-z_]\w{0,29})\b")
MENTION_RE = _MENTION_RE
_HTML_RE = re.compile(r"<[^>]+>")

_ABBREV = re.compile(r"\b(?:Mr|Mrs|Ms|Dr|Prof|Sr|Jr|St|Mt|vs|Inc|Ltd|Corp|Gen|Col|Capt|Lt|Sgt|Rev|"
                     r"Hon|Fig|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\.")
_DOT = "\u0000"
_SENT_SPLIT = re.compile(
    r"(?:(?<=[.!?])|(?<=[.!?][\"'”’)\]]))\s+(?=[\"'“‘(\[]?[A-Z0-9])")

_GUT_START = re.compile(r"\*\*\*\s*START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK[^\n]*\*\*\*", re.I)
_GUT_END = re.compile(r"\*\*\*\s*END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK", re.I)

_MONTH = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|"
          r"Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)")
DATE_PATTERNS = {
    "DD/MM/YYYY": re.compile(r"\b(?:0?[1-9]|[12]\d|3[01])/(?:0?[1-9]|1[0-2])/\d{4}\b"),
    "MM-DD-YYYY": re.compile(r"\b(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[12]\d|3[01])-\d{4}\b"),
    "Month DD, YYYY": re.compile(
        rf"\b{_MONTH}\.?\s+(?:0?[1-9]|[12]\d|3[01])(?:st|nd|rd|th)?,?\s+\d{{4}}\b"),
}

CURRENCY_RE = re.compile(
    r"[$£€¥₹]\s?\d+(?:,\d{3})*(?:\.\d+)?(?:\s?(?:million|billion|trillion|thousand|bn|[mk])\b)?"
    r"|\b\d+(?:,\d{3})*(?:\.\d+)?\s?(?:USD|EUR|GBP|INR|dollars|euros|pounds|rupees)\b",
    re.I)
_SYMBOL_CODE = {"$": "USD", "£": "GBP", "€": "EUR", "¥": "JPY", "₹": "INR"}
_WORD_CODE = {"usd": "USD", "dollars": "USD", "eur": "EUR", "euros": "EUR",
              "gbp": "GBP", "pounds": "GBP", "inr": "INR", "rupees": "INR"}
_SCALE = {"thousand": 1e3, "k": 1e3, "million": 1e6, "m": 1e6, "billion": 1e9, "bn": 1e9,
          "trillion": 1e12}


def extract_currency(text):
    """Extract currency amounts ($100, £50, €75, $2.5 million, 50 dollars ...)."""
    matches = [m.group().strip() for m in CURRENCY_RE.finditer(text)]
    by_cur = {}
    for m in matches:
        code, value = parse_currency(m)
        entry = by_cur.setdefault(code, {"count": 0, "total_value": 0.0})
        entry["count"] += 1
        entry["total_value"] = round(entry["total_value"] + value, 2)
    return {"total": len(matches), "matches": matches, "by_currency": by_cur}

def _domain(url):
    """Return the host of a URL without a leading 'www.'."""
    u = url if re.match(r"https?://", url, re.I) else "http://" + url
    host = urlparse(u).netloc.lower().split("@")[-1].split(":")[0]
    return host[4:] if host.startswith("www.") else host

def extract_urls(text):
    """Find all URLs and categorise them by domain and by top-level domain."""
    urls = [m.group().rstrip(".,;:!?'\"") for m in _URL_RE.finditer(text)]
    by_domain = {}
    for u in urls:
        by_domain.setdefault(_domain(u), []).append(u)
    tlds = Counter(d.rsplit(".", 1)[-1] for d in by_domain for _ in by_domain[d])
    return {"total": len(urls), "unique_count": len(set(urls)), "urls": urls,
            "by_domain": {d: {"count": len(v), "urls": sorted(set(v))}
                          for d, v in sorted(by_domain.items(), key=lambda kv: -len(kv[1]))},
            "by_tld": dict(tlds.most_common())}

    
def word_frequency_stats(word_freq):
    """Convert word frequencies to a NumPy array and compute descriptive statistics."""
    freqs = np.array(list(word_freq.values()), dtype=float)
    if freqs.size == 0:
        return {}
    p25, p50, p75 = np.percentile(freqs, [25, 50, 75])
    return {"vocabulary_size": int(freqs.size), "total_tokens": int(freqs.sum()),
            "mean": float(freqs.mean()), "median": float(np.median(freqs)),
            "std": float(freqs.std()), "max": int(freqs.max()),
            "p25": float(p25), "p50": float(p50), "p75": float(p75),
            "hapax_legomena": int((freqs == 1).sum()),
            "hapax_ratio": float((freqs == 1).mean())}

def section(title):
    """Print a section banner."""
    report("\n" + "=" * 78)
    report(title)
    report("=" * 78)


def strip_gutenberg_boilerplate(text):
    """Remove the Project Gutenberg licence header/footer if present (otherwise no-op)."""
    start = _GUT_START.search(text)
    if start:
        text = text[start.end():]
    end = _GUT_END.search(text)
    if end:
        text = text[:end.start()]
    return text.strip()


def tokenize(text):
    """Lower-case a text and return its word tokens (letters and inner apostrophes)."""
    text = text.lower().replace("’", "'").replace("‘", "'")
    return WORD_RE.findall(text)


def remove_noise(text):
    """Remove URLs, e-mail addresses, @mentions and HTML tags (case/punctuation are kept)."""
    for rx in (_URL_RE, _EMAIL_RE, _MENTION_RE, _HTML_RE):
        text = rx.sub(" ", text)
    return text

def _protect_dots(par):
    """Hide dots that do not end a sentence (abbreviations, initials, decimals)."""
    par = _ABBREV.sub(lambda m: m.group(0).replace(".", _DOT), par)
    par = re.sub(r"\b(?:[A-Za-z]\.){2,}", lambda m: m.group(0).replace(".", _DOT), par)
    par = re.sub(r"\b[A-Z]\.(?=\s[A-Z])", lambda m: m.group(0).replace(".", _DOT), par)
    return re.sub(r"(?<=\d)\.(?=\d)", _DOT, par)

def split_sentences(text):
   
    sentences = []
    for par in re.split(r"\n\s*\n", text):
        par = re.sub(r"\s+", " ", par).strip()
        if not par:
            continue
        for s in _SENT_SPLIT.split(_protect_dots(par)):
            s = s.replace(_DOT, ".").strip()
            if s and re.search(r"\w", s):
                sentences.append(s)
    return sentences

def _base_char(ch):
    """Strip accents so that 'é' counts as the vowel 'e'."""
    return unicodedata.normalize("NFKD", ch)[:1].lower()


def character_analysis(text):
    char_freq = Counter(c for c in text.lower() if not c.isspace())
    letter_freq = Counter({c: n for c, n in char_freq.items() if c.isalpha()})
    punct_freq = Counter({c: n for c, n in char_freq.items()
                          if unicodedata.category(c)[0] in "PS"})
    vowels = sum(n for c, n in letter_freq.items() if _base_char(c) in VOWELS)
    consonants = sum(letter_freq.values()) - vowels
    counts = np.array(list(letter_freq.values()), dtype=float)
    pct = 100 * counts / counts.sum() if counts.size else counts
    ordered = letter_freq.most_common()
    all_ordered = char_freq.most_common()
    return {"char_freq": char_freq, "letter_freq": letter_freq, "punct_freq": punct_freq,
            "letter_pct": dict(zip(letter_freq.keys(), pct.round(3))),
            "total_non_space_chars": int(sum(char_freq.values())),
            "vowels": vowels, "consonants": consonants,
            "vowel_consonant_ratio": vowels / consonants if consonants else float("nan"),
            "most_common_chars": all_ordered[:5], "least_common_chars": all_ordered[-5:],
            "most_common_letters": ordered[:5], "least_common_letters": ordered[-5:]}

def basic_statistics(text, tokens=None, sentences=None):
    """Total characters/words/sentences plus average word and sentence length."""
    tokens = tokenize(text) if tokens is None else tokens
    sentences = split_sentences(text) if sentences is None else sentences
    word_lengths = np.array([len(w) for w in tokens], dtype=float)
    sent_lengths = np.array([len(tokenize(s)) for s in sentences], dtype=float)
    return {
        "total_characters": len(text),
        "characters_no_spaces": len(re.sub(r"\s", "", text)),
        "total_words": len(tokens),
        "unique_words": len(set(tokens)),
        "total_sentences": len(sentences),
        "avg_word_length": float(word_lengths.mean()) if word_lengths.size else 0.0,
        "avg_sentence_length": float(sent_lengths.mean()) if sent_lengths.size else 0.0,
    }

def normalize_phone(raw):
    """Normalise any matched US-style phone number to +1-XXX-XXX-XXXX (None if invalid)."""
    digits = re.sub(r"\D", "", raw)
    if len(digits) == 11 and digits[0] == "1":
        digits = digits[1:]
    if len(digits) != 10:
        return None
    return f"+1-{digits[:3]}-{digits[3:6]}-{digits[6:]}"

def extract_phones(text):
    """Extract phone numbers in several formats and normalise them."""
    raw = [m.group().strip() for m in PHONE_RE.finditer(text)]
    normalized = [n for n in (normalize_phone(r) for r in raw) if n]
    return {"total": len(raw), "raw_matches": raw, "normalized": normalized,
            "unique_normalized": sorted(set(normalized))}

def extract_hashtags_mentions(text):
    """Extract #hashtags and @mentions (case-insensitive counting)."""
    tags = [m.group().lower() for m in HASHTAG_RE.finditer(text)]
    mentions = ["@" + m.group(1).lower() for m in MENTION_RE.finditer(text)]
    return {"hashtags": {"total": len(tags), "counts": dict(Counter(tags).most_common())},
            "mentions": {"total": len(mentions), "counts": dict(Counter(mentions).most_common())}}

def extract_dates(text):
    """Extract dates in DD/MM/YYYY, MM-DD-YYYY and 'Month DD, YYYY' formats."""
    result = {fmt: [m.group() for m in rx.finditer(text)] for fmt, rx in DATE_PATTERNS.items()}
    years = [int(re.findall(r"\d{4}", d)[-1]) for ds in result.values() for d in ds]
    return {"total": sum(len(v) for v in result.values()), "by_format": result,
            "years": dict(sorted(Counter(years).items()))}


def parse_currency(match):
    """Return (currency_code, numeric_value) for a matched currency string."""
    num = re.search(r"\d+(?:,\d{3})*(?:\.\d+)?", match)
    rest = match[num.end():].strip().lower()
    code = _SYMBOL_CODE.get(match.strip()[0]) or _WORD_CODE.get(rest, "UNK")
    value = float(num.group().replace(",", "")) * _SCALE.get(rest, 1.0)
    return code, value

def extract_all_patterns(text):
    """Run every extractor on `text` and return one JSON-serialisable dictionary."""
    social = extract_hashtags_mentions(text)
    return {"emails": extract_emails(text), "phones": extract_phones(text),
            "hashtags": social["hashtags"], "mentions": social["mentions"],
            "urls": extract_urls(text), "dates": extract_dates(text),
            "currency": extract_currency(text)}

def sentence_length_analysis(sentences):
    """Sentence-length distribution (in words), extremes and IQR-based outliers."""
    lengths = np.array([len(tokenize(s)) for s in sentences])
    if lengths.size == 0:
        return {}
    q1, q3 = np.percentile(lengths, [25, 75])
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    nonzero = [(len(tokenize(s)), s) for s in sentences if tokenize(s)]
    longest = max(nonzero, key=lambda t: t[0])
    shortest = min(nonzero, key=lambda t: t[0])
    return {"lengths": lengths, "count": int(lengths.size), "mean": float(lengths.mean()),
            "median": float(np.median(lengths)), "std": float(lengths.std()),
            "min": int(lengths.min()), "max": int(lengths.max()), "q1": float(q1), "q3": float(q3),
            "outlier_low": float(low), "outlier_high": float(high),
            "n_outliers": int(((lengths < low) | (lengths > high)).sum()),
            "longest": {"words": longest[0], "text": longest[1]},
            "shortest": {"words": shortest[0], "text": shortest[1]}}



def _draw_word_length_hist(ax, word_lengths):
    lengths = np.asarray(word_lengths)
    bins = np.arange(lengths.min(), lengths.max() + 2) - 0.5
    ax.hist(lengths, bins=bins, density=True, color=PRIMARY, alpha=0.85, edgecolor="white",
            label="Observed")
    mu, sd = lengths.mean(), lengths.std()
    if sd > 0:
        x = np.linspace(lengths.min() - 1, lengths.max() + 1, 300)
        pdf = np.exp(-0.5 * ((x - mu) / sd) ** 2) / (sd * np.sqrt(2 * np.pi))
        ax.plot(x, pdf, color=ACCENT, lw=2.2, label=f"Normal fit (μ={mu:.2f}, σ={sd:.2f})")
    ax.set_xlabel("Word length (characters)")
    ax.set_ylabel("Density")
    ax.legend(frameon=False)


def plot_word_length_distribution(word_lengths):
    """Histogram of word lengths with a normal-distribution curve overlay."""
    fig, ax = plt.subplots(figsize=(9, 5))
    _draw_word_length_hist(ax, word_lengths)
    ax.set_title("Word length distribution")
    return fig

def top_words(word_freq, n=20, exclude_stopwords=False):
    """Top-n (word, count) pairs, optionally skipping stop-words."""
    items = ((w, c) for w, c in word_freq.most_common()
            )
    return list(itertools.islice(items, n))


def _draw_top_words(ax, word_freq, top_n=20, exclude_stopwords=False, color=PRIMARY):
    items = top_words(word_freq, top_n, exclude_stopwords)
    words, counts = zip(*items) if items else ((), ())
    bars = ax.barh(list(words)[::-1], list(counts)[::-1], color=color)
    ax.bar_label(bars, padding=3, fontsize=8)
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Word")
    ax.margins(x=0.12)


def preprocess_text(sentences):
    """Cleaned/processed text: one sentence per line, lower-case tokens only."""
    lines = (" ".join(tokenize(s)) for s in sentences)
    return "\n".join(line for line in lines if line)


def plot_word_frequency(word_freq, top_n=20, exclude_stopwords=False):
    """Horizontal bar chart of the most frequent words with value labels."""
    fig, ax = plt.subplots(figsize=(9, 0.38 * top_n + 2))
    _draw_top_words(ax, word_freq, top_n, exclude_stopwords)
    kind = "content words (stop-words removed)" if exclude_stopwords else "words"
    ax.set_title(f"Top {top_n} most frequent {kind}")
    ax.grid(axis="y", visible=False)
    return fig

def save_fig(fig, path):
    """Save a figure as PNG and free its memory."""
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return path


def _boxplot(ax, data, labels):
    """Horizontal box plot that works on old and new Matplotlib versions."""
    try:
        bp = ax.boxplot(data, orientation="horizontal", patch_artist=True, tick_labels=labels)
    except TypeError:
        bp = ax.boxplot(data, vert=False, patch_artist=True, labels=labels)
    for patch in bp["boxes"]:
        patch.set(facecolor=PRIMARY, alpha=0.55)
    for med in bp["medians"]:
        med.set(color=ACCENT, lw=2)
    for fl in bp["fliers"]:
        fl.set(marker="o", markerfacecolor=RED, markeredgecolor=RED, markersize=3, alpha=0.5)
    return bp



def plot_sentence_length_boxplot(sent_lengths_by_doc, doc_names, max_docs=8):
    """Box plot of sentence lengths (overall + largest documents) with outlier counts."""
    all_len = np.concatenate([s for s in sent_lengths_by_doc if s.size])
    order = sorted(range(len(sent_lengths_by_doc)), key=lambda i: -sent_lengths_by_doc[i].size)
    chosen = [i for i in order[:max_docs] if sent_lengths_by_doc[i].size]
    data = [all_len] + [sent_lengths_by_doc[i] for i in chosen]
    labels = ["ALL DOCUMENTS"] + [doc_names[i][:28] for i in chosen]
    fig, ax = plt.subplots(figsize=(10, 1.0 * len(data) + 2.5))
    _boxplot(ax, data, labels)
    for pos, arr in enumerate(data, start=1):
        q1, q3 = np.percentile(arr, [25, 75])
        hi = q3 + 1.5 * (q3 - q1)
        n_out = int((arr > hi).sum() + (arr < q1 - 1.5 * (q3 - q1)).sum())
        ax.annotate(f"{n_out} outlier(s) above {hi:.0f} words", xy=(1, pos), xycoords=("axes fraction", "data"),
                    xytext=(8, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=8, color=RED, annotation_clip=False)
    ax.invert_yaxis()
    ax.set_xlabel("Sentence length (words)")
    ax.set_title("Sentence length distribution (whiskers = 1.5×IQR, red dots = outliers)")
    return fig


def _draw_sentence_hist(ax, lengths):
    top = np.percentile(lengths, 99) if lengths.size > 20 else lengths.max()
    bins = np.arange(0, max(top, 2) + 2, max(1, int(top // 40) or 1))
    ax.hist(lengths, bins=bins, color=PRIMARY, alpha=0.85, edgecolor="white")
    ax.axvline(lengths.mean(), color=ACCENT, lw=2, label=f"Mean = {lengths.mean():.1f}")
    ax.axvline(np.median(lengths), color=GREEN, lw=2, ls="--", label=f"Median = {np.median(lengths):.0f}")
    ax.set_xlabel("Sentence length (words)")
    ax.set_ylabel("Number of sentences")
    ax.legend(frameon=False)



def plot_character_frequency(char_info, top_n=15):
    """Three panels: top characters overall (no spaces), letters only, punctuation only."""
    total = char_info["total_non_space_chars"]
    fig, axes = plt.subplots(1, 3, figsize=(17, 5))
    overall = char_info["char_freq"].most_common(top_n)
    chars, counts = zip(*overall)
    colors = [PRIMARY if c.isalpha() else (GREEN if c.isdigit() else ACCENT) for c in chars]
    bars = axes[0].bar(list(chars), list(counts), color=colors)
    axes[0].bar_label(bars, labels=[f"{c / total:.1%}" for c in counts], fontsize=7, padding=2)
    axes[0].set_title(f"Top {top_n} characters (excluding spaces)")
    axes[0].set_xlabel("Character")
    axes[0].set_ylabel("Count")
    axes[0].grid(axis="x", visible=False)
    axes[0].margins(y=0.12)
    from matplotlib.patches import Patch
    axes[0].legend(handles=[Patch(color=PRIMARY, label="letter"), Patch(color=GREEN, label="digit"),
                            Patch(color=ACCENT, label="punctuation/symbol")], frameon=False)
    _draw_char_bars(axes[1], char_info["letter_freq"], total, top_n, PRIMARY, f"Top {top_n} letters")
    _draw_char_bars(axes[2], char_info["punct_freq"], total, top_n, ACCENT, "Punctuation & symbols")
    return fig


def _draw_char_bars(ax, freq, total, top_n, color, title):
    items = freq.most_common(top_n)
    if not items:
        ax.set_title(title + " (none)")
        return
    chars, counts = zip(*items)
    bars = ax.bar(list(chars), list(counts), color=color)
    ax.bar_label(bars, labels=[f"{c / total:.1%}" for c in counts], fontsize=7, padding=2)
    ax.set_title(title)
    ax.set_xlabel("Character")
    ax.set_ylabel("Count")
    ax.grid(axis="x", visible=False)
    ax.margins(y=0.12)

def plot_dashboard(word_freq, word_lengths, char_info, sent_lengths, subtitle=""):
    """2×2 dashboard: top words, word lengths, letter frequency, sentence lengths."""
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    _draw_top_words(axes[0, 0], word_freq, 10)
    axes[0, 0].set_title("Top 10 words")
    axes[0, 0].grid(axis="y", visible=False)
    _draw_word_length_hist(axes[0, 1], word_lengths)
    axes[0, 1].set_title("Word length distribution")
    _draw_char_bars(axes[1, 0], char_info["letter_freq"], char_info["total_non_space_chars"],
                    10, PRIMARY, "Top 10 letters")
    _draw_sentence_hist(axes[1, 1], sent_lengths)
    axes[1, 1].set_title("Sentence length distribution")
    fig.suptitle("Text Statistics Dashboard" + (f"\n{subtitle}" if subtitle else ""),
                 fontsize=15, fontweight="bold")
    return fig


def plot_time_series(date_years, sent_lengths_by_doc, doc_names):
    
    fig, ax = plt.subplots(figsize=(10, 5))
    if len(date_years) >= 2:
        years = np.arange(min(date_years), max(date_years) + 1)
        counts = [date_years.get(int(y), 0) for y in years]
        ax.plot(years, counts, marker="o", color=PRIMARY, lw=2, label="Date mentions")
        ax.fill_between(years, counts, alpha=0.15, color=PRIMARY)
        ax.set_xlabel("Year mentioned in text")
        ax.set_ylabel("Number of date mentions")
        ax.set_title("Time series: dates mentioned per year")
        ax.set_xticks(years)
        ax.legend(frameon=False)
        return fig, "dates"
    idx = int(np.argmax([s.size for s in sent_lengths_by_doc]))
    lens = sent_lengths_by_doc[idx]
    chunks = np.array_split(lens, max(1, min(20, lens.size)))
    means = [c.mean() for c in chunks]
    x = np.linspace(0, 100, len(means))
    ax.plot(x, means, marker="o", color=PRIMARY, lw=2, label="Mean sentence length")
    ax.axhline(lens.mean(), color=ACCENT, ls="--", label=f"Document mean = {lens.mean():.1f}")
    ax.set_xlabel("Position in document (%)")
    ax.set_ylabel("Average sentence length (words)")
    ax.set_title(f"Narrative timeline (no dates found): {doc_names[idx][:40]}")
    ax.legend(frameon=False)
    return fig, "narrative"

def vocabulary_growth(tokens):
    """Vocabulary size after each token (Heaps' law curve), computed with NumPy."""
    first_pos = {}
    for i, t in enumerate(tokens):
        first_pos.setdefault(t, i)
    positions = np.sort(np.fromiter(first_pos.values(), dtype=np.int64))
    return np.searchsorted(positions, np.arange(len(tokens)), side="right")


def plot_vocabulary_growth(tokens_by_doc, doc_names, max_docs=4):
    """CUSTOM VISUALISATION: vocabulary growth (Heaps' law) with fitted power law."""
    all_tokens = [t for toks in tokens_by_doc for t in toks]
    fig, ax = plt.subplots(figsize=(10, 6))
    series = [("Whole corpus", all_tokens, PRIMARY)]
    order = sorted(range(len(tokens_by_doc)), key=lambda i: -len(tokens_by_doc[i]))
    palette = [ACCENT, GREEN, RED, GRAY]
    for rank, i in enumerate(order[:max_docs]):
        if len(tokens_by_doc) > 1 and len(tokens_by_doc[i]) > 20:
            series.append((doc_names[i][:24], tokens_by_doc[i], palette[rank % len(palette)]))
    beta = None
    for name, toks, color in series:
        if len(toks) < 10:
            continue
        growth = vocabulary_growth(toks)
        idx = np.unique(np.geomspace(1, len(toks), 250).astype(int)) - 1
        ax.plot(idx + 1, growth[idx], color=color, lw=2 if name == "Whole corpus" else 1.2, label=name)
        if name == "Whole corpus":
            beta, logk = np.polyfit(np.log10(idx + 1), np.log10(growth[idx]), 1)
            ax.plot(idx + 1, 10 ** logk * (idx + 1) ** beta, "k--", lw=1,
                    label=f"Heaps fit: V = {10 ** logk:.1f}·n^{beta:.2f}")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Tokens read (n)")
    ax.set_ylabel("Distinct words seen (V)")
    ax.set_title("Vocabulary growth: how fast does new vocabulary appear? (Heaps' law)")
    ax.legend(frameon=False)
    return fig, beta


def zipf_analysis(word_freq, max_rank=2000):
    """Fit log10(freq) = slope·log10(rank) + intercept; ideal Zipf has slope ≈ -1."""
    freqs = np.array(sorted(word_freq.values(), reverse=True), dtype=float)
    if freqs.size < 3:
        return None
    ranks = np.arange(1, freqs.size + 1, dtype=float)
    k = min(freqs.size, max_rank)
    x, y = np.log10(ranks[:k]), np.log10(freqs[:k])
    slope, intercept = np.polyfit(x, y, 1)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r2 = 1 - np.sum((y - (slope * x + intercept)) ** 2) / ss_tot if ss_tot else float("nan")
    return {"ranks": ranks, "freqs": freqs, "slope": float(slope), "intercept": float(intercept),
            "r2": float(r2), "fit_up_to_rank": int(k)}


def plot_zipf(zipf):
    """BONUS: Zipf's law log-log plot with fitted line and the ideal 1/r reference."""
    fig, ax = plt.subplots(figsize=(9, 6))
    r, f = zipf["ranks"], zipf["freqs"]
    ax.loglog(r, f, ".", color=PRIMARY, ms=4, label="Observed words")
    k = zipf["fit_up_to_rank"]
    ax.loglog(r[:k], 10 ** zipf["intercept"] * r[:k] ** zipf["slope"], color=ACCENT, lw=2,
              label=f"Fit: slope = {zipf['slope']:.2f}, R² = {zipf['r2']:.3f}")
    ax.loglog(r, f[0] / r, "k--", lw=1, label="Ideal Zipf (frequency ∝ 1/rank)")
    ax.set_xlabel("Rank (log scale)")
    ax.set_ylabel("Frequency (log scale)")
    ax.set_title("Zipf's law")
    ax.legend(frameon=False)
    return fig


def extract_ngrams(tokens_by_doc, n, top_k=15, content_only=True):
    
    counter = Counter()
    for toks in tokens_by_doc:
        counter.update(zip(*[toks[i:] for i in range(n)]))
    if content_only:
        counter = Counter({g: c for g, c in counter.items()
                           })
    return [(" ".join(g), c) for g, c in counter.most_common(top_k)]



def plot_ngrams(bigrams, trigrams):
    """BONUS: top bigrams and trigrams."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    for ax, data, title, color in ((axes[0], bigrams, "Top bigrams", PRIMARY),
                                   (axes[1], trigrams, "Top trigrams", ACCENT)):
        if data:
            labels, counts = zip(*data)
            bars = ax.barh(list(labels)[::-1], list(counts)[::-1], color=color)
            ax.bar_label(bars, padding=3, fontsize=8)
        ax.set_title(title + " (stop-word edges removed)")
        ax.set_xlabel("Frequency")
        ax.grid(axis="y", visible=False)
        ax.margins(x=0.12)
    return fig

def sentiment_counts(tokens):
    """Count positive/negative keywords in a token list and compute a net score in [-1, 1]."""
    freq = Counter(tokens)
    pos = {w: freq[w] for w in POSITIVE_WORDS if freq[w]}
    neg = {w: freq[w] for w in NEGATIVE_WORDS if freq[w]}
    p, n = sum(pos.values()), sum(neg.values())
    return {"positive": pos, "negative": neg, "positive_total": p, "negative_total": n,
            "score": (p - n) / (p + n) if (p + n) else 0.0}


def plot_sentiment(sent):
    """BONUS: most common positive and negative keywords."""
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    for ax, key, color, title in ((axes[0], "positive", GREEN, "Positive keywords"),
                                  (axes[1], "negative", RED, "Negative keywords")):
        items = sorted(sent[key].items(), key=lambda kv: -kv[1])[:10]
        if items:
            words, counts = zip(*items)
            bars = ax.barh(list(words)[::-1], list(counts)[::-1], color=color)
            ax.bar_label(bars, padding=3, fontsize=8)
        ax.set_title(title)
        ax.set_xlabel("Occurrences")
        ax.grid(axis="y", visible=False)
    fig.suptitle(f"Sentiment keyword detection (net score = {sent['score']:+.2f})", fontweight="bold")
    return fig


def plot_correlation_heatmap(meta_df):
    """Correlation between document-level metrics (only meaningful with ≥3 documents)."""
    cols = [c for c in ["word_count", "char_count", "sentence_count", "avg_word_length",
                        "avg_sentence_length", "unique_words", "type_token_ratio",
                        "guiraud_index", "sentiment_score"] if c in meta_df]
    corr = meta_df[cols].corr()
    fig, ax = plt.subplots(figsize=(9, 7.5))
    im = ax.imshow(corr.values, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(cols)), cols, rotation=45, ha="right")
    ax.set_yticks(range(len(cols)), cols)
    for i in range(len(cols)):
        for j in range(len(cols)):
            v = corr.values[i, j]
            ax.text(j, i, "" if np.isnan(v) else f"{v:.2f}", ha="center", va="center", fontsize=8)
    ax.grid(False)
    fig.colorbar(im, ax=ax, shrink=0.8, label="Pearson r")
    ax.set_title("Correlation between document metrics")
    return fig, corr


def build_metadata_dataframe(docs):
   
    rows = []
    for i, d in enumerate(docs, start=1):
        words = len(d["tokens"])
        unique = len(set(d["tokens"]))
        sent_len = d["sent_lengths"]
        rows.append({
            "doc_id": i,
            "filename": d["filename"],
            "category": d["category"],
            "encoding": d["encoding"],
            "word_count": words,
            "char_count": len(d["raw"]),
            "sentence_count": len(d["sentences"]),
            "avg_word_length": round(float(np.mean([len(w) for w in d["tokens"]])), 3) if words else 0.0,
            "avg_sentence_length": round(float(sent_len.mean()), 3) if sent_len.size else 0.0,
            "unique_words": unique,
            "type_token_ratio": round(unique / words, 4) if words else 0.0,
            "guiraud_index": round(unique / np.sqrt(words), 3) if words else 0.0,
        })
    return pd.DataFrame(rows)


def count_vowels(word):
    """Number of vowels in a word (accent-insensitive)."""
    return sum(_base_char(c) in VOWELS for c in word)

def build_word_dataframe(word_freq):
    """DataFrame indexed by word with columns frequency, length, first_char, vowel_count."""
    words = list(word_freq)
    df = pd.DataFrame({
        "frequency": [word_freq[w] for w in words],
        "length": [len(w) for w in words],
        "first_char": [w[0] for w in words],
        "vowel_count": [count_vowels(w) for w in words],
    }, index=pd.Index(words, name="word"))
    df = df.sort_values("frequency", ascending=False, kind="stable")
    df["length_bucket"] = pd.cut(df["length"], bins=[0, 3, 6, 9, np.inf],
                                 labels=["1-3", "4-6", "7-9", "10+"])
    df["freq_band"] = pd.cut(df["frequency"], bins=[0, 1, 5, 20, 100, np.inf],
                             labels=["1 (hapax)", "2-5", "6-20", "21-100", ">100"])
    return df


def groupby_analysis(df):
    """Group by word length and by first character."""
    by_len = df.groupby("length").agg(
        unique_words=("frequency", "size"), total_occurrences=("frequency", "sum"),
        mean_frequency=("frequency", "mean"), median_frequency=("frequency", "median"),
        max_frequency=("frequency", "max"), avg_vowels=("vowel_count", "mean")).round(2)
    by_len["most_common_word"] = df.groupby("length")["frequency"].idxmax()
    by_char = df.groupby("first_char").agg(
        unique_words=("frequency", "size"), total_occurrences=("frequency", "sum"),
        mean_frequency=("frequency", "mean"), avg_length=("length", "mean")).round(2)
    by_char["most_common_word"] = df.groupby("first_char")["frequency"].idxmax()
    return by_len, by_char.sort_values("total_occurrences", ascending=False)


def pivot_and_crosstab(df, top_chars=12):
    """Pivot (first letter × length bucket) and cross-tabulation (length bucket × freq band)."""
    best = df.groupby("first_char")["frequency"].sum().nlargest(top_chars).index
    pivot = pd.pivot_table(df[df["first_char"].isin(best)], index="first_char",
                           columns="length_bucket", values="frequency", aggfunc="sum",
                           fill_value=0, observed=False)
    cross = pd.crosstab(df["length_bucket"], df["freq_band"])
    return pivot, cross

def build_interactive_dashboard(word_freq):
    """
    BONUS: interactive Matplotlib-widgets dashboard. A slider chooses how many words are
    shown and radio buttons toggle stop-word filtering. Keep the returned widget objects
    referenced, otherwise they are garbage-collected and stop responding.
    """
    from matplotlib.widgets import RadioButtons, Slider
    fig, ax = plt.subplots(figsize=(11, 7))
    fig.subplots_adjust(left=0.30, bottom=0.18, right=0.95, top=0.92)
    state = {"n": 20, "stop": False}

    def redraw(*_):
        ax.clear()
        _draw_top_words(ax, word_freq, state["n"], state["stop"])
        ax.set_title(f"Top {state['n']} words" + (" (stop-words removed)" if state["stop"] else ""))
        ax.grid(axis="y", visible=False)
        fig.canvas.draw_idle()

    slider = Slider(fig.add_axes([0.30, 0.06, 0.55, 0.03]), "Top N", 5, 50, valinit=20, valstep=1)
    radio = RadioButtons(fig.add_axes([0.02, 0.45, 0.2, 0.12]), ("All words", "Exclude stop-words"))
    slider.on_changed(lambda v: (state.update(n=int(v)), redraw()))
    radio.on_clicked(lambda label: (state.update(stop=label.startswith("Exclude")), redraw()))
    redraw()
    return fig, slider, radio


def parse_args(argv=None):
    ap = argparse.ArgumentParser(description="Text Statistics Analyzer (Python fundamentals for NLP)")
    ap.add_argument("inputs", nargs="*", help=".txt files, folders (searched recursively) or globs; "
                                              "omit to use the built-in demo corpus")
    ap.add_argument("--outdir", default="output", help="output directory (default: output)")
    ap.add_argument("--top-n", type=int, default=20, help="words shown in the frequency chart")
    ap.add_argument("--interactive", action="store_true", help="open the matplotlib-widgets dashboard")
    return ap.parse_args(argv)
if __name__ == "__main__":
    args = parse_args(sys.argv)
    outdir = Path(args.outdir)
    plots = outdir / "plots"
    plots.mkdir(parents=True, exist_ok=True)
    inputs = []
    inputs.append("data_set/bbc-fulltext/bbc/tech")
    inputs.append("data_set/bbc-fulltext/bbc/business")
    inputs.append("data_set/bbc-fulltext/bbc/entertainment")
    inputs.append("data_set/bbc-fulltext/bbc/politics")
    inputs.append("data_set/bbc-fulltext/bbc/sport")
    docs = load_text(inputs)
    if not docs:
        sys.exit("No readable .txt documents found. Check the paths you passed.")
    
    for d in docs:
        d["raw"] = strip_gutenberg_boilerplate(d["raw"])
        d["text"] = remove_noise(d["raw"])          # analysis text (no URLs / e-mails / @mentions)
        d["tokens"] = tokenize(d["text"])
        d["sentences"] = split_sentences(d["text"])
        d["sent_lengths"] = np.array([len(tokenize(s)) for s in d["sentences"]])
        report(f"Loaded {len(docs)} document(s). Encodings detected: "
               f"{dict(Counter(d['encoding'] for d in docs))}")
    
    all_text = "\n\n".join(d["text"] for d in docs)
    all_tokens = [t for d in docs for t in d["tokens"]]
    all_sentences = [s for d in docs for s in d["sentences"]]
    overall = basic_statistics(all_text, all_tokens, all_sentences)
    report("\nOverall corpus statistics:")
    for k, v in overall.items():
        report(f"  {k:<22}: {v:,.2f}" if isinstance(v, float) else f"  {k:<22}: {v:,}")
    meta = build_metadata_dataframe(docs)
    # ------------------------------------------------------------------ PART 2
    section("PART 2 - REGULAR EXPRESSION PATTERN EXTRACTION")
    joined_raw = "\n\n=====\n\n".join(d["raw"] for d in docs)
    patterns = extract_all_patterns(joined_raw)
    patterns["per_document_counts"] = {
        d["filename"] + f"#{i}": {k: v["total"] for k, v in extract_all_patterns(d["raw"]).items()}
        for i, d in enumerate(docs, start=1)} if len(docs) <= 500 else "omitted (more than 500 documents)"
    with open(outdir / "extracted_patterns.json", "w", encoding="utf-8") as f:
        json.dump(patterns, f, indent=2, ensure_ascii=False)
    e, p, u = patterns["emails"], patterns["phones"], patterns["urls"]
    report(f"Emails     : {e['total']} found, {e['unique_count']} unique -> {e['unique'][:5]}")
    report(f"Phones     : {p['total']} found -> {p['unique_normalized'][:5]}")
    report(f"Hashtags   : {patterns['hashtags']['total']} | top: "
           f"{list(patterns['hashtags']['counts'].items())[:5]}")
    report(f"Mentions   : {patterns['mentions']['total']} | top: "
           f"{list(patterns['mentions']['counts'].items())[:5]}")
    report(f"URLs       : {u['total']} found; domains: "
           f"{ {d: v['count'] for d, v in list(u['by_domain'].items())[:5]} }")
    report(f"Dates      : {patterns['dates']['total']} -> "
           f"{ {k: len(v) for k, v in patterns['dates']['by_format'].items()} }")
    report(f"Currency   : {patterns['currency']['total']} -> {patterns['currency']['by_currency']}")

    # ------------------------------------------------------------------ PART 3
    section("PART 3 - TEXT STATISTICS WITH NUMPY")
    word_freq = Counter(all_tokens)
    wstats = word_frequency_stats(word_freq)
    report("Word frequency statistics (NumPy array of frequencies):")
    for k, v in wstats.items():
        report(f"  {k:<16}: {v:,.3f}" if isinstance(v, float) else f"  {k:<16}: {v:,}")
    report(f"Top 10 words              : {top_words(word_freq, 10)}")
    report(f"Top 10 content words      : {top_words(word_freq, 10, exclude_stopwords=True)}")

    char_info = character_analysis(all_text)
    report("\nCharacter-level analysis:")
    report(f"  most common characters  : {char_info['most_common_chars']}")
    report(f"  least common characters : {char_info['least_common_chars']}")
    report(f"  most common letters     : {char_info['most_common_letters']}")
    report(f"  least common letters    : {char_info['least_common_letters']}")
    report(f"  vowels / consonants     : {char_info['vowels']:,} / {char_info['consonants']:,} "
           f"= ratio {char_info['vowel_consonant_ratio']:.3f}")

    sent = sentence_length_analysis(all_sentences)
    report("\nSentence-length analysis (words per sentence):")
    report(f"  sentences {sent['count']:,} | mean {sent['mean']:.2f} | median {sent['median']:.1f} | "
           f"std {sent['std']:.2f} | min {sent['min']} | max {sent['max']}")
    report(f"  Q1 {sent['q1']:.1f} | Q3 {sent['q3']:.1f} | outliers (>{sent['outlier_high']:.1f} words): "
           f"{sent['n_outliers']}")
    report(f"  longest ({sent['longest']['words']} words): {sent['longest']['text'][:150]}...")
    report(f"  shortest ({sent['shortest']['words']} words): {sent['shortest']['text']}")

    cleaned = "\n\n".join(f"# {d['filename']}\n{preprocess_text(d['sentences'])}" for d in docs)
    with open(outdir / "cleaned_text.txt", "w", encoding="utf-8") as f:
        f.write(cleaned + "\n")

    # ------------------------------------------------------------------ PART 4
    section("PART 4 - DATA VISUALISATION WITH MATPLOTLIB")
    names = [d["filename"] for d in docs]
    word_lengths = np.array([len(w) for w in all_tokens])
    subtitle = (f"{len(docs)} document(s) | {overall['total_words']:,} words | "
                f"{overall['total_sentences']:,} sentences | avg word length "
                f"{overall['avg_word_length']:.2f} | avg sentence length {overall['avg_sentence_length']:.1f} words")
    saved = []
    saved.append(save_fig(plot_word_frequency(word_freq, args.top_n), plots / "01_top_words.png"))
    saved.append(save_fig(plot_word_frequency(word_freq, args.top_n, exclude_stopwords=True),
                          plots / "01b_top_content_words.png"))
    saved.append(save_fig(plot_word_length_distribution(word_lengths), plots / "02_word_length_histogram.png"))
    saved.append(save_fig(plot_character_frequency(char_info), plots / "03_character_frequency.png"))
    saved.append(save_fig(plot_sentence_length_boxplot([d["sent_lengths"] for d in docs], names),
                          plots / "04_sentence_length_boxplot.png"))
    saved.append(save_fig(plot_dashboard(word_freq, word_lengths, char_info, sent["lengths"], subtitle),
                          plots / "05_dashboard_2x2.png"))
    fig, mode = plot_time_series(patterns["dates"]["years"], [d["sent_lengths"] for d in docs], names)
    saved.append(save_fig(fig, plots / "06_time_series.png"))
    report(f"Time series mode: {mode} ({'dates found in text' if mode == 'dates' else 'no dates, narrative timeline'})")
    fig, beta = plot_vocabulary_growth([d["tokens"] for d in docs], names)
    saved.append(save_fig(fig, plots / "07_custom_vocabulary_growth.png"))
    report(f"Heaps' law exponent (vocabulary growth): {beta:.3f}" if beta is not None else
           "Heaps' law: not enough tokens to fit")

    # ------------------------------------------------------------------ BONUS
    section("BONUS - ZIPF'S LAW, N-GRAMS, SENTIMENT KEYWORDS")
    zipf = zipf_analysis(word_freq)
    if zipf:
        saved.append(save_fig(plot_zipf(zipf), plots / "08_zipf_law.png"))
        report(f"Zipf fit on top {zipf['fit_up_to_rank']} ranks: slope = {zipf['slope']:.3f} "
               f"(ideal -1), R² = {zipf['r2']:.3f}")
    tokens_by_doc = [d["tokens"] for d in docs]
    bigrams = extract_ngrams(tokens_by_doc, 2)
    trigrams = extract_ngrams(tokens_by_doc, 3)
    saved.append(save_fig(plot_ngrams(bigrams, trigrams), plots / "09_ngrams.png"))
    report(f"Top bigrams : {bigrams[:8]}")
    report(f"Top trigrams: {trigrams[:8]}")
    corpus_sent = sentiment_counts(all_tokens)
    saved.append(save_fig(plot_sentiment(corpus_sent), plots / "10_sentiment_keywords.png"))
    report(f"Sentiment keywords: {corpus_sent['positive_total']} positive vs "
           f"{corpus_sent['negative_total']} negative (net {corpus_sent['score']:+.2f})")

    if len(docs) >= 3:
        fig, corr = plot_correlation_heatmap(meta)
        saved.append(save_fig(fig, plots / "11_metric_correlations.png"))
        corr.round(3).to_csv(outdir / "metric_correlations.csv", encoding="utf-8")
    report(f"\nSaved {len(saved)} plots in {plots}/")

    # ------------------------------------------------------------------ PART 5
    section("PART 5 - PANDAS DATA ANALYSIS")
    wdf = build_word_dataframe(word_freq)
    wdf.to_csv(outdir / "word_dataframe.csv", encoding="utf-8")
    report("Word DataFrame (index = word):")
    report(wdf.head(8).to_string())
    by_len, by_char = groupby_analysis(wdf)
    by_len.to_csv(outdir / "pandas_groupby_length.csv", encoding="utf-8")
    by_char.to_csv(outdir / "pandas_groupby_first_char.csv", encoding="utf-8")
    report("\nGroup by word length:")
    report(by_len.head(12).to_string())
    report("\nGroup by first character (top 8 by occurrences):")
    report(by_char.head(8).to_string())
    top50 = wdf.nlargest(50, "frequency")
    long_words = wdf[wdf["length"] > 10].sort_values("frequency", ascending=False)
    top50.to_csv(outdir / "pandas_top50_words.csv", encoding="utf-8")
    long_words.to_csv(outdir / "pandas_words_longer_than_10.csv", encoding="utf-8")
    report(f"\nTop 50 words kept; words longer than 10 characters: {len(long_words)} "
           f"(most frequent: {list(long_words.head(5).index)})")
    pivot, cross = pivot_and_crosstab(wdf)
    pivot.to_csv(outdir / "pandas_pivot_firstchar_by_length.csv", encoding="utf-8")
    cross.to_csv(outdir / "pandas_crosstab_length_by_freqband.csv", encoding="utf-8")
    report("\nPivot table (sum of frequency: first letter x length bucket):")
    report(pivot.to_string())
    report("\nCross-tabulation (number of distinct words: length bucket x frequency band):")
    report(cross.to_string())

    # ------------------------------------------------------------------ wrap up
    with open(outdir / "summary.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(_REPORT_LINES) + "\n")
    report(f"\nDone. All files are in: {outdir.resolve()}")

    if args.interactive:
        fig, *widgets = build_interactive_dashboard(word_freq)
        plt.show()

    #print(file_data)
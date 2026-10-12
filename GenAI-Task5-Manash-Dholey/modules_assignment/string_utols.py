async def concatenate(a, b):
    return a + b

async def to_uppercase(s):
    return s.upper()

async def to_lowercase(s):
    return s.lower()

async def reverse_string(s):
    return s[::-1]

async def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

async def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

async def count_consonants(s):
    return sum(1 for char in s.lower() if char.isalpha() and char not in 'aeiou')

async def count_words(s):
    return len(s.split())

async def count_characters(s):
    return len(s)

async def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
async def remove_whitespace(s):
    return ''.join(s.split())
async def remove_punctuation(s):
    import string
    return ''.join(char for char in s if char not in string.punctuation)

async def remove_digits(s):
    return ''.join(char for char in s if not char.isdigit())
async def remove_special_characters(s):
    import string
    return ''.join(char for char in s if char.isalnum() or char.isspace())


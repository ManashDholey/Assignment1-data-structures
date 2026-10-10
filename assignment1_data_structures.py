
print("===== Task 1: Lists & Tuples =====")

products = ["Laptop", "Phone", "Headphones", "Keyboard", "Mouse", "Desk Lamp"]

sample_product = ("Laptop", 55000, "Electronics")

print("2nd product:", products[1])
print("Last product:", products[-1])

products.append("Monitor")
products.append("Backpack")
print("Updated products:", products)

temp = list(sample_product)
temp[1] = 52000
sample_product = tuple(temp)
print("Updated sample_product:", sample_product)


print("\n===== Task 2: Sets =====")

categories = ["Electronics", "Electronics", "Accessories", "Accessories",
              "Accessories", "Home", "Electronics", "Accessories"]

categories_set = set(categories)
print("categories_set:", categories_set)

categories_set.add("Furniture")
print("After adding 'Furniture':", categories_set)
categories_set.add("Home")  # already exists
print("After adding 'Home' again (no change):", categories_set)

print("Is 'Electronics' in set?", "Electronics" in categories_set)
print("Is 'Toys' in set?", "Toys" in categories_set)

print("Unique categories:", len(categories_set))

print("\n===== Task 3: Dictionaries =====")

price_dict = {
    "Laptop": 52000,
    "Phone": 25000,
    "Headphones": 2500,
    "Keyboard": 1200,
    "Mouse": 600,
    "Desk Lamp": 900,
    "Monitor": 12000,
    "Backpack": 1500,
}

price_dict["Webcam"] = 3000
print("After adding Webcam:", price_dict)

price_dict["Mouse"] = 700
print("After updating Mouse price:", price_dict["Mouse"])

def remove_product(name):
    if name in price_dict:
        del price_dict[name]
        print("Removed:", name)
    else:
        print("Cannot remove, product not found:", name)


remove_product("Webcam")   # exists
remove_product("Tablet")   # does not exist

total = 0
for price in price_dict.values():
    total += price
average = total / len(price_dict)
print("Average price:", round(average, 2))

max_product = min_product = None
for name, price in price_dict.items():
    if max_product is None or price > price_dict[max_product]:
        max_product = name
    if min_product is None or price < price_dict[min_product]:
        min_product = name
print("Most expensive:", max_product, price_dict[max_product])
print("Cheapest:", min_product, price_dict[min_product])

print("\n===== Task 4: Combined Operations =====")

catalog = []
for i in range(len(products)):
    name = products[i]
    catalog.append((name, price_dict[name], categories[i]))
print("catalog:")
for item in catalog:
    print("  ", item)

category_to_products = {}
for name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(name)
print("category_to_products:", category_to_products)

biggest_category = None
for category in category_to_products:
    if (biggest_category is None or
            len(category_to_products[category]) > len(category_to_products[biggest_category])):
        biggest_category = category
print("Category with most products:", biggest_category)
print("Products in it:", category_to_products[biggest_category])

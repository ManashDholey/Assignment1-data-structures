

import os


sales = [1200, 450, 980, 1500, 3000]

print("===== Task 1 =====")
with open("sales_data.txt", "w") as file:
    for sale in sales:
        file.write(str(sale) + "\n")
    file.close()

with open("sales_data.txt", "a") as file:
    file.write("\n")
    for sale in sales:
        if(sale != sales[-1]):
            file.write(str(sale) + ",")
        else:
            file.write(str(sale))
    file.close()        
with open("sales_data.txt", "r") as file:
    contents = file.read()
    print("Sales Data:")
    print(contents)
    file.close()
print("===== End of Task 1 =====")

print("===== Task 2 =====")
with open("sales_data.txt", "r") as file:
    contents = file.read()
    print("Sales Data:")
    print(contents)
    file.seek(0) 
    first_line_contain = file.readline().strip() 
    print("First line contains using readline:",first_line_contain)
    file.seek(0) 
    all_line_contaon = [line.strip() for line in file.readlines()]
    print("all lines contain using readlines:",all_line_contaon)
    file.close()
print("===== End of Task 2 =====")


print("===== Task 3 =====")

with open("sales_data.txt", "a") as file:
    file.write("\n")
    for sale in [5000,2500,1700]:
        if(sale != [5000,2500,1700][-1]):
            file.write(str(sale) + ",")
        else:
            file.write(str(sale))
    file.close()
with open("sales_data.txt", "r") as file:
    contents = file.read()
    print("Updated Sales Data:")
    print(contents)
    file.close()
with open('sales_data.txt', 'r') as file:
    line_count = len(file.readlines())
    file.close()
print(f"Total lines: {line_count}")

print("===== End of Task 3 =====")

print("===== Task 4 =====")
all_line_contaon = []
with open("sales_data.txt", "r") as file:
    all_line_contaon = [line.strip() for line in file.readlines()]
    print("all lines contain using readlines:",all_line_contaon)
    file.close()
integers = [
    int(num) 
    for item in all_line_contaon 
    if item.strip()           
    for num in item.split(',')
]
print(integers)
total_sales = sum(integers)
print("Total Sales:", total_sales)
highest_sale = max(integers)
print("Highest Sale:", highest_sale)
lowest_sale = min(integers)
print("Lowest Sale:", lowest_sale)
average_sale = total_sales / len(integers) if integers else 0
print("Average Sale:", average_sale)

print("===== End of Task 4 =====")


print("===== Task 5 =====")
product_dic = {}
counter = 0
while True:
    produce_name  = input("Please enter product name:")
    product_price = input("Please enter the price for the product:")
    counter += 1
    product_dic[produce_name] = product_price
    if counter >= 3:
        break
print("Product Dictionary:", product_dic)
with open("products.txt", "w") as file:
    for product_name, product_price in product_dic.items():
        file.write(f"{product_name}| {product_price}\n")
    file.close()
with open("products.txt", "r") as file:
    contents = file.read()
    print("Product Data:")
    print(contents)
    file.close()

print("===== End of Task 5 =====")

print("===== Task 6 =====")

user_input = input("Please enter the file name to open: ")
file_path = os.path.join(os.getcwd(), user_input)
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        contents = file.read()
        print(f"Contents of {user_input}:")
        print(contents)
        file.close()
else:
    print(f"File {user_input} does not exist.")
print("===== End of Task 6 =====")
print("===== Task 7 =====")
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}
for product, price in prices.items():
    user_input = input("Please enter the discounted percentage: ")
    try:
        discount_percentage = int(user_input)
        discounted_price = price * ( discount_percentage / 100)
        final_discounted_price = price - discounted_price
        print(f"Discounted price for {product}: {final_discounted_price}")
        with open("discount_report.txt", "a") as file:
            file.write(f"{product}| {price}| {final_discounted_price}\n")
            file.close()
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
with open("discount_report.txt", "r") as file:
    contents = file.read()
    print(contents)
    file.close()
all_line_contaon = []
with open("discount_report.txt", "r") as file:
    all_line_contaon = [line.strip() for line in file.readlines()]
    print("all lines contain using readlines:",all_line_contaon)
    file.close()
print("Total Items:", len(all_line_contaon))
print("Average discounted price:", sum([float(line.split("|")[2].strip()) for line in all_line_contaon]) / len(all_line_contaon) if all_line_contaon else 0)

print("===== End of Task 7 =====")
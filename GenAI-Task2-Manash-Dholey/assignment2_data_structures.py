#from tabulate import tabulate
print("===== Task 1 =====")
order_amount = input("Enter the order amount: ")
order_amount = int(order_amount)
if isinstance(order_amount, (int,)):
    order_amount = int(order_amount)
else:
    print("Invalid input. Please enter a numeric value.")
discount = 0
total_amount = order_amount
if order_amount > 2000:
    print("You are eligible for a discount.")
    discount = order_amount * 0.15
elif order_amount >= 1500 and order_amount < 2000:
    print("You are eligible for a medium discount.")
    discount = order_amount * 0.10
elif order_amount >= 1000 and order_amount < 1500:
    print("You are eligible for a smaller discount.")
    discount = order_amount * 0.07
else:
    discount = 0
    print("You are not eligible for a discount.")

print("Subtotal:", total_amount)
total_amount -= discount
tax = total_amount * 0.05
print("Discount:", discount)
print("Tax:", tax)
total_amount += tax
print("Final total amount to pay:", total_amount)
print("===== End Task 1 =====")

print("===== Task 2 =====")
all_orders = []
order = [1200,2500,800,1750,3000]
discount_2 = 0
final_amount = 0
roder_discount_count = 0
total_revenue = 0
for amount in order:
    if amount > 2000:
        print(f"Order amount {amount} is eligible for a discount of 15%.")
        discount_2 = amount * 0.15
        roder_discount_count += 1
    elif amount >= 1500 and amount < 2000:
        print(f"Order amount {amount} is eligible for a medium discount of 10%.")
        discount_2 = amount * 0.10
        roder_discount_count += 1
    elif amount >= 1000 and amount < 1500:
        print(f"Order amount {amount} is eligible for a smaller discount of 7%.")
        discount_2 = amount * 0.07
        roder_discount_count += 1
    else:
        print(f"Order amount {amount} is not eligible for a discount.")
        discount_2 = 0
    final_amount = amount - discount_2
    total_revenue += final_amount
    all_orders.append((amount, discount_2, final_amount))
print("All orders with their respective discounts:", all_orders)
print("Number of orders that received a discount:", roder_discount_count)
print("Total revenue from all orders:", total_revenue)
# Print header row
print(f"{'Order Ref':<15} | {'Order Amount':>14} | {'Discount':>10} | {'Final Amount':>14}")
print("-" * 63)

# Print data rows
for o in all_orders:
    print(f"{all_orders.index(o)+1:<15} | ${o[0]:>13.2f} | ${o[1]:>9.2f} | ${o[2]:>13.2f}")

#print(tabulate(all_orders, headers=["Order Amount", "Discount", "Final Amount"], tablefmt="grid"))

print("===== Task 3 =====")
all_orders_add_by_user = []
print("Menu for Task 3:")
print("1. Add an order")
print("2. Show all orders")
print("q. Quit")
while True:
    try:
        manu_code = input("Please select the menu option for Task 3: ")
        #manu_code = int(manu_code)
        discount_3 = 0
        match manu_code:
            case '1':
                order_amount = int(input("Enter the order amount for Task 3: "))
                order_amount = int(order_amount)
                if isinstance(order_amount, (int,)):
                    order_amount = int(order_amount)
                else:
                    print("Invalid input. Please enter a numeric value.")
                all_orders_add_by_user.append(order_amount)
            case '2':
                print("Option 2 selected. show all orders.")
                for amount in all_orders_add_by_user:
                    if amount > 2000:
                        print(f"Order amount {amount} is eligible for a discount of 15%.")
                        discount_3 = amount * 0.15
                    elif amount >= 1500 and amount <= 2000:
                        discount_3 = amount * 0.10
                        print(f"Order amount {amount} is eligible for a medium discount of 10%.")
                    elif amount >= 1000 and amount < 1500:
                        discount_3 = amount * 0.07
                        print(f"Order amount {amount} is eligible for a smaller discount of 7%.")
                    else:
                        print(f"Order amount {amount} is not eligible for a discount.")
                        discount_3 = 0
                    final_amount = amount - discount_3
                    print(f"Final amount for order {amount} after discount is {final_amount}.")
            case 'q':
                break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        break;


print("===== Task 5 =====")
daily = [200,150,0,400,50,-1,300]

total_sales = 0
for sale in daily:
    if sale == -1:
        print("Invalid sale entry detected.")
        break
    elif sale == 0:
        print("No sales for this day.")
        continue
    else:
        print(f"Sales for the day: {sale}")
    total_sales += sale
print("Total sales for the week:", total_sales)
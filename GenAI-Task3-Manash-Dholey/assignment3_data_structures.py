print("===== Task 1 =====")
async def apply_discount(price, discount=None):
    if discount is None:
        discount = 5
    discount_price = 0
    if discount > 60:
        raise ValueError("Discount must be between 0 and 60")
    if discount <= 0 or discount is None or discount == 5:
        discount_price = price * 0.05
        return price - discount_price
    if discount > 0 and discount <= 60:
        discount_price = price * discount / 100
        return price - discount_price

print("===== End of Task 1 =====")
print("===== Task 2 =====")
async def factorial_recursive_example(n):
    try:
        # 1. Handle the negative test case first
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0 or n == 1:
            return 1
        else:
            return n * await factorial_recursive_example(n - 1)
    except ValueError as e:
        print(e)

async def task2_example():
    print(await factorial_recursive_example(5))
    print(await factorial_recursive_example(0))
    print(await factorial_recursive_example(-3))
print("===== End of Task 2 =====")
print("===== Task 3 =====")
gst = lambda price: price + ( 0.18 * price)
final_price = lambda price, discount, gst: price * (1 - discount / 100) * (1 + gst / 100)

async def task3_example():
    print(gst(100))
    print(final_price(100, 10, 18))
    print("===== End of Task 3 =====")

prices = [100, 250, 400, 1200, 50]

async def task4_example():
    print("===== Task 4 =====")
    final_prices = list(map(lambda price: gst(price), prices))
    print("Original prices:", prices)
    print("Final prices after GST:", final_prices)
    print("===== End of Task 4 =====")

prices = [100, 250, 400, 1200, 50,2000,850]
async def task5_example():
    
    print("===== Task 5 =====")
    # discounted_prices = [await apply_discount(price, 10) for price in prices]
    prices_list_graterthan_500 = list(filter(lambda price: price > 500, prices))
    print("Original prices:", prices)
    print("Prices greater than 500:", prices_list_graterthan_500)
    price_list_lesthan_500 = list(filter(lambda price: price <= 500, prices))
    print("Prices less than or equal to 500:", price_list_lesthan_500)
    print("===== End of Task 5 =====")
   
async def process_prices(prices):
    discounted_prices = await asyncio.gather(*map(lambda price: apply_discount(price, 10), prices))
    filtered_prices = list(filter(lambda price: price > 300, prices))
    return discounted_prices, filtered_prices
async def task6_example():
    print("===== Task 6 =====")
    discounted_prices, filtered_prices = await process_prices(prices)
    discounted_prices_one, filtered_prices_one = await process_prices([100, 500, 900, 50,750])
    print("Original prices:", prices)
    print("Discounted prices:", discounted_prices)
    print("Filtered prices (greater than 300):", filtered_prices)
    print("Discounted prices (second list):", discounted_prices_one)
    print("Filtered prices (second list, greater than 300):", filtered_prices_one)
    print("===== End of Task 6 =====")

async def add_price(prices_list, price):
    prices_list.append(price)
    return prices_list
async def get_average_price(prices_list):
    if not prices_list:
        return 0
    return sum(prices_list) / len(prices_list)
async def get_max_price(prices_list):
    if not prices_list:
        return 0
    return max(prices_list)
async def task7_example():
    print("===== Task 7 =====")
    prices_list = [100, 250, 400]
    print("Original prices list:", prices_list)
    # prices_list = await add_price(prices_list, 500)
    # print("Updated prices list after adding 500:", prices_list)
    # prices_list = await add_price(prices_list, 1000)
    # print("Updated prices list after adding 1000:", prices_list)
    # avg_price = await get_average_price(prices_list)
    # print("Average price of the updated list:", avg_price)
    # max_price = await get_max_price(prices_list)
    # print("Maximum price of the updated list:", max_price)
    print("Menu for Task 7:")
    print("1. Add price")
    print("2. Show average price")
    print("3. Show maximum/highest price")
    print("q. Quit")
    while True:
        try:
            manu_code = input("Please select the menu option for Task 7: ")
            if manu_code == "1":
                price = float(input("Enter the price to add: "))
                prices_list = await add_price(prices_list, price)
                print("Updated prices list:", prices_list)
            elif manu_code == "2":
                avg_price = await get_average_price(prices_list)
                print("Average price of the updated list:", avg_price)
            elif manu_code == "3":
                max_price = await get_max_price(prices_list)
                print("Maximum price of the updated list:", max_price)
            elif manu_code.lower() == "q":
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            break
    print("===== End of Task 7 =====")

async def main():
    price = 1000
    print(await apply_discount(price,10))
    print(await apply_discount(price, 20))
    print(await apply_discount(500))
    await task2_example()
    await task3_example()
    await task4_example()
    await task5_example()
    await task6_example()
    await task7_example()

import asyncio
asyncio.run(main())




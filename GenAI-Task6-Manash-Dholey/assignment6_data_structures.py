async def error_handling_example():
    try:
        numerator = input("Enter a number for division(numerator): ")
        denominator = input("Enter a number for division(denominator): ")
        isError = False
        if not numerator.isdigit() or not denominator.isdigit():
            isError = True
            raise ValueError("Invalid input: not an integer")
        if int(denominator) == 0:
            isError = True
            raise ZeroDivisionError("Division by zero")
        # Simulate an error
        if isError:
            result = None
            print("Error occurred, result is None")
        else:
            result = int(numerator) / int(denominator)
            print(f"Result: {result}")
        return result
    except ZeroDivisionError as e:
        isError = True
        print(f"Error occurred: {e}")
        return "Error: Division by zero"
    except ValueError as e:
        isError = True
        print(f"Error occurred: {e}")
        return "Error: Invalid input"
    finally:
        print("Operation completed.")

async def bill_calculator():
    try:
        prices = [120,350,'abc',500,-200,800]
        total_bill = 0
        error_occurred = []
        for price in prices:
            if not isinstance(price, int):
                error_occurred.append(f"Invalid price in the list: {price}")
            if isinstance(price, int) and price < 0:
                error_occurred.append(f"Negative price not allowed: {price}")
            if isinstance(price, int) and price >= 0:
                total_bill += price
        if error_occurred:
            print("Errors occurred:")
            for error in error_occurred:
                print(error)
        print(f"Total bill amount: {total_bill}")
        return total_bill
    except ValueError as e:
        print(f"Error occurred: {e}")
        return "Error: Invalid input"
    finally:
        print("Bill calculation completed.")

async def check_age(age):
    try:
        if not isinstance(age, int):
            raise ValueError("Invalid input: not an integer")
        if age < 0:
            raise ValueError("Invalid input: age cannot be negative")
        if age >= 1 and age <= 120:
            if age < 18:
                print("You are a minor.")
                return "Minor"
            else:
                print("You are an adult.")
                return "Adult"
        else:
            raise ValueError("Invalid input: age must be between 1 and 120")
    except ValueError as e:
        print(f"Error occurred: {e}")
        return "Error: Invalid input"
    finally:
        print("Age check completed.")

async def file_render_error_handling():
    try:
        user_file_name_input = input("Enter the file name: ")
        with open(user_file_name_input, 'r') as file:
             for i in range(3):
                line = file.readline()
                if not line:
                    break  
                print(line, end='')
    except FileNotFoundError as e:
        print(f"Error occurred: {e}")
        return "Error: File not found"
    except PermissionError as e:
        print(f"Error occurred: {e}")
        return "Error: Permission denied"
    finally:
        print("Operation completed.")
async def safe_shopping_cart():
    try:
        cart_list =[]
        total_cost = 0
        while True:
            item = input("Enter item name (or 'q' to finish): ")
            if item.lower() == 'q':
                break
            try:
                price = float(input(f"Enter price for '{item}': "))
            except ValueError:
                print("Invalid input: price must be a number")
                continue
            cart_list.append((item, price))

        for item, price in cart_list:
            if not isinstance(price, (int, float)) or price < 0:
                raise ValueError(f"Invalid price for item '{item}': {price}")
            total_cost += price
        print("total items in cart:", len(cart_list))
        print(f"Total cost or bill of shopping cart: {total_cost}")
        return total_cost
    except ValueError as e:
        print(f"Error occurred: {e}")
        return "Error: Invalid input"
    finally:
        print("Shopping cart processing completed.")

async def main():
    
    try:
        await error_handling_example()
        await bill_calculator()
        await file_render_error_handling()
        await safe_shopping_cart()
        user_age = input("Enter your age: ")
        
        if user_age is not None and not user_age.isdigit():
            raise ValueError("Invalid input: not an integer")
        user_age = int(user_age)
        if user_age is not None and user_age < 0:
            raise ValueError("Invalid input: age cannot be negative")
        if user_age is not None and user_age <= 1 or user_age >= 120:
            raise ValueError("Invalid input: age must be between 1 and 120")
        await check_age(user_age)
        
    except Exception as e:
        print(f"Error occurred: {e}")
    

import asyncio
asyncio.run(main())

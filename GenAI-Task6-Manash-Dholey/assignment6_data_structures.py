def error_handling_example():
    try:
        numerator = int(input("Enter a number for division(numerator): "))
        denominator = int(input("Enter a number for division(denominator): "))
    except ValueError:
        print("Error occurred: Invalid input")
        return "Error: Invalid input"
    else:
        try:
            result = numerator / denominator
        except ZeroDivisionError:
            print("Error occurred: Division by zero")
            return "Error: Division by zero"
        else:
            print(f"Result: {result}")
            return result
    finally:
        print("Operation completed.")


def bill_calculator():
    prices = [120, 350, 'abc', 500, -200, 800]
    total_bill = 0

    try:
        for price in prices:
            try:
                if not isinstance(price, (int, float)):
                    raise TypeError(f"Invalid price in the list: {price}")
                if price < 0:
                    raise ValueError(f"Negative price not allowed: {price}")
                total_bill += price
                print(f"Added {price}; running total: {total_bill}")
            except TypeError as e:
                print(f"Error occurred: {e}")
            except ValueError as e:
                print(f"Error occurred: {e}")

        print(f"Total bill amount: {total_bill}")
        return total_bill
    finally:
        print("Bill calculation completed.")


def check_age(age):
    if not isinstance(age, int):
        raise ValueError("Invalid input: not an integer")
    if age < 0:
        raise ValueError("Invalid input: age cannot be negative")
    if age < 18:
        print("You are a minor.")
        return "Minor"
    if age <= 120:
        print("You are an adult.")
        return "Adult"
    raise ValueError("Invalid input: age must be between 1 and 120")


def file_render_error_handling():
    try:
        user_file_name_input = input("Enter the file name: ")
        with open(user_file_name_input, 'r') as file:
            for _ in range(3):
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
        print("File operation attempted")


def safe_shopping_cart():
    try:
        cart_list = []
        total_cost = 0
        while True:
            item = input("Enter item name (or 'q' to finish): ")
            if item.lower() == 'q':
                break
            try:
                price = float(input(f"Enter price for '{item}': "))
                if price < 0:
                    raise ValueError(f"Negative price not allowed for '{item}': {price}")
            except ValueError as e:
                print(f"Error occurred: {e}")
                continue
            cart_list.append((item, price))

        for item, price in cart_list:
            if not isinstance(price, (int, float))  or price < 0:
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


def main():
    try:
        error_handling_example()
        bill_calculator()
        file_render_error_handling()
        safe_shopping_cart()
        user_age = input("Enter your age: ")
        if user_age is None or user_age.strip() == "":
            raise ValueError("Invalid input: age cannot be empty")
        try:
            user_age = int(user_age)
        except ValueError:
            raise ValueError("Invalid input: not an integer")
        if user_age < 0:
            raise ValueError("Invalid input: age cannot be negative")
        if user_age <= 1 or user_age >= 120:
            raise ValueError("Invalid input: age must be between 1 and 120")
        check_age(user_age)
    except ValueError as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()

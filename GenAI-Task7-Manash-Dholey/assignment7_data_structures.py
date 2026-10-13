from abc import ABC, abstractmethod
class Product:
    def __init__(self, name, price,category):
        self.name = name
        self.price = price
        self.category = category
        self.__price = None       # Private attribute 
    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, category={self.category}), private price={self.__price}"
    def __add__(self, other):
        try:
            if isinstance(other, Product):
                if self.name != other.name:
                    raise ValueError("Cannot combine two different products directly.")
                
                return Product(self.name,self.price + other.price,self.category )  # Adjusted to match the constructor parameters of Product class
        except ValueError as e:
            print(f"Error occurred: {e}")
            return "Error: Cannot combine products"
        
        return NotImplemented
    def get_info(self):
        return f"Product(name={self.name}, price={self.price}, category={self.category}) , private price={self.__price}"
    def apply_discount(self, discount_percentage):
        try:
            if not isinstance(discount_percentage, (int, float)):
                raise ValueError("Discount must be a number")
            if discount_percentage < 0 or discount_percentage > 100:
                raise ValueError("Discount must be between 0 and 100")
            self.price -= self.price * (discount_percentage / 100)
        except ValueError as e:
            print(f"Error occurred: {e}")
            return "Error: Invalid discount"
        
class ElectronicProduct(Product): ## inherits from Product class
    def __init__(self, name, price, category, warranty):
        super().__init__(name, price, category)
        self.warranty_years = warranty

    def __str__(self):
        return f"ElectronicProduct(name={self.name}, price={self.price}, category={self.category}, warranty={self.warranty_years}), private price={self._Product__price}"

    def get_info(self):
        return f"ElectronicProduct(name={self.name}, price={self.price}, category={self.category}, warranty={self.warranty_years}) , private price={self._Product__price}"

class Laptop(Product): ## inherits from ElectronicProduct class
    def __init__(self, name, price, category, warranty, brand):
        super().__init__(name, price, category)
        self.brand = brand
        self.warranty_years = warranty

    def __str__(self):
        return f"Laptop(name={self.name}, price={self.price}, category={self.category}, warranty={self.warranty_years}, brand={self.brand}), private price={self._Product__price}"

    def get_info(self):
        return f"Laptop class (name={self.name}, price={self.price}, category={self.category}, warranty={self.warranty_years}, brand={self.brand}) , private price={self._Product__price}"
class Mobile(Product): ## inherits from Product class
    def __init__(self, name, price, category, brand):
        super().__init__(name, price, category)
        self.brand = brand

    def __str__(self):
        return f"Mobile(name={self.name}, price={self.price}, category={self.category}, brand={self.brand}), private price={self._Product__price}"

    def get_info(self):
        return f"Mobile class (name={self.name}, price={self.price}, category={self.category}, brand={self.brand}) , private price={self._Product__price}"


# 1. Define the abstract base class by inheriting from ABC
class Payment(ABC):
    
    def __init__(self, amount):
        self.amount = amount

    # 2. Define an abstract method (blueprint only, no real implementation)
    @abstractmethod
    def process_payment(self):
        pass

    # 3. Define a concrete method (shared logic available to all child classes)
    def receipt(self):
        return f"Payment of amount {self.amount} has been made."

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number, cardholder_name, expiry_date, cvv):
        super().__init__(amount)
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        self.expiry_date = expiry_date
        self.cvv = cvv

    def process_payment(self):
        try:
            if not self.card_number or not self.cardholder_name or not self.expiry_date or not self.cvv:
                raise ValueError("All credit card details must be provided.")
            if len(str(self.card_number)) != 16:
                raise ValueError("Card number must be 16 digits.")
            if len(str(self.cvv)) != 3:
                raise ValueError("CVV must be 3 digits.")
            if self.amount <= 0:
                raise ValueError("Payment amount must be positive.")
            if not self.expiry_date:
                raise ValueError("Expiry date must be provided.")
            if self.expiry_date <= "00/00":
                raise ValueError("Expiry date must be valid.")
            if not self.cvv:
                raise ValueError("CVV must be provided.")

            return f"Processing credit card payment of {self.amount} using card {self.card_number} belonging to {self.cardholder_name} with expiry date {self.expiry_date} and CVV {self.cvv}."
        except ValueError as e:
            return str(e)

class UPIPayment(Payment):
    def __init__(self, amount, email,upi_id):
        super().__init__(amount)
        self.email = email
        self.upi_id = upi_id

    def process_payment(self):
        try:
            if not self.upi_id:
                 raise ValueError(" UPI ID must be provided.")
            if self.amount <= 0:
                raise ValueError("Payment amount must be positive.")

            return f"Processing UPI payment of {self.amount} using account {self.email} and UPI ID {self.upi_id}."
        except ValueError as e:
            return str(e)
class Inventory:
    def __init__(self, products=None):
        self.products = products if products is not None else []

    def add_product(self, product):
        self.products.append(product)

    def get_all_products(self):
        return self.products
    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                break
    def get_total_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.price
        return total_value
    def show_all_products(self):
        for product in self.products:
            print(product.get_info())

class Store:
    def __init__(self, name, inventory=None):
        self.name = name
        self.inventory = inventory if inventory is not None else Inventory()

    def add_product_to_inventory(self, product):
        self.inventory.add_product(product)

    def remove_product_from_inventory(self, name):
        self.inventory.remove_product(name)

    def get_inventory_total_value(self):
        return self.inventory.get_total_value()

    def show_inventory(self):
        self.inventory.show_all_products()
product = Product("Laptop", 1500, "Electronics")
print(product)
print(product.get_info())
product.apply_discount(10)
print(product)
product.apply_discount(200)  # This should trigger an error
print(product)
product_one = Product("Smartphone", 800, "Electronics")
print(product_one)
print(product_one.get_info())
product_one.apply_discount(15)
print(product_one)
product_one.apply_discount(200)  # This should trigger an error
print(product_one)
electronic_product = ElectronicProduct("TV", 1200, "Electronics", "2 years")
print(electronic_product)
print(electronic_product.get_info()) ## overridden method from ElectronicProduct class and inherited all the attributes and methods from Product class
electronic_product.apply_discount(20)
print(electronic_product)
electronic_product.apply_discount(150)  # This should trigger an error
print(electronic_product)

list_of_laptops = [
    Laptop("MacBook Pro", 2500, "Electronics", "1 year", "Apple"),
    Laptop("Dell XPS 13", 1800, "Electronics", "2 years", "Dell"),
    Laptop("HP Spectre x360", 2000, "Electronics", "2 years", "HP")
]

for laptop in list_of_laptops:
    ##print(laptop)
    print(laptop.get_info())

list_of_mobiles = [
    Mobile("iPhone 13", 1000, "Electronics", "Apple"),
    Mobile("Samsung Galaxy S21", 900, "Electronics", "Samsung"),
    Mobile("Google Pixel 6", 800, "Electronics", "Google")
]

for mobile in list_of_mobiles:
    ##print(mobile)
    print(mobile.get_info())

list_of_upi_payments = [
    UPIPayment(500, "user1@example.com", "user1@upi"),
    UPIPayment(1000, "user2@example.com", "user2@upi"),
    UPIPayment(0, "user3@example.com", "")
]

for upi_payment in list_of_upi_payments:
    print(upi_payment.process_payment())

list_of_credit_card_payments = [
    CreditCardPayment(500, "1234567890123456", "John Doe", "12/25", "12"),
    CreditCardPayment(1000, "9876543210987654", "Jane Smith", "11/24", "456"),
    CreditCardPayment(0, "1111222233334444", "Alice Johnson", "10/23", "789"),
    CreditCardPayment(100, "2222333344445555", "Bob Brown", "00/00", "321"),
    CreditCardPayment(50, "3333444455556666", "", "01/22", "654"),
    CreditCardPayment(200, "44445555666", "Charlie Davis", "02/23", "987"),
    CreditCardPayment(300, "5555666677778888", "David Evans", "03/24", "123"),
]

for credit_card_payment in list_of_credit_card_payments:
    print(credit_card_payment.process_payment())   

laptop_one =  Laptop("MacBook Pro", 2500, "Electronics", "1 year", "Apple")
laptop_two =  Laptop("MacBook Pro", 5500, "Electronics", "1 year", "Apple")
laptop_three = Laptop("MacBook Air", 1500, "Electronics", "1 year", "Apple")
laptop_four = Laptop("MacBook Air", 1800, "Electronics", "2 years", "Dell")
laptop_combined = laptop_one + laptop_two
print("combined laptop:",laptop_combined.get_info())
laptop_combined_two = laptop_four + laptop_three
print("combined laptop with MacBook Air:", laptop_combined_two.get_info())

store = Store("Tech Store")
store.add_product_to_inventory(laptop_one)
store.add_product_to_inventory(laptop_two)
store.add_product_to_inventory(laptop_three)
store.add_product_to_inventory(laptop_four)
store.show_inventory()
print("Total inventory value:", store.get_inventory_total_value())
store.remove_product_from_inventory("MacBook Pro")
store.show_inventory()
print("Total inventory value after removal:", store.get_inventory_total_value())
store.add_product_to_inventory(laptop_combined)
store.add_product_to_inventory(laptop_combined_two)
store.show_inventory()
print("Total inventory value after adding combined laptop:", store.get_inventory_total_value())

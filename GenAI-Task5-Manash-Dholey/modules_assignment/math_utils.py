async def add(a, b):
    return a + b

async def subtract(a, b):
    return a - b

async def multiply(a, b):
    return a * b

async def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
async def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b
async def square(a):
    return a * a

async def cube(a):
    return a * a * a

async def power(a, b):
    return a ** b
async def factorial(a):
    if a < 0:
        raise ValueError("Cannot compute factorial of a negative number")
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result


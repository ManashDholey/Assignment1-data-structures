async def calculate_total(prices):
    return sum(prices)

async def apply_tax(amount):
    return amount + amount * 0.05


async def apply_discount(price, percent):
    return price - (price * percent / 100)

async def flat_discount(price):
    return price - 50

async def percentage_discount(price, percent):
    return price - (price * percent / 100)

async def limited_time_discount(price, percent, expiry_date):
    from datetime import datetime
    if datetime.now() <= expiry_date:
        return price - (price * percent / 100)
    return price
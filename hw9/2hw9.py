DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    if "discount" in customer:
        price = price * (1 - customer["discount"])
    else:
        price = price * (1 - DEFAULT_DISCOUNT)
    return price


print(get_discount_price_customer(10, {"name": "Dima"}))

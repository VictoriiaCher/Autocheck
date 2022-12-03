def cost_15(price):
    return price - price * 0.15


def cost_10(price):
    return price - 0.1 * price


def cost_05(price):
    return price - 0.05 * price


def cost_25(price):
    return price - 0.25 * price


def cost_0(price):
    return price


DISCOUNTS = {"0.15": cost_15, 0.10: cost_10, 0.05: cost_05, 0: cost_0, 0.25: cost_25}


def discount_price(discount):
    return DISCOUNTS[discount]


price = 100


cost_15 = discount_price("0.15")
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))

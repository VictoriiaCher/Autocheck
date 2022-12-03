from functools import reduce


payment = [100, -3, 400, 35, -100]


def amount_payment(payment):
    return reduce((lambda x, y: x + y), filter((lambda x: x > 0), payment))


print(amount_payment(payment))

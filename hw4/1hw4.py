def amount_payment(payment):
    amount = 0
    for value in payment:
        if value > 0:
            amount += value
    return amount


payment = [2, -3, 4, 9, 5]
amount_payment(payment)
print(amount_payment(payment))

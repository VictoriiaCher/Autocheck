def cost_delivery(quantity, *_, discount=0):
    """Обчислює вартість доставки.

    Перший параметр визначає кількість товарів у замовленні, останній - значення знижки (за замовчуванням 0)"""

    price_with = (5 + 2 * (quantity - 1)) * discount
    price_without = 5 + 2 * (quantity - 1)
    price = price_with if discount else price_without
    return price


print(cost_delivery(2, 1, 2, 3))
print(cost_delivery(3, 3))
print(cost_delivery(1))
print(cost_delivery(2, 1, 2, 3, discount=0.5))

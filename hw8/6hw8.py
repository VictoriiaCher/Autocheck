from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    return sum(Decimal(i) for i in number_list) / len(number_list)


print(decimal_average([3, 5, 77, 23, 0.57], 6))
print(decimal_average([4.5788689699797, 34.7576578697964, 86.8877666656633, 12], 6))

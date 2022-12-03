import re


def generator_numbers(string=""):
    num = re.findall(r"\d+", string)
    for i in num:
        yield i


def sum_profit(string):
    num_generator = generator_numbers(string)
    sum = 0
    for i in num_generator:
        sum += int(i)
    return sum


string = "The resulting profit was: from the southern possessions $ 800, from the northern colonies $500, and the king gave $1000."
print(sum_profit(string))

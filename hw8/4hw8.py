from random import randrange, sample


def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000 and min <= quantity <= max:
        lucky_numbers = sample(range(min, max), k=quantity)
        lucky_numbers.sort()
        return lucky_numbers
    else:
        return []


print(get_numbers_ticket(1, 49, 6))

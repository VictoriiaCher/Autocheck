from random import randint


def get_random_password():
    password = ""
    i = 1
    while i <= 8:
        random_num = randint(40, 126)
        i += 1
        password += chr(random_num)
    return password


print(get_random_password())

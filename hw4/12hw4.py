from random import randint

from click import password_option


def get_random_password():
    password = ""
    i = 1
    while i <= 8:
        random_num = randint(40, 126)
        i += 1
        password += chr(random_num)
    return password


def is_valid_password(password):
    upper = False
    lower = False
    number = False
    if len(password) == 8:
        for ch in password:
            if ord(ch) in range(65, 90):
                upper = True
            elif ord(ch) in range(97, 122):
                lower = True
            elif ord(ch) in range(48, 57):
                number = True
        return True if upper is True and lower is True and number is True else False
    else:
        return False


def get_password():
    pas = get_random_password()
    check = is_valid_password(pas)
    i = 0

    while not check and i < 100:
        pas = get_random_password()
        check = is_valid_password(pas)
        i += 1
    return pas


print(get_password())

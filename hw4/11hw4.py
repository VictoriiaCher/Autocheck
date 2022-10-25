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


print(is_valid_password("VVVVVVVV"))
print(is_valid_password("V~HJ(G,2"))
print(is_valid_password("v~hj(g,2"))
print(is_valid_password("V~Hj(G,k"))
print(is_valid_password("V~2j(G,k"))

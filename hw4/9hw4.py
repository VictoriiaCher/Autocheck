def is_valid_pin_codes(pin_codes):
    unique = set(pin_codes)
    k = 0
    if len(unique) == len(pin_codes):
        for i in range(len(pin_codes)):
            if len(pin_codes[i]) == 4 and type(i) != str and pin_codes[i].isdigit():
                k += 1
        return True if k != 0 and k == len(pin_codes) else False
    else:
        return False


print(is_valid_pin_codes(["1001", "9034", "0112", "0112"]))
print(is_valid_pin_codes(["1001", "9034", "00112"]))
print(is_valid_pin_codes(["1001", "9034", "a112"]))
print(is_valid_pin_codes([]))
print(is_valid_pin_codes(["1001", "9034", "0112"]))

def is_integer(s):
    new_s = s.strip()
    if len(new_s) == 0:
        return False
    else:
        if new_s[1:].isdigit():
            return True
        else: return False


print(is_integer("+"))
    
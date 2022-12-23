def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        probel = (length - len(string)) // 2
        probel = probel * " "
        return probel + string


print(format_string(string="aaaaaaaaaaaaaaaaacd", length=12))
print(format_string(length=15, string="abaa"))

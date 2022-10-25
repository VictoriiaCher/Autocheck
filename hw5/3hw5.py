def sanitize_phone_number(phone):
    phone = phone.replace("(", "")
    phone = phone.replace(")", "")
    phone = phone.replace("+", "")
    phone = phone.replace("-", "")
    phone = phone.replace(" ", "")
    return phone


print(sanitize_phone_number("   +  3()8099338-2352   "))

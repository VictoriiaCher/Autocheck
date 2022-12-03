def format_phone_number(func):
    def inner(phone):
        x = func(phone)
        print(x)
        if x.startswith("3"):
            return "+" + x
        else:
            return "+38" + x

    return inner


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

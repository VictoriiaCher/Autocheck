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


def get_phone_numbers_for_countries(list_phones):
    country = ["JP", "SG", "TW", "UA"]
    jp_phone = []
    sg_phone = []
    tw_phone = []
    ua_phone = []
    for phone in list_phones:
        new_phone = sanitize_phone_number(phone)
        if new_phone.find("81", 0, 2) > -1:
            jp_phone.append(new_phone)
        elif new_phone.find("65", 0, 2) > -1:
            sg_phone.append(new_phone)
        elif new_phone.find("886", 0, 3) > -1:
            tw_phone.append(new_phone)
        else:
            ua_phone.append(new_phone)
    phone = [jp_phone, sg_phone, tw_phone, ua_phone]
    return {x: y for x, y in zip(country, phone)}


print(
    get_phone_numbers_for_countries(
        ["+3809987()59405", "818765347", "8881658976 ", "-657658976"]
    )
)

def get_emails(list_contacts):
    list_email = []
    for i in map(lambda x: x["email"], list_contacts):
        list_email.append(i)
    return list_email


list_contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": False,
    },
    {
        "name": "Wylie Pope",
        "email": "est@utquamvel.net",
        "phone": "(692) 802-2949",
        "favorite": False,
    },
    {
        "name": "Cyrus Jackson",
        "email": "nibh@semsempererat.com",
        "phone": "(501) 472-5218",
        "favorite": False,
    },
]

print(get_emails(list_contacts))

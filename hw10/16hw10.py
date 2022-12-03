class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        for i in self.contacts:
            if i["id"] == id:
                self.contacts.remove(i)


Vika = Contacts()
Vika.add_contacts("Vika", "0322666", "sdfhk@gmail.com", True)
Masha = Contacts()
Masha.add_contacts("Masha", "035555", "masha@gmail.com", True)

print(Vika.list_contacts())
print(Masha.list_contacts())

Masha.remove_contacts(2)

print(Masha.list_contacts())
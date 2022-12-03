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
        for i in self.contacts:
            if i["id"] == id:
                
                return i


contact_1 = Contacts()
contact_2 = Contacts()
contact_1.add_contacts("Vika", 265525, "vika@i.net", True)
contact_2.add_contacts("Vitya", 234254, "vitya@i.net", True)
print(contact_2.get_contact_by_id(2))

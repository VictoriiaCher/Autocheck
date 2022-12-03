class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress

    def info(self):
        book_info = {"name": self.name, "age": self.age, "adress": self.adress}
        return book_info


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner

        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()


owner = Owner("Sherlock", 24, "London, 221B Baker Street")
dog = Dog("Barbos", 4, "labrador", owner)

print(dog.who_is_owner())

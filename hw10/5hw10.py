class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return f'Hi!'

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return f"Meow"


cat = Cat("Simon", 10)
print(cat.say())

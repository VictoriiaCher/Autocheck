class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        print(f"Your pet's name is {self.nickname}, it weighs {self.weight} pound")


animal = Animal("Tiger", 4)
animal.say()

cat = Animal("Simon", 2.5)
cat.say()

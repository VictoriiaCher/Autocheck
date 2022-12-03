class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        print(f"Your pet's name is {self.nickname}, it weighs {self.weight} pound")

    def change_weight(self, weight):
        self.weight = weight
        return f"Your pet's weight is {self.weight}"


animal = Animal("Simon", 10)
print(animal.change_weight(12))

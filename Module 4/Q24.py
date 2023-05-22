# Explain inheritance in python with an  example ? what is init ? or what is a constructor in python ?



class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        print("Meow!")

my_dog = Dog("Rufus", "Labrador")
my_cat = Cat("Whiskers", "Orange")

print(my_dog.name)    # Output: Rufus
print(my_cat.species) # Output: Cat
my_dog.make_sound()   # Output: Woof!
my_cat.make_sound()   # Output: Meow!
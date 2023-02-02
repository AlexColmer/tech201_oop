# initialisation
# relates to setting a particular data for an instance of a class
# instantiation creation of an instance of an object

class Dog:


    def __init__(self, name, colour):
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour


    def bark(self):
        return "woof"

fido = Dog("Fido", "Brown")


print(fido.name)
print(fido.colour)

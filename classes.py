


class Dog:
    animal_kind = "Canine"  # class variable

    def bark(self):  # method
        print(self.animal_kind)
        return "Woof"


print(Dog.animal_kind)



fido = Dog()
lassie = Dog()

print(type(fido))
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark())
Dog.animal_kind = "Dolphin" # instance variable rather than a class variable 

print(fido.animal_kind) # now outputs dolphin
print(lassie.animal_kind) # now outputs dolphin

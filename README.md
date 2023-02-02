# oop (object-oriented programming)

- everything in oop is an object and objects are modeled against real world objects 

an objet has both attributes and behaviours 
- Attributes (variables) eg a car has a colour (red, black, green)
- Behaviours (methods) eg a car can def accelerate(), def brake(), def steer()

### classes

These are templates used to create an object. they are a way of bringing both data and functionality of our code together.

- `self` I'm refering to the current class.

``` python
class Dog:
    animal_kind = "canine"  # class variable

    def bark(self):  # method a functon within a class
        print(self.animal_kind)
        return "Woof"
```
bark needs self so that it can find animal_kind class variable if not then it will come up with an error


Instantiation of a class is creating an object from a class

### initialisation 
- relates to setting particular data for an instance of a class
instantiation creation of an instance of an object

```python
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

```
Initialising a class with class variables is good practice. It is possible to set variables at class level but should stay away form this
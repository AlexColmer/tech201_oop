# oop Four Pillars

OOP (object-oriented programming) 
oop is a programing paradigm that uses objects and classes in programming. it aims to implement real world entities. 

![](Class%20diagram.jpg)

- Abstraction - Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only how to use the application
```python
#Abstraction

class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in one breath out")

    def eat(self):
        print("Nom Nom Nom")

    def procreate(self):
        print("Find a mate")

    def move(self):
        print("Onwards and upwards")
cat = Animal()
#cat.breath()
```
- Inheritance -allows us to define a class that inherits methods and properties from another class.
```python
from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None # not all reptiles are tetrapods
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("It's chilly outside, where is the sun?")

    def hunt(self):
        print("Wait wait wait...Pounce")

    def use_venom(self):
        print("If i have got it, I am going to use it")

    def attract_through_scent(self):
        print("Time to spray some eut de toilet")

jeremy_the_reptile = Reptile()
# jeremy_the_reptile.breath()
# jeremy_the_reptile.hunt()
# jeremy_the_reptile.eat()
```
- Encapsulation - When I encapsulate something in my code, I am taking caution to not let outside effects impact that code.
```python
from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None
        self.limbs = False

    def use_tounge_to_smell(self):
        print("Do I say it smells or tastes nice?")

sidney = Snake()
#sidney.seek_heat()

```
- Polymorphism - The word polymorphism means having many forms. In programming, polymorphism means the same function name is used for different types
```python
class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_pray(self):
        print("Ok, let me get the stretchy pants")

    def constrict(self):
        print("Squeeeeeeeeze")

    def climb(self):
        print("Up we go")

    def sheds_skin(self):
        print("I'm growing out of this now")

peter = Python()
peter.hunt()
```


### the benefits of using oop are
- Reusability
- Security
- Flexibility
- Easily upgradable and scalable 

### what is a lambda function

a lambda function in python is an anonymous function (i.e., defined without a name) that can take any number of arguments but, unlike normal functions, evaluates and returns only one expression.

### When are lambda functions used in python
Lambda functions are frequently used with higher-order functions, which take one or more functions as arguments or return one or more functions.


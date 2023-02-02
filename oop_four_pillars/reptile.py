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
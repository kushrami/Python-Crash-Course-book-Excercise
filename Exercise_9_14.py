#Dice:

from random import randint


class Die():
    """Simple class die"""
    def __init__(self,sides):
        self.sides = sides
    def roll_die(self):
        print(randint(1, self.sides)) 

die6 = Die(6)
die6.roll_die()
die6.roll_die()
die6.roll_die()
die6.roll_die()
die10 = Die(10)
die10.roll_die()
die10.roll_die()
die10.roll_die()
die10.roll_die()
die10.roll_die()
die20 = Die(20)
die20.roll_die()
die20.roll_die()
from os import access
from random import randint
from select import KQ_FILTER_SIGNAL
import numbers
import random

class Cards:
    
    def __init__(self, name, value, choice, id):
        self.name = name
        self.value = value

    def __repr__(self, name):
        print(' your drew a {self.name}')
    
        
        pass
    


two= Cards('two', 2, False, 1)
three= Cards('three', 3, False, 2)
four= Cards('four', 4, False, 3)
five= Cards('five', 5, False, 4)
six= Cards('six', 6, False, 5)
seven= Cards('seven', 7, False, 6)
eight= Cards('eight', 8, False, 7)
nine= Cards('nine', 9, False, 8)
ten= Cards('ten', 10, False, 9)
jack= Cards('jack', 10, False, 10)
queen= Cards('queen', 10, False, 11)
king= Cards('king', 10, False, 12)
ace= Cards('ace', 10, True, 13)


def draw_card():
    in_play= False
    while in_play == False:
        print(random.choice(Cards))

print(draw_card())





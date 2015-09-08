import os
import deck_adder

def decks(l):
    basic=[]
    deck_adder.add('Mage/basic.txt',basic)
    l.append(basic)

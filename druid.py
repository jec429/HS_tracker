import os
import deck_adder

def decks(l):
    basic=[]
    deck_adder.add('Druid/basic.txt',basic)
    l.append(basic)

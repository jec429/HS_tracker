import os,glob
import deck_adder

def decks(l):
    for f in glob.glob('Paladin/*.txt'):
        d=[]
        deck_adder.add(f,d)
        l.append(d)

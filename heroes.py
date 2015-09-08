import os,glob
import deck_adder

def druid(l):    
    for f in glob.glob('Druid/*.txt'):
        d=[]
        deck_adder.add(f,d)
        l.append(d)
def paladin(l):    
    for f in glob.glob('Paladin/*.txt'):
        d=[]
        deck_adder.add(f,d)
        l.append(d)
def mage(l):    
    for f in glob.glob('Mage/*.txt'):
        d=[]
        deck_adder.add(f,d)
        l.append(d)
def hunter(l):    
    for f in glob.glob('Hunter/*.txt'):
        d=[]
        deck_adder.add(f,d)
        l.append(d)
def warlock(l):    
    for f in glob.glob('Warlock/*.txt'):
        d=[]
        deck_adder.add(f,d)
        l.append(d)
def warrior(l):    
    for f in glob.glob('Warrior/*.txt'):
        d=[]
        deck_adder.add(f,d)
        l.append(d)
def rogue(l):    
    for f in glob.glob('Rogue/*.txt'):
        d=[]
        deck_adder.add(f,d)
        l.append(d)
def mage(l):    
    for f in glob.glob('Mage/*.txt'):
        d=[]
        deck_adder.add(f,d)
        l.append(d)
def shaman(l):    
    for f in glob.glob('Shaman/*.txt'):
        d=[]
        deck_adder.add(f,d)
        l.append(d)

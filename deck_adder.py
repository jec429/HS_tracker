import os

def add(fn,l):
    f=open(fn)
    for line in f:
        number=line.split(' ')[0].replace('x','')
        name=line.replace(number,'').strip().replace('x ','')
        l.append([int(number),name])

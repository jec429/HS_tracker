import os
import heroes

# Delete the log file after each game or find the breaking point between games
# Windows C:\Program Files (x86)\Hearthstone\Hearthstone_Data\output_log.txt (or just Program Files for 32 bit people)
### mklink C:\Users\YOURUSER\Documents\HS\HS_tracker\Player.log C:\Hearthstone\Hearthstone_Data\output_log.txt
# Mac ~/Library/Logs/Unity/Player.log
f = open('Player.log') # Soft link to the log file is easier
decks=[]
cards=[]
hero=''

#############################################
# LOG PARSER
#############################################
for line in f:
    if 'Zone' in line and 'player=2' in line and 'name=' in line and 'name=[' not in line:
        if 'Malfurion Stormrage' in line:
            hero='druid'
        elif 'Uther Lightbringer' in line:
            hero='paladin'
        elif 'Jaina Proudmoore' in line:
            hero='mage'
        elif 'Rexxar' in line:
            hero='hunter'
        elif 'Garrosh Hellscream' in line:
            hero='warrior'
        elif "Gul'dan" in line:
            hero='warlock'
        elif 'Thrall' in line:
            hero='shaman'
        elif 'Anduin Wrynn' in line:
            hero='priest'
        elif 'Valeera Sanguinar' in line:
            hero='rogue'
        else:
            cards.append(line.split('name=')[-1].split(' id=')[0]) # Card name
            
#############################################
# DECK LOADER
#############################################

if hero is 'druid':
    heroes.druid(decks)
if hero is 'paladin':
    heroes.paladin(decks)
if hero is 'mage':
    heroes.mage(decks)
if hero is 'warrior':
    heroes.warrior(decks)
if hero is 'warlock':
    heroes.warlock(decks)
if hero is 'priest':
    heroes.priest(decks)
if hero is 'hunter':
    heroes.hunter(decks)
if hero is 'shaman':
    heroes.shaman(decks)
if hero is 'rogue':
    heroes.rogue(decks)

#############################################
# DECK FINDER
#############################################
good_cards=[]
#print set(cards)
for x in set(cards): # A set will not see a card that is played twice
    for d in decks:
        good=False        
        for c in d:
            if x in c:
                good=True
        if good:
            good_cards=good_cards+[c[1] for c in d]
#print good_cards
#############################################
# POINT ASSIGNMENT
#############################################          
g=open('cards.txt')
all_cards = [[line.split('\t')[0],0] for line in g]
#print all_cards
for x in good_cards:
    for y in all_cards:
        if x in y[0]:
            y[1]=y[1]+1
            #print x,y

for i in sorted(all_cards, key=lambda x: -x[1]):
    if i[1]>0:
        print (i)

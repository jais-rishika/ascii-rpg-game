import os
# Game Variables
run= True  #running the game
menu= True
play= False
rules= False # see about the game
key= False # cave
fight= False
standing= True #is fight on
buy= False
boss= False
speak= False

#Player Stats
HP= 100 # curr HP
HPMAX=100 # curr MAX HP
ATK =6 #ATTACK
ELIXIR=0
POT=1 #POTION
GOLD=10

def clear():
    os.system("cls")

def draw():
    print("---------- ฅʕ'ᴥ'ʔฅ  ☜╮(•`╭╮´•) ----------"+"\n")

def drawline():
    print(
        "*******-----------------------------------*********"
    )
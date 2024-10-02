import game_state as gs
import battle as b
def shop():
    while gs.buy:
        gs.clear()
        gs.draw()
        gs.drawline()
        print("WELCOME TO The Shop")
        gs.drawline()
        print("GOLD: "+ str(gs.GOLD))
        print("POTIONS: "+ str(gs.POT))
        print("ELIXIR: "+ str(gs.ELIXIR))
        print("ATK: "+ str(gs.ATK))
        gs.drawline()
        print("1-> Buy Potion (30 HP) - 5 GOLD")
        print("2-> Buy ELIXIR (50 HP) - 15 GOLD")
        print("3-> Upgrade Weapon (+2 ATK) - 20 GOLD")
        print("4-> Upgrade HealthBar (+5 HP) - 25 GOLD")       
        print("5-> Leave")
        gs.drawline()
        
        choice=input("# ")
        if choice=="1":
            if gs.GOLD >= 5:
                gs.POT+=1
                gs.GOLD-=5
                print("You've bought a Potion!")
            else:
                print("Not Enough Gold")
            input("> ")
        elif choice=="2":
            if gs.GOLD >= 15:
                gs.ELIXIR+=1
                gs.GOLD-=15
                print("You've bought an Elixir!")
            else:
                print("Not Enough Gold")
            input("> ")
        elif choice=="3":
            if gs.GOLD >= 20:
                gs.ATK+=2
                gs.GOLD-=20
                print("You've upgraded your Weapon!")
            else:
                print("Not Enough Gold")
            input("> ")
        elif choice=="4":
            if gs.GOLD >= 25:
                gs.HPMAX+=10
                gs.HP+=5
                gs.GOLD-=25
                print("Your HP Increased!")
            else:
                print("Not Enough Gold")
            input("> ")
        elif choice=="5":
            gs.buy= False
        else:
            print("Invalid Choice")
            input("> ")

def heal(amount):
    gs.HP=min(gs.HP+amount,gs.HPMAX)
    print("Your HP increased by "+ str(amount))
    
    
def cave():
    while gs.boss:
        gs.clear()
        gs.drawline()
        print(" Cave of The Dragon lies Ahead! What will you Do?")
        gs.drawline()
        if gs.key:
            print("1-> Use Key!")
        print("2-> Turn Back")
        gs.draw()
        
        choice=input("> ")
        if choice=="1":
            if gs.key:
                gs.fight= True
                b.battle()
            else:
                print("You need a Key to Enter the cave, Ask The Mayor!")
        elif choice=="2":
                gs.boss= False
    
    
def mayor(): 
    while gs.speak:
        gs.clear()
        gs.draw()
        gs.drawline()
        print("Hello there, "+gs.name+" !")
        print(" I am the Mayor, are you here for the key to the cave?")
        avg=(gs.ATK+gs.HPMAX)/4
        if avg<40:
            print(" You're not strong Enough to face the Dragon yet! \n Keep Training, Increase your stats and come back later \n we are waiting for you, Hero")
            gs.key=False
        else:
            print("You might want to take on the dragon now! Take this key, but be careful with the beast!")
            gs.key = True
        gs.drawline()
        print("1-> Leave")
        gs.draw()
        
        choice=input("# ")
        if choice=="1":
            gs.speak= False
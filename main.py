import os, random , time 
import battle as b
import game_state as gs
import game_func as gf
import game_model as gm

x=0
y=0

x_len=len(gm.map[0])-1
y_len=len(gm.map)-1

def save():
    list=[
        gs.name,
        str(gs.HP),
        str(gs.ATK),
        str(gs.ELIXIR),
        str(gs.POT),
        str(gs.GOLD),
        str(x),
        str(y),
        str(gs.key),
    ]
    
    f=open("load.txt", "w")
    for item in list:
        f.write(item + "\n")
    f.close()
     
while gs.run:
    while gs.menu:
        gs.clear()
        gs.draw()
        print("1-> New Game")
        print("2-> Load Game")
        print("3-> Rules")
        print("4-> Quit Game")
        
        if gs.rules:
            print("These are the rules")
            gs.rules= False
            choice=""
            input("> ")
        else:
            choice=input("# ")
        # choice= int(input("Enter your choice: "))
        if choice=="1":
            gs.clear()
            gs.name= input("Enter your name: ")
            gs.play=True
            gs.menu=False
        elif choice=="2": 
            gs.clear()
            try:
                f=open("load.txt","r")
                load_list= f.readlines()
                if len(load_list)==9:
                    gs.name= load_list[0][:-1]
                    gs.HP= int(load_list[1][:-1])
                    gs.ATK= int(load_list[2][:-1])
                    gs.ELIXIR= int(load_list[3][:-1])
                    gs.POT= int(load_list[4][:-1])
                    gs.GOLD= int(load_list[5][:-1])
                    x= int(load_list[6][:-1])
                    y= int(load_list[7][:-1])
                    gs.key= bool(load_list[8][:-1])
                
                    print("welcome back "+ gs.name)
                    input(">")
                    gs.menu= False
                    gs.play=True
                else:
                    print("Corrupt file")
                    input("> ")
            except OSError:
                print("No saved game found")
                input("> ")
        elif choice=="3": 
            pass
        elif choice=="4": {
            quit()
        }
    
    while gs.play:
        save()
        gs.clear()
        gs.draw()
        if not gs.standing:
            if gm.biom[gm.map[y][x]]["e"]:
                if random.randint(0,100) <= 30:
                    gs.fight= True
                    b.battle()
        if gs.play:          
            gs.drawline()
            print("LOCATION "+ gm.biom[gm.map[y][x]]["t"])
            gs.drawline()
            print("------------------0, Save and quit ---------------------")
            print("NAME: "+gs.name)
            print("HP: " + str(gs.HP))
            print("ATK: " + str(gs.ATK))
            print("ELIXIR: " + str(gs.ELIXIR))
            print("POTION: " + str(gs.POT))
            print("GOLD: " + str(gs.GOLD))
            gs.drawline()
            print("0-> Save and Quit")
            print("\n MOVE \n")
            if y>0:
                print("1-> North")
            if x<x_len:
                print("2-> East")
            if y<y_len:
                print("3-> South")
            if x>0:
                print("4-> West")
            if gs.POT > 0:
                print("5 - USE POTION (30HP)")
            if gs.ELIXIR > 0:
                print("6 - USE ELIXIR (50HP)")
            if gm.map[y][x] =="shop" or gm.map[y][x] =="mayor" or gm.map[y][x]=="cave":
                print("7 - Enter")
            gs.drawline()
            dest= input("# ")
            if dest=="0":
                gs.play= False
                gs.menu=True
                save()
                
            if dest=="1":
                if y>0:
                    y-=1
                    gs.standing= False
                    
            elif dest=="2":
                if x<x_len:
                    x+=1
                    gs.standing= False
                    
            elif dest=="3":
                if y<y_len:
                    y+=1
                    gs.standing= False
                    
            elif dest=="4":
                if x>0:
                    x-=1
                    gs.standing= False
                    
            elif dest == "5":
                if gs.POT > 0:
                    gs.POT = max(gs.POT-1,0)
                    gf.heal(30)
                else:
                    print("No potions!")
                input("> ")
                gs.standing = True
                
            elif dest == "6":
                if gs.ELIXIR > 0:
                    gs.ELIXIR = max(gs.ELIXIR-1, 0)
                    gf.heal(50)
                else:
                    print("No elixirs!")
                input("> ")
                gs.standing = True
                
            elif dest == "7":
                if gm.map[y][x] == "shop":
                    gs.buy = True
                    gf.shop()
                if gm.map[y][x] == "mayor":
                    gs.speak = True
                    gf.mayor()
                if gm.map[y][x] == "cave":
                    gs.boss = True
                    gf.cave()
                gs.standing=True
            else:
                print("Invalid Input. Please Enter a Number")
                gs.standing=True
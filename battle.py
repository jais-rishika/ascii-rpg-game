import random, os
import game_state as gs
e_list = ["Goblin", "Orc", "Slime"]

mobs = {
    "Goblin": {
        "hp": 30,
        "at": 8,
        "go": 10
    },
    "Orc": {
        "hp": 40,
        "at": 12,
        "go": 18
    },
    "Slime": {
        "hp": 15,
        "at": 5,
        "go": 6
    },
    "Dragon": {
        "hp": 100,
        "at": 16,
        "go": 100
    }
}

def battle():
    if not gs.boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    hp=mobs[enemy]["hp"]
    hpmax=hp
    atk=mobs[enemy]["at"]
    g=mobs[enemy]["go"]
    
    while gs.fight:
        gs.clear()
        gs.draw()
        gs.drawline()
        print("Defeat the "+enemy+" !!! \n")

        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(gs.name + "'s HP: " + str(gs.HP) + "/" + str(gs.HPMAX))
        gs.drawline()
        print("POTION "+ str(gs.POT))
        print("ELIXIR "+ str(gs.ELIXIR))
        gs.drawline()
        print("1-> ATK")
        if gs.POT>0:
            print("2-> POTION")
        if gs.ELIXIR>0:
            print("3-> ELIXIR")
        gs.drawline()
        
        choice=input("# ")
        if choice =="1":
            a =random.randint(0,gs.ATK)
            hp-=a
            if(a==0):
                print("Damn!!")
                print("Enemy Defended Against You!!")
            else:
                print(gs.name + " dealt " + str(a) + " damage to the " + enemy + ".")
            if hp > 0:
                a= random.randint(0,atk)
                if a==13:
                    print("Dragon used Flame Thrower!!!  Big Damage!! -50HP")
                    gs.HP-= 50
                else:
                    gs.HP -= a
                if(a==0):
                    print("Good Defence!!")
                    print(" \n You Defended against the Enemy")
                else:
                    print(enemy + " dealt " + str(a) + " damage to " + gs.name + ".")
            input("> ")
        
        elif choice =="2":
            if gs.POT>0:
                gs.POT=max(gs.POT-1,0)
                gf.heal(30)
                a=random.randint(0,atk)
                gs.HP -=a
                if(a==0):
                    print("Good Defence!!")
                    print(" \n You Defended against the Enemy")
                else:
                    print(enemy + " dealt " + str(a) + " damage to " + gs.name + ".")
            else:
                print("No potions!")
            input("> ")
        
        elif choice=="3":
            if POT>0:
                gs.ELIXIR=-1
                gf.heal(50)
                a =random.randint(0,atk)
                gs.HP -= a
                if(a==0):
                    print("Good Defence!!")
                    print(" \n You Defended against the Enemy")
                else:
                    print(enemy + " dealt " + str(atk) + " damage to " + gs.name + ".")
            else:
                print("No Elixir!")
            input("> ")
        else :
            print("Invalid Input, -1 HP ")
            gs.HP-=atk
        
        if gs.HP<=0:
            print(enemy+ " has Defeated "+ gs.name)
            gs.fight= False
            gs.play= False
            gs.run= False
            gs.drawline()
            print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
            print(gs.name + "'s HP: " + str(max(gs.HP,0)) + "/" + str(gs.HPMAX))
            print("""
                   * * * *  * * *  *       *  * * *     * * * *  *       *  * * *  * * *  
                   *        *   *  * *   * *  *         *     *   *     *   *      *   *  
                   *   * *  * * *  *   *   *  * * *     *     *    *   *    * * *  * * 
                   *     *  *   *  *       *  *         *     *     * *     *      *   *
                   * * * *  *   *  *       *  * * *     * * * *      *      * * *  *    *
                  """)
            gs.drawline()
            input("> ")
            gs.clear()
        
        if hp<=0:
            print("Great")
            print(gs.name+ " has Defeated the "+ enemy)
            gs.draw()
            gs.drawline()
            gs.fight= False
            gs.GOLD+=g
            if random.randint(0,100)%3==0:
                print("Yeah!!!!! \n You found a potion!")
                gs.POT+=1
            if enemy=="dragon":
                print("Congratulation!! You Finished the game!")
                gs.boss= False
                gs.run= False
                gs.play= False
            input("> ")
            gs.clear()
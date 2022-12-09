#ONCE DONE NEED TO ADD ALL THE CODES WORKED ON THIS TOGETHER SUCH AS dc 11-29, AND 11-30
print("   @. .@    ")
print("  ( ---- )  ")
print(" (  >___<  )")
print("  ^^ ~~ ^^  ")


import winsound
winsound.Beep(500, 500)

print("You wake up on the floor in a room, you look around, wondering where you are.")
print("All of a sudden you hear a voice from the speaker that is connected to your room.")
print("It says: Welcome you have been selected to participate in this experient, you have 96 hours to escape, if you do not escape in time the helicopter that is here to take you back home will leave.")
print("Good luck")
import time
import random
#start of game loop------------------------------------------------------------------------------------------------------------------------
inventory = []
PlayerHealth = 100
PlayerHealth = 100
def BossBattle(PlayerHealth):
    TigerHealth = 100
    while TigerHealth >0 and PlayerHealth >0:
        if inventory[0] =="woodend sword":
            damage = random.randrange(20,31) #more damage whe you have the sword
        else:
            damage = random.randrange(5, 11)
        print("You hit the tiger for", damage, "HP")#I dont want to hit the tiger if they have ham and if they have a broken sword
        TigerHealth -= damage
        print("The tigers now has", TigerHealth, "HP.")
        damage = random.randrange(5,16)
        print("The tiger attacks you for", damage, "HP")#I dont want to hit the tiger if they have ham and if they have a broken sword
        PlayerHealth -= damage
        print("You have", PlayerHealth, "HP left, and the tiger has", TigerHealth, "HP left.")
        choice = input("press p for potion, H for ham, or any other key to continue")
        if choice == "p":
            if inventory[3]=="health potion":
                print("glug glug (xp+20)")
                PlayerHealth +=20
                inventory[3] = "empty"
            else:
                print("sorry, you have no potion")
        elif choice == "H":
            if inventory[2]=="Ham":
                print("you have feed the tiger the ham, and is happy and goes away!")
                TigerHealth = 0
            else:
                print("the tiger is not happy that you ate the ham, and decides to eat you, it got sick from your bacteria and died, so thanks a lot you killed my pet tiggy :(")
                PlayerHealth = 0
                #Break statment if needed
            
        print()
    if PlayerHealth <= 0:
        TimeLeft = 0
        print("you lost the game!,start over ig")
    elif TigerHealth <= 0:
        print("The tiger dead, and guess what tigers are becoming extinct!:(")
    return PlayerHealth
doExit = False #runs game loop
room = 1
choice = 'a'
def FloorFall():
    num = random.randrange(0, 100)
    if num < 65 :
        print("The floor opens you are falling down into a tank full of sharks, You have DIED!!!!")
        PlayerHealth = 0
        return True
    else:
        print("the floor feels soggy!!!, so you quickly chose to move on to the next room")
        return False
    #print("your inventory:", end = "")
    print(inventory)
start = time.time()#starting time for game
TimeLeft = 120 #how many seconds to give the user to complete the game
while TimeLeft > 0:
    print()
    newTime = time.time()#get current time
    timeElapsed = start - newTime #check how much time has passed
    print(int(timeElapsed*-1), "seconds have passed.")#print how much has passed
    TimeLeft += timeElapsed #decrement the counter
    print("you have", int(TimeLeft), "seconds left to complete the game!")#print time left
    if TimeLeft < 0:
        print("The helicopter has left with out you, you just lost the game.")
        break
#room1-------------------------------------------------------------------------------------------------------------------------------------
    if room ==1: #NEED TO ADD THE SWORD TO THERE INVENTORY
        print("you are in room 1, you can go (e)ast")
        print("In this room there is nothing in your surroundings but a wooden sword right next to your feet")
        choice = input()
        inventory.append("woodend sword")
        print("you chose to pick up the sword just in case, as you leave and move on to the next room")
        if choice == 'e' or choice == 'east':
            room = 2
        else:
            print("Not an option")
        print(inventory)
#room2-------------------------------------------------------------------------------------------------------------------------------------
    if room ==2:#YOU CANT GO TO ROOM 7 THROUGH HERE SINCE IT IS LOCKED 
        print("you are in room 2, you can go (w)est or (s)outh or (e)ast, There is a bookshelf full of cobwebs in the corner. Would you like to look at it? (y)es")
        choice = input()
        if choice == 'yes' or choice == "y":
            print("As you look at the bookshelf you see dusty old books that look like they have not been used for years, as you start to give up on looking for clues you realize that there is a key on the top shelf")#MAKE IT SO THAT THEY CAN ONLY FIND THE KEY ONCE AND CAN NOT HAVE MULTIPLE OF THE KEYS
            print("You found a key!!!")
            inventory.append("key")
        if choice == 'west' or choice == 'w':
            room = 1
        elif choice == 'south' or choice == 's':
            room = 3
        elif choice == 'east' or choice == 'e':
            print("The door to room 7 is locked try going west or south!")
        print(inventory)
#room3--------------------------------------------------------------------------------------------------------------------------------------
    if room ==3:#SAME AS ROOM 2
        print("you are in room 3, you can go (n)orth, (s)outh, or (e)ast")
        choice = input()
        if choice == 'north' or choice == 'n':
            room = 2
        elif choice == 'south' or choice == 's':
            room = 4
        elif choice == 'east' or choice == 'e':
            print("Can not go to room 6 door is locked, try going to room 4")
        else:
            print("Not an option")
        print(inventory)
#room4--------------------------------------------------------------------------------------------------------------------------------------
    if room ==4:#NEED TO REMOVE SWORD IF THEY USE SWORD TO OPEN CHEST 
        print("you are in room 4, you can go north(n) or east(e), or look at the brown wooden chest to the right of you. would you like to use the (s)word or (k)ey for the chest (y)es or no")
        choice = input()
        if choice == 'yes' or choice == 'y':
             print("use (w)ooden sword or (k)ey")
        choice = input()
        if choice == 'woodendsword' or choice == 'w' or choice == 'W':
            print("You broke your sword, you should try the key")
            hasWoodenSword = False
            for i in range(len(inventory)):
                if inventory[i] == 'woodend sword':
                    hasWoodenSword = True
                if hasWoodenSword == True:
                    inventory[0] = "" 
                    print(inventory)
                    hasWoodendSword=False #this erases the sword
        elif choice == 'key' or choice == 'k' or choice == 'K':
            print("Go back to the rooms before and look for a key")
            hasKey = False
            for i in range(len(inventory)):
                if inventory[i] == 'key':
                    hasKey = True
                if hasKey== True:
                    inventory.append("Ham")
                    print("You opened the chest in the corner with the key, in chest there is ham")#repeats 
                    inventory[1] = "" #erase the key
                    print(inventory)
                    hasKey=False
        if choice == 'north' or choice == 'n':
            room = 3
        elif choice == 'east' or choice == 'e':
            room = 5
#Room 5-------------------------------------------------------------------------------------------------------------------------------------  
    if room ==5:
        print("you are in room 5 there are vials of liquid all around the room,you can go (n)orth or (w)est ")
        choice = input()
        print("you take one of those vials and they so happen to be a health potion")#THE VIAL OF HEALTH POTION IS ADDED EVERY TIME THEY COME BACK TO THIS ROOM
        inventory.append("health potion")
        if FloorFall() == True:
            doExit = True#THE PROBABILITY OF THE PERSON DYING IS 65% AND THEN THE PLAYER MUST RESTART
            break
        if choice == 'north' or choice == 'n':
            room = 6
        elif choice == 'west' or choice == 'w':
            room = 4
        else:
            print("Not an option")
        print(inventory)
#Room 6------------------------------------------------------------------------------------------------------------------------------------
    if room ==6:
        print("you are in room 6, you can go north(n) or west(w)")
        choice = input()
        if choice == 'north' or choice == 'n':
            room = 7
        elif choice == 'west' or choice == 'w':
            room = 3
        else:
            print("Not an option")
        print(inventory)
#Room 7-------------------------------------------------------------------------------------------------------------------------------------          
    if room ==7:
        print("you are in room 7, you can go west(w), south(s) or (e)ast")
        choice = input()
        if choice == 'west' or choice == 'w':
            room = 2
        elif choice == 'south' or choice == 's':
            room = 6
        elif choice == 'east' or choice == 'e':
            room = 8
        else:
            print("Not an option")
        print(inventory)
#Room 8-------------------------------------------------------------------------------------------------------------------------------------          
    if room ==8:
        print("you are in room 8, you can go west(w) or (s)outh", "You seem to be hungry do you wish to eat your ham?, (y)es or (n)o")
        choice = input()
        if choice == 'yes' or choice == 'y':#NEED TO FIX TO REMOVE HAM IF IT WAS EATEN
            print("press e to eat ham")
            choice = input()
        if choice == 'e':
            print("you have eaten your ham and it was not that good, pretty cold :(")
            hasHam = False
            for i in range(len(inventory)):
                if inventory[i] == 'Ham':
                    hasHam = True
                if hasHam== True:
                    inventory[2] = "" 
                    print(inventory)
                    hasHam=False
            print("chose to go (w)est or (s)outh then")     
        elif choice == 'no' or choice == 'n':
            print("You chose to not eat your ham :(, so go west or south in this game then")
        choice = input()
        if choice == 'west' or choice == 'w':
            room = 7
        elif choice == 'south' or choice == 's':
            room = 9
        else:
            print("Not an option")
        print(inventory)
#Room 9------------------------------------------------------------------------------------------------------------------------------------           
    if room ==9:#THIS IS LIKE THAT LAST LEVEL THAT THE PERSON MUST COMPLETE TO MAKE IT OUT
        print("you are in room 9, in this room you see a desk full of papers, you decide to inspect it and realize that the papers are junk, you start to give up on looking for clues when you see that under a reciept for ham there is a old flip phone, do you wish to pick it up?")
        print("press (y)es to pick the phone up, or press (n)o move on to the next rooms which are (w)est, (n)orth or (e)ast")
        choice = input()
        if choice == 'y' or choice == 'yes':
            print("There is no service in this building maybe the phone will work outside for if you make it!, now move to the next room")
            inventory.append("phone") 
        elif choice == 'n' or choice == 'no':
            print("YOU SHOULD HAVE PICKED UP THE PHONE BUT OH WELL I GUESS, now move to the next room")
        choice = input()
        if choice == 'west' or choice == 'w':
            room = 6
        elif choice == 'north' or choice == 'n':
            room = 8
        elif choice == 'east' or choice == 'e':
            room = 10
        else:
            print("Not an option")
        print(inventory)
#Room 10------------------------------------------------------------------------------------------------------------------------------------
    if room ==10:#NEED TO ADD SOMETHING SO THAT IF THEY DO NOT MAKE IT IN TIME THE HELECOPTER LEAVES WITH OUT THEM AND THEY ARE STRANDED THERE OR IF THEY DO MAKE IT THEY LEAVE WITH THE HELICOPTER
            PlayerHealth =  BossBattle(PlayerHealth) #ONCE DONE MOVE IT TO ROOM 9
            if PlayerHealth <= 0:
                break
            print("you are in room 10 the last room that you need to escape from, you can go (s)outh or (e)ast")
            choice = input()
            if choice == 'south' or choice == 's':
                room = 9
            elif choice == 'east' or choice == 'e':
                room = 11
                print("CONGRATULATIONS YOU HAVE ESCAPED THE BUILDING. As you exit the building your eyes adjust to the bright, as you look at your surroundings you see that you are in the middle of nowhere,you check your flipphone to see if it has service and it doesnt sorry?")
            else:
                print("Not an option")
            
#end of game loop --------------------------------------------------------------------------------------------------------------------------
if PlayerHealth <= 0:
    print("you lost")
end = time.time() #HAVE TO MAKE IT SO THAT THEY LEAVE IF THE Y MAKE IT OUT BEFORE 0 AND HAVE TO MAKE IT SO IT SAYS THAT THEY SEE HELICOPER  LEAVING THEM 

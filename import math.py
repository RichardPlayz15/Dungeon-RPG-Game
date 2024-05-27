import math

#Dungeon RPG - Levels and Growths and Stats and Name and Classes Implemented, Fully Functional
#records stats
PHP=0
MaxHP=0
PATK=0
PDEF=0
LVL=0
MaxMana=10
Mana=10 
EXP=0
HPRaise=0
ATKRaise=0
DEFRaise=0
Flee=0
ManaRaise=0
Class=0
Dead=0
Reunited=0
Heal=0
SacrTrue=0
MGCDN1=0
Monst1=0
MagiChest2=0
FinalBoss=0
FB=0
Complete=0

#asks the user to input a name
Name=input("Enter your Character's Name: ")

#lists posable classes alongside a hint for secret classes
while Class==0:
  Class = int(input("Choose your Class: Assassin, Soldier, or Knight. Enter 1 for Assassin, 2 for Soldier, and 3 for Knight (And you can enter other numbers if you want to see you can find a secret):: "))

#picks class depending on which number you pick
  if Class!=1 and Class!=2 and Class!=3 and Class!=2187 and Class!=1987:
    print("That's not an option!\n")
    Class=0

  #Assassin class stats
  if Class==1:
    MaxHP=15
    PHP=15
    PATK=7
    PDEF=3
    print("You chose the Assassin Class!\n\nYour Current Stats Are::")
    print("\nHealth: " , PHP)
    print("Mana: " , Mana)
    print("Attack: " , PATK)
    print("Defense: " , PDEF)
    HPRaise=2
    ATKRaise=3
    DEFRaise=2
    ManaRaise=1

#Soldier class stats
  if Class==2:
    MaxHP=20
    PHP=20
    PATK=6
    PDEF=4
    print("You chose the Soldier Class!\n\nYour Current Stats Are::")
    print("\nHealth: " , PHP)
    print("Mana: " , Mana)
    print("Attack: " , PATK)
    print("Defense: " , PDEF)
    HPRaise=2
    ATKRaise=2
    DEFRaise=3
    ManaRaise=2

  #Knight class stats
  if Class==3:
    MaxHP=30
    PHP=30
    PATK=2
    PDEF=6
    print("You chose the Knight Class!\n\nYour Current Stats Are::")
    print("\nHealth: " , PHP)
    print("Mana: " , Mana)
    print("Attack: " , PATK)
    print("Defense: " , PDEF)
    HPRaise=3
    ATKRaise=2
    DEFRaise=4
    ManaRaise=3

#secret class stats #1 Jedi Class
  if Class==2187:
    MaxHP=50
    PHP=50
    PATK=10
    PDEF=10
    print("You are now the Jedi Class!\n\nYour Current Stats Are::")
    print("\nHealth: " , PHP)
    print("Mana: " , Mana)
    print("Attack: " , PATK)
    print("Defense: " , PDEF)
    HPRaise=10
    ATKRaise=10
    DEFRaise=10
    ManaRaise=10

  #secret class stats #2 Animatronic Class
  if Class==1987:
    MaxHP=1000
    PHP=1000
    PATK=500
    PDEF=500
    print("You are now the Animatronic Class!\n\nYour Current Stats Are::")
    print("\nHealth: " , PHP)
    print("Mana: " , Mana)
    print("Attack: " , PATK)
    print("Defense: " , PDEF)
    HPRaise=100
    ATKRaise=15
    DEFRaise=15
    ManaRaise=15


#start of the game and story
LVL=1
print("You are now Level 1!\n\n\n")
intro=int(input("Would you like to hear the story? Enter 1 for Yes, and 2 for No:: "))

#plays the story and gives 3 options
if intro==1:
  print("\nYou, " , Name , ", are a traveling Mercenary in the Medieval Times. Mostly you get small jobs, like getting a stolen item back, or spying on the police to back them up on a minor operation. Today, you got your biggest job yet. Your client had a large, priceless collection of diamonds stolen by some monsters. The monsters were seen heading into a cave dungeon. That's where you are heading now.")

Fork1=int(input("The moment you enter the cave, there is a fork in the road. There are 3 ways you can go. Left, Straight, or Right. Enter 1, 2, or 3 respectively to choose which way to go: "))

if Fork1==1:
  print("You encountered a Werewolf! Engage Battle!")
  EHP=15
  EATK=5
  EDEF=3

if Fork1==2:
  print("You encountered a Ransacker!! Engage Battle!")
  EHP=12
  EATK=4
  EDEF=5

if Fork1==3:
  print("You encountered a Treasure Chest! It's Guarded by a Werewolf!! Engage Battle!")
  EHP=15
  EATK=5
  EDEF=3  

#while in an encounter it will display stats and give you options to Attack, use a Fire Spell that costs 2 Mana, or Flee
while EHP>0 and PHP>0 and Flee==0:
  print(Name, "HP: " , PHP)
  print(Name, "Mana: " , Mana)
  print("Enemy HP: " , EHP)
  AC=int(input("Choose your move: \n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Flee."))

  if AC!=1 and AC!=2 and AC!=3:
    AC=1

  if AC==2 and Mana<2:
    AC=1

  if AC==1:
    Mana=Mana+1
    if Mana>MaxMana:
      Mana=MaxMana
    DMG=PATK-EDEF
    if DMG<1:
      DMG=1

  if AC==2:
    Mana=Mana-2
    DMG=PATK*2-EDEF
    if DMG<1:
      DMG=1

  #if choose to flee it will either display if you can flee or not
  if AC==3:
    if Fork1==1 or Fork1==2:
      print("Cannot Flee!")
      Flee=2
    if Fork1==3:
      Flee=1
      print("Fled from Battle!")

  #tells the user that they attacked the monster and which damage option they picked
  if Flee==0:
    EHP=EHP-DMG
    print(Name , "Attacked!" , DMG , " Damage Dealt!\n")

#tells the user that the Enemy attacked the user
  if Flee==0 and EHP>0 or Flee==2 and EHP>0:
    DMG=EATK-PDEF
    if DMG<1:
      DMG=1
    PHP=PHP-DMG
    print("Enemy Attacked! " , Name , "Took " , DMG , " Damage!\n")
    Flee=0

  #tells the user that they beat the monster and how much exp was awarded
  if EHP<1 and Flee==0:
    print("The Enemy has been defeated! 10 EXP Gained!")
    EXP=EXP+10
    if EXP>=10:
      LVL=LVL+1
      PATK=PATK+ATKRaise
      PDEF=PDEF+DEFRaise
      MaxHP=MaxHP+HPRaise
      MaxMana=MaxMana+ManaRaise
      PHP=MaxHP

#tells the user that they leveled up and learned a new spell
      print("\nYou've leveled up! You are now Level 2! You've learned Heal Spell!")
      Heal=1
      print("Your stats are now: ")
      print("\nHealth: " , MaxHP)
      print("Mana: " , MaxMana)
      print("Attack: " , PATK)
      print("Defense: " , PDEF)

  #tells the user that they had been defeated
  if PHP<1 and Flee==0:
    print(Name , "has been defeated! Game Over!")
    Dead=1

#depending on if the user uses the secret class code 2187 and picks to open one of the chests the user will get an item to help them on there jorney
if Flee==0 and PHP>1:
  PHP = MaxHP
  Mana=MaxMana
  if Fork1==3 and Class!=2187:
    print("You got a Steel Sword! Attack Raised by 2!")
    PATK=PATK+2
  if Fork1==3 and Class==2187:
    print("You got a Lightsaber! Attack Raised by 30!")
    PATK=PATK+30

#if you flee then you get past the Werewolf guarding the chest so you do not get a reward but you live so you continue down the Dungeon
if Flee==1:
  print("You didn't defeat the Werewolf guarding the Chest, so you didn't get the Treasure! Continuing on in the Dungeon.")
  Flee=0

if Dead!=1 and Fork1==1:
 Fork12=int(input("You continue on in the dungeon and find a second fork. There are 2 paths. Choose 1 for Left and 2 for Right: "))

#you find a Treasure Chest with nothing to stop you, you can choose to open it or not, if you decide to open it you get a shield and raise defence, but if not then you skip it and nothing happenes
 if Fork12==1:
   chest12=int(input("You found a Treasure Chest! Nothing is guarding it! Do you want to open it? Enter 1 to open it. Enter anything else to skip it: "))
   if chest12==1:
      print("You found a Steel Shield Inside! Your Defense was Raised by 2!")
      PDEF=PDEF+2
   else:
      print("You decided to skip the Chest.")

      #you find a Wandering Soldier but he want the treasure that you were hired to find, so he challenges you to a fight for the treasure
 if Fork12==2:
   print("You've found a Wandering Soldier!")
   print("\nSoldier:: Hey! You're that guy the rich dude hired to get his treasure back, right!?\n",Name,":: Yes.\nSoldier:: Well I want that treasure! If you want it you have to get through me!")

   EHP=30
   EATK=10
   EDEF=6 

#you can pick if you want to Attack, use a Fire Spell that costs 2 Mana, use a Heal Spell that costs 4 Mana, or flee
   while EHP>0 and PHP>0:
      print(Name, "HP: " , PHP)
      print(Name, "Mana: " , Mana)
      print("Enemy HP: " , EHP)
      AC=int(input("Choose your move: \n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Heal Spell: 4 Mana\n4 - Flee."))

      if AC!=1 and AC!=2 and AC!=3 and AC!=4:
        AC=1

      if AC==2 and Mana<2:
        AC=1

  #if you pick option 1 you gain 1 mana and do physical damage
      if AC==1:
        Mana=Mana+1
        if Mana>MaxMana:
          Mana=MaxMana
        DMG=PATK-EDEF
        if DMG<1:
          DMG=1

  #if you pick option 2 which is Fire Spell you lose 2 mana and do magic damage
      if AC==2:
        Mana=Mana-2
        DMG=PATK*2-EDEF
        if DMG<1:
          DMG=1

#if you pick option 3 which is Heal Spell you lose 4 mana and gain 10 Health
      if AC==3:
        Mana=Mana-4
        PHP=PHP+10
        if PHP>MaxHP:
          PHP=MaxHP

#if you pick option 4 which is flee you can't
      if AC==4:
        print("Cannot Flee!")

      #if option 1 (normal attack) or 2 (spell attack) the user attacks the enemy
      if AC==1 or AC==2:
        EHP=EHP-DMG
        print(Name, "attacked!",DMG, "damage dealt!")

      #if option
      if AC==3:
        print(Name, "cast Heal Spell! 10 HP Recovered.")

      #tells the user that the Enemy attacked the user
      if EHP>0:
        DMG=EATK-PDEF
        if DMG<1:
          DMG=1
        PHP=PHP-DMG
        print("Enemy Attacked! " , Name , "Took " , DMG , " Damage!\n")

      #if health points reaches less then 1 user dies
      if PHP<1:
        print("You have died!")
        Dead=1

      #you defeat the Soldier and gains 30 experience points
      if EHP<1:
        print("You have defeated the Soldier! You have gained 30 EXP!")
        EXP=EXP+30
        #if user is level 2 and gains 30 experience points user rises to level 3 and continues through the dungeon
      if LVL==2 and EXP>=30:
        LVL=LVL+1
        print("Level Up! You've grown to Level 3!")
        MaxHP=MaxHP+HPRaise
        MaxMana=MaxMana+ManaRaise
        PATK=PATK+ATKRaise
        PDEF=PDEF+DEFRaise
        PHP=MaxHP
        Mana=MaxMana
        print("You continue on as the path curves and meets with 5 other pathways. You wonder if these are connected to the paths from the beginning of the dungeon.")
   Reunited=1
 else:
   print("You find nothing and continue on as the path curves and meets with 5 other pathways. You wonder if these are connected to the paths from the beginning of the dungeon.")
   Reunited=1

if Dead!=1 and Fork1==2:

#user continues through dungeon and can pick to go Left, or Right
 Fork22=int(input("You continue on in the dungeon and find a second fork. There are 2 paths. Choose 1 for Left and 2 for Right: "))

 # if you pick the option to open it then you get a Magic Heart that gives the user 5 extra health points if not then nothing happens and you continue through the dungeon
 if Fork22==1:

  chest22=int(input("You found a treasure chest! Open it? Enter 1 for Yes and anything else for No: "))

  if chest22==1:

   print("You got a Magic Heart! HP increased by 5!")
   MaxHP=MaxHP+5
   PHP=MaxHP
   print("You continue on as the path curves and meets with 5 other pathways. You wonder if these are connected to the paths from the beginning of the dungeon.")
   Reunited=1

#user didn't open the chest and continues through the dungeon
  else:
    print("You didn't open the chest!")
    print("You continue on as the path curves and meets with 5 other pathways. You wonder if these are connected to the paths from the beginning of the dungeon.")
    Reunited=1
 else: 
   print("You find nothing and continue on as the path curves and meets with 5 other pathways. You wonder if these are connected to the paths from the beginning of the dungeon.")
   Reunited=1

#all comments from the previous lines repeats to line 511
if Fork1==3 and Dead!=1:
  print("\nYou continue on and find a Werewolf!\n Engage Battle!\n\n")

  EHP=15
  EATK=5
  EDEF=3

  while EHP>0 and PHP>0 and Heal==1:
    print(Name, "HP: " , PHP)
    print(Name, "Mana: " , Mana)
    print("Enemy HP: " , EHP)
    AC=int(input("Choose your move: \n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Heal Spell: 4 Mana\n4 - Flee."))

    if AC!=1 and AC!=2 and AC!=3 and AC!=4:
      AC=1

    if AC==2 and Mana<2:
      AC=1

    if AC==1:
      Mana=Mana+1
      if Mana>MaxMana:
        Mana=MaxMana
      DMG=PATK-EDEF
      if DMG<1:
        DMG=1


    if AC==2:
      Mana=Mana-2
      DMG=PATK*2-EDEF
      if DMG<1:
        DMG=1

    if AC==3:
      Mana=Mana-4
      PHP=PHP+10
      if PHP>MaxHP:
        PHP=MaxHP

    if AC==4:
      print("Cannot Flee!")

    if AC==1 or AC==2:
      EHP=EHP-DMG
      print(Name, "attacked!",DMG, "damage dealt!")

    if AC==3:
      print(Name, "cast Heal Spell! 10 HP Recovered.")

    if EHP>0:
      DMG=EATK-PDEF
      if DMG<1:
        DMG=1
      PHP=PHP-DMG
      print("Enemy Attacked! " , Name , "Took " , DMG , " Damage!\n")

    if PHP<1:
      print("You have died!")
      Dead=1

    if EHP<1:
      print("You have defeated the Werewolf! You have gained 10 EXP!")
      EXP=EXP+10
    if LVL==1 and EXP>=10:
      LVL=LVL+1
      print("Level Up! You've grown to Level 2!")
      MaxHP=MaxHP+HPRaise
      MaxMana=MaxMana+ManaRaise
      PATK=PATK+ATKRaise
      PDEF=PDEF+DEFRaise
      PHP=MaxHP
      Mana=MaxMana

      print("You continue on as the path curves and meets with 5 other pathways. You wonder if these are connected to the paths from the beginning of the dungeon.")
      Reunited=1

  while EHP>0 and PHP>0 and Heal==0:
      print(Name, "HP: " , PHP)
      print(Name, "Mana: " , Mana)
      print("Enemy HP: " , EHP)
      AC=int(input("Choose your move: \n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Flee"))

      if AC!=1 and AC!=2 and AC!=3:
        AC=1

      if AC==2 and Mana<2:
        AC=1

      if AC==1:
        Mana=Mana+1
        if Mana>MaxMana:
          Mana=MaxMana
        DMG=PATK-EDEF
        if DMG<1:
          DMG=1


      if AC==2:
        Mana=Mana-2
        DMG=PATK*2-EDEF
        if DMG<1:
          DMG=1

      if AC==3:
        print("Cannot Flee!")

      if AC==1 or AC==2:
        EHP=EHP-DMG
        print(Name, "attacked!",DMG, "damage dealt!")

      if EHP>0:
        DMG=EATK-PDEF
        if DMG<1:
          DMG=1
        PHP=PHP-DMG
        print("Enemy Attacked! " , Name , "Took " , DMG , " Damage!\n")

      if PHP<1:
        print("You have died!")
        Dead=1

      if EHP<1:
        print("You have defeated the Werewolf! You have gained 10 EXP!")
        EXP=EXP+10
      if LVL==1 and EXP>=10:
        LVL=LVL+1
        print("Level Up! You've grown to Level 2!\n\nYou've learned the Heal Spell!")
        MaxHP=MaxHP+HPRaise
        MaxMana=MaxMana+ManaRaise
        PATK=PATK+ATKRaise
        PDEF=PDEF+DEFRaise
        PHP=MaxHP
        Mana=MaxMana
  print("You continue on as the path curves and meets with 5 other pathways. You wonder if these are connected to the paths from the beginning of the dungeon.")
  Reunited=1

#the story line continues
if Reunited==1:
  print("\n\nYou walk more into the room you are in when suddenly a floating human figure appears in front of you. You can't tell the gender. They are glowing white and are slightly transparent. Is this person a spirit? Suddenly, it talks to you.")
  print("\n\n???: Human...")
  print("The voice is definitely female.\n\n" , Name , ": What? What do you want?")
  print("\n\n???: I have been watching you...do not talk. Just listen to me. There are 3 Treasure Chests in the next room. You can only open one before the other 2 get a magic lock on them. The left chest contains a magic battleaxe, much stronger than your average blade. The middle chest has magic body armor, capable of taking more hits than any soldier's armor. The third chest contains magic energy. This energy will give the person who opened the chest and touched the energy a rare ability. In short, it's a new spell. I do not know what the spell is, but apparently, it is very powerful. Choose wisely" , Name , "...")
  print("\n\nThe spirit dissappeared. Who is she?\n\n")
  conti=input("Press enter when you are ready to continue.")
  print("Just for reference, your stats are::\n\n")
  print("Level: " , LVL)
  print("EXP: " , EXP)
  print("HP: " , PHP , " / " , MaxHP)
  print("Mana: " , Mana , " / " , MaxMana)
  print("Attack: " , PATK)
  print("Defense: " , PDEF)

  MagiChest1=0

#3 magic chests appear to choose from
  while MagiChest1!=1 and MagiChest1!=2 and MagiChest1!=3:

    MagiChest1=int(input("You go into the next room and find three chests. Just like the spirit said. Time to choose. Enter 1 for the left chest, 2 for the middle chest, and 3 for the right chest:: "))
    if MagiChest1!=1 and MagiChest1!=2 and MagiChest1!=3:
      print("That's not an option!")

#gives user a Battleaxe and rises attack by 6 
if MagiChest1==1:
  print("You got the Magic Battleaxe! Your Attack has been raised by 6!")
  PATK=PATK+6
  MGCDN1=1

#gives user Magic Armor and rises defense by 6
if MagiChest1==2:
  print("You got the Magic Armor! Your Defense has been raised by 6!")
  PDEF=PDEF+6
  MGCDN1=1

#gives user a new Spell [Sacrificer]
if MagiChest1==3:
  print("The magic energy surrounds you. It fills you with DETERMINATION... just kidding. Anyway, you learned a new spell! Sacrificer!\n")
  SacrTrue=1
  MGCDN1=1

#if user picks magic chest 1 the user gets a monster encounter
if MGCDN1==1:
  print("A monster blocks the path into the next room. Engage battle!")

EHP=55
EATK=14
EDEF=7

while EHP>0 and PHP>0 and Heal==1 and SacrTrue:
    print(Name, "HP: " , PHP)
    print(Name, "Mana: " , Mana)
    print("Enemy HP: " , EHP)
    AC=int(input("Choose your move: \n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Heal Spell: 4 Mana\n4 - Sacrificer: 6 Mana & 1/3 of your current HP\n5 - Flee."))

    if AC!=1 and AC!=2 and AC!=3 and AC!=4 and AC!=5:
      AC=1

    if AC==2 and Mana<2:
      AC=1

    if AC==1:
      Mana=Mana+1
      if Mana>MaxMana:
        Mana=MaxMana
      DMG=PATK-EDEF
      if DMG<1:
        DMG=1


    if AC==2:
      Mana=Mana-2
      DMG=PATK*2-EDEF
      if DMG<1:
        DMG=1

    if AC==3:
      Mana=Mana-4
      PHP=PHP+10
      if PHP>MaxHP:
        PHP=MaxHP

    if AC==4:
      DMG=PATK*3-EDEF
      if DMG<1:
        DMG=1

    if AC==5:
      print("Cannot Flee!")

    if AC==1 or AC==2 or AC==4:
      EHP=EHP-DMG
      print(Name, "attacked!",DMG, "damage dealt!")
      if AC==4:

        print(Name , "took damage from Sacrificer!" , math.floor(3/2*PHP*1/3) , "damage taken!")
        PHP=math.ceil(2/3*PHP)

    if AC==3:
      print(Name, "cast Heal Spell! 10 HP Recovered.")

    if EHP>0:
      DMG=EATK-PDEF
      if DMG<1:
        DMG=1
      PHP=PHP-DMG
      print("Enemy Attacked! " , Name , "Took " , DMG , " Damage!\n")



    if PHP<1:
      print("You have died!")
      Dead=1

      #user beats monter and gains 50 exp
    if EHP<1:
      print("You have defeated the Monster! You have gained 50 EXP!")
      Monst1=1
      EXP=EXP+50
    if LVL==2 and EXP>=30:
      LVL=LVL+1
      print("\n\nYou've leveled up! You are now Level 3!")
      MaxHP=MaxHP+HPRaise
      PHP=MaxHP
      MaxMana=MaxMana+ManaRaise
      Mana=MaxMana
      PATK=PATK+ATKRaise
      PDEF=PDEF+DEFRaise
    if LVL==3 and EXP>=60:
      LVL=LVL+1
      print("\n\nYou've leveled up! You are now Level 4!")
      MaxHP=MaxHP+HPRaise
      PHP=MaxHP
      MaxMana=MaxMana+ManaRaise
      Mana=MaxMana
      PATK=PATK+ATKRaise
      PDEF=PDEF+DEFRaise
    if LVL==4 and EXP>=100:
      LVL=LVL+1
      print("\n\nYou've leveled up! You are now Level 5!")
      MaxHP=MaxHP+HPRaise
      PHP=MaxHP
      MaxMana=MaxMana+ManaRaise
      Mana=MaxMana
      PATK=PATK+ATKRaise
      PDEF=PDEF+DEFRaise

while EHP>0 and PHP>0 and Heal==1 and SacrTrue==0:
    print(Name, "HP: " , PHP)
    print(Name, "Mana: " , Mana)
    print("Enemy HP: " , EHP)
    AC=int(input("Choose your move: \n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Heal Spell: 4 Mana\n4 - Flee."))

    if AC!=1 and AC!=2 and AC!=3 and AC!=4:
      AC=1

    if AC==2 and Mana<2:
      AC=1

    if AC==1:
      Mana=Mana+1
      if Mana>MaxMana:
        Mana=MaxMana
      DMG=PATK-EDEF
      if DMG<1:
        DMG=1


    if AC==2:
      Mana=Mana-2
      DMG=PATK*2-EDEF
      if DMG<1:
        DMG=1

    if AC==3:
      Mana=Mana-4
      PHP=PHP+10
      if PHP>MaxHP:
        PHP=MaxHP

    if AC==4:
      print("Cannot Flee!")

    if AC==1 or AC==2:
      EHP=EHP-DMG
      print(Name, "attacked!",DMG, "damage dealt!")

    if AC==3:
      print(Name, "cast Heal Spell! 10 HP Recovered.")

    if EHP>0:
      DMG=EATK-PDEF
      if DMG<1:
        DMG=1
      PHP=PHP-DMG
      print("Enemy Attacked! " , Name , "Took " , DMG , " Damage!\n")

    if PHP<1:
      print("You have died!")
      Dead=1

      #user defeats monster and gains 50 exp
    if EHP<1:
      Monst1=1
      print("You have defeated the Monster! You have gained 50 EXP!")
      EXP=EXP+50
    if LVL==2 and EXP>=30:
      LVL=LVL+1
      print("\n\nYou've leveled up! You are now Level 3!")
      MaxHP=MaxHP+HPRaise
      PHP=MaxHP
      MaxMana=MaxMana+ManaRaise
      Mana=MaxMana
      PATK=PATK+ATKRaise
      PDEF=PDEF+DEFRaise
    if LVL==3 and EXP>=60:
      LVL=LVL+1
      print("\n\nYou've leveled up! You are now Level 4!")
      MaxHP=MaxHP+HPRaise
      PHP=MaxHP
      MaxMana=MaxMana+ManaRaise
      Mana=MaxMana
      PATK=PATK+ATKRaise
      PDEF=PDEF+DEFRaise

    if LVL==4 and EXP>=100:
      LVL=LVL+1
      print("\n\nYou've leveled up! You are now Level 5!")
      MaxHP=MaxHP+HPRaise
      PHP=MaxHP
      MaxMana=MaxMana+ManaRaise
      Mana=MaxMana
      PATK=PATK+ATKRaise
      PDEF=PDEF+DEFRaise

#continues the story line
if Monst1==1:
  print("\n\nYou continue on into the next room.")
  print("\n\nThe spirit appears again.\n\n" , Name , ": What do you want?\n???: I don't want anything. I'm simply a spirit guide. I guide those who I sense have a pure heart. Anyway, the next room has 3 chests as well, but they are very different this time. 2 of them will curse you. However, the third... will give you a blessing. If you don't want to take the risk, you can skip the chests all together. Also, there's an ogre you will have to face to leave the room. That battle isn't easy for most people. Choose wisely," , Name , "...")
  conti=input("\n\nPress enter to continue.")
  print("\n\nThe spirit vanished again. Who the heck is she and why is she helping me? Also, her figure was clearer this time. The light no longer blocked her shape. It's clear she's a female; It's not just her voice. Why did her appearance change? What's going on?\n\n")
  conti=input("\n\nPress enter to continue.")
  print("\n\nYou reach the room with the three chests. Time to Choose!\n")

  MagiChest2=0

#lets user pick a chest or skip the chests
  while MagiChest2!=1 and MagiChest2!=2 and MagiChest2!=3 and MagiChest2!=4:
    MagiChest2=int(input("Choose 1 for the left chest, 2 for the middle chest, 3 for the right chest, and 4 to skip the chests."))
    if MagiChest2!=1 and MagiChest2!=2 and MagiChest2!=3 and MagiChest2!=4:
      print("That's not an option!")

  #gives user 50 exp
if MagiChest2==1 and MagiChest1==3:
  print("You feel some energy surround you...once again you are filled with DETERMINATION...just kidding...again. You've gained 50 EXP!")

#gives user 50 exp
if MagiChest2==1 and MagiChest1!=3:
  print("You feel some energy surround you. It fills you with DETERMINATION...just kidding. You've gained 50 EXP!")

#stats get upgraded
if MagiChest2==1:
  EXP=EXP+60
  if LVL==4 and EXP>=100:
   LVL=LVL+1
   print("You've leveled up! You are now Level 5!")
   MaxHP=MaxHP+HPRaise
   PHP=MaxHP
   MaxMana=MaxMana+ManaRaise
   Mana=MaxMana
   PATK=PATK+ATKRaise
   PDEF=PDEF+DEFRaise
  if LVL==5 and EXP>=150:
    LVL=LVL+1
    print("You've leveled up! You are now Level 6!")
    MaxHP=MaxHP+HPRaise
    PHP=MaxHP
    MaxMana=MaxMana+ManaRaise
    Mana=MaxMana
    PATK=PATK+ATKRaise
    PDEF=PDEF+DEFRaise
    print("\n\nHeal has been enhanced!!")
    Heal=2

#curses user by lowering user's stats
if MagiChest2==2:
  print("You feel cursed...you feel some of your strength leave your body. Your Attack and Defense were lowered!")
  PATK=PATK-1
  PDEF=PDEF-1

#curses user by lowering user's stats
if MagiChest2==3:
  print("You feel cursed...you feel some of your strength leave your body. Your Attack and Defense were lowered!")
  PATK=PATK-1
  PDEF=PDEF-1

#user skips chests
if MagiChest2==4:
  print("\n\nYou decided to skip the chests!")

#lets user encounter an Ogre
if MagiChest2!=0:
  print("The Ogre has appeared! Engage Battle!")





  EHP=70
  EATK=25
  EDEF=15

  while EHP>0 and PHP>0 and Heal==2 and SacrTrue==1:

    print(Name , "HP:" , PHP)
    print(Name , "Mana:" , Mana)
    print("\nEnemy HP: " , EHP)
    AC=int(input("\n\n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Mega Heal: 5 Mana\n4 - Sacrificer: 6 Mana and 1/3 of your current HP\nChoose your move:"))

    if AC!=1 and AC!=2 and AC!=3 and AC!=4:
      AC=1

    if AC==2 and Mana<2:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==3 and Mana<5:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==4 and Mana<6 or AC==4 and PHP<3:
      AC=1
      if Mana<6:
        print("You don't have enough Mana for that! You do a Normal Attack instead!")
      if PHP<3:
        print("You don't have enough HP for that! You do a Normal Attack instead!")

    if AC==1:
      Mana=Mana+1
      DMG=PATK-EDEF
      if DMG<1:
        DMG=1

    if AC==2:
      Mana=Mana-2
      DMG=PATK*2-EDEF
      if DMG<1:
        DMG=1

    if AC==3:
      Mana=Mana-5
      PHP=PHP+math.ceil(MaxHP/2)
      if PHP>MaxHP:
        PHP=MaxHP

    if AC==4:
      DMG=PATK*3-EDEF
      Mana=Mana-6
      PHP=math.ceil(2/3*PHP)

    if AC==1 or AC==2 or AC==4:
      EHP=EHP-DMG
      print("\n" , Name , "attacked!" , DMG , "damage dealt!")

      if AC==4:

        print(Name , "took damage from Sacrificer!" , math.floor(3/2*PHP*1/3) , "damage taken!")

    if AC==3:
      print("\n" , Name , "cast Mega Heal!" , math.ceil(MaxHP/2) , "HP Recovered!")

    if EHP>0: 
      DMG=EATK-PDEF
      PHP=PHP-DMG
      if DMG<1:
        DMG=1
      print("Enemy attacked!" , DMG , "damage taken!")

    #user beats Ogre and gains 60 exp, user also levels up
    if EHP<1:
      print("The Ogre has been defeated! You gained 60 EXP!")
      EXP=EXP+60
      if LVL==4 and EXP>100:
        LVL=LVL+1
        print("Level Up! You've grown to Level 5!\n\n")
        MaxHP=MaxHP+HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+ManaRaise
        Mana=MaxMana
        PATK=PATK+ATKRaise
        PDEF=PDEF+DEFRaise
      if LVL==5 and EXP>=150:
        LVL=LVL+1
        print("Level Up! You've grown to Level 6!\n\nHeal has been Enhanced!")
        Heal==2
        MaxHP=MaxHP+HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+ManaRaise
        Mana=MaxMana
        PATK=PATK+ATKRaise
        PDEF=PDEF+DEFRaise
      if LVL==6 and EXP>=210:
        LVL=LVL+1
        print("Level Up! You've grown to Level 7!")
        MaxHP=MaxHP+2*HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+2*ManaRaise
        Mana=MaxMana
        PATK=PATK+2*ATKRaise
        PDEF=PDEF+2*DEFRaise
        print("\n\n\nYou've reached Max Level! Congratulations!")

    if PHP<1:
      print("You have died!")
      Dead=1



#all comments are reletivly the same from this line all the way to line 1322
  while EHP>0 and PHP>0 and Heal==1 and SacrTrue==1:

    print(Name , "HP:" , PHP)
    print(Name , "Mana:" , Mana)
    print("\nEnemy HP: " , EHP)
    AC=int(input("\n\n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Heal: 4 Mana\n4 - Sacrificer: 6 Mana and 1/3 of your current HP\nChoose your move:"))

    if AC!=1 and AC!=2 and AC!=3 and AC!=4:
      AC=1

    if AC==2 and Mana<2:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==3 and Mana<4:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==4 and Mana<6 or AC==4 and PHP<3:
      AC=1
      if Mana<6:
        print("You don't have enough Mana for that! You do a Normal Attack instead!")
      if PHP<3:
        print("You don't have enough HP for that! You do a Normal Attack instead!")

    if AC==1:
      Mana=Mana+1
      DMG=PATK-EDEF
      if DMG<1:
        DMG=1

    if AC==2:
      Mana=Mana-2
      DMG=PATK*2-EDEF
      if DMG<1:
        DMG=1

    if AC==3:
      Mana=Mana-5
      PHP=PHP+10
      if PHP>MaxHP:
        PHP=MaxHP

    if AC==4:
      DMG=PATK*3-EDEF
      Mana=Mana-6
      PHP=math.ceil(2/3*PHP)

    if AC==1 or AC==2 or AC==4:
      EHP=EHP-DMG
      print("\n" , Name , "attacked!" , DMG , "damage dealt!")

      if AC==4:

        print(Name , "took damage from Sacrificer!" , math.floor(3/2*PHP*1/3) , "damage taken!")

    if AC==3:
      print("\n" , Name , "cast Heal! 10 HP Recovered!")

    if EHP>0: 
      DMG=EATK-PDEF
      PHP=PHP-DMG
      if DMG<1:
        DMG=1
      print("Enemy attacked!" , DMG , "damage taken!")

    if EHP<1:
      print("The Ogre has been defeated! You gained 60 EXP!")
      EXP=EXP+60
      if LVL==4 and EXP>=100:
        LVL=LVL+1
        print("Level Up! You've grown to Level 5!\n\n")
        MaxHP=MaxHP+HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+ManaRaise
        Mana=MaxMana
        PATK=PATK+ATKRaise
        PDEF=PDEF+DEFRaise
      if LVL==5 and EXP>=150:
        LVL=LVL+1
        print("Level Up! You've grown to Level 6!\n\nHeal has been Enhanced!")
        Heal==2
        MaxHP=MaxHP+HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+ManaRaise
        Mana=MaxMana
        PATK=PATK+ATKRaise
        PDEF=PDEF+DEFRaise
      if LVL==6 and EXP>=210:
        LVL=LVL+1
        print("Level Up! You've grown to Level 7!")
        MaxHP=MaxHP+2*HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+2*ManaRaise
        Mana=MaxMana
        PATK=PATK+2*ATKRaise
        PDEF=PDEF+2*DEFRaise
        print("\n\n\nYou've reached Max Level! Congratulations!")

    if PHP<1:
      print("You have died!")
      Dead=1



  while EHP>0 and PHP>0 and Heal==5 and SacrTrue==1:

    print(Name , "HP:" , PHP)
    print(Name , "Mana:" , Mana)
    print("\nEnemy HP: " , EHP)
    AC=int(input("\n\n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Heal: 4 Mana\n4 - Sacrificer: 6 Mana and 1/3 of your current HP\nChoose your move:"))

    if AC!=1 and AC!=2 and AC!=3 and AC!=4:
      AC=1

    if AC==2 and Mana<2:
        AC=1
        print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==3 and Mana<5:
        AC=1
        print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==4 and Mana<6 or AC==4 and PHP<3:
        AC=1
        if Mana<6:
          print("You don't have enough Mana for that! You do a Normal Attack instead!")
        if PHP<3:
          print("You don't have enough HP for that! You do a Normal Attack instead!")

    if AC==1:
        Mana=Mana+1
        DMG=PATK-EDEF
        if DMG<1:
          DMG=1

    if AC==2:
        Mana=Mana-2
        DMG=PATK*2-EDEF
        if DMG<1:
          DMG=1

    if AC==3:
        Mana=Mana-5
        PHP=PHP+10
        if PHP>MaxHP:
          PHP=MaxHP

    if AC==4:
        DMG=PATK*3-EDEF
        Mana=Mana-6
        PHP=math.ceil(2/3*PHP)

    if AC==1 or AC==2 or AC==4:
      EHP=EHP-DMG
      print("\n" , Name , "attacked!" , DMG , "damage dealt!")

      if AC==4:
        print(Name , "took damage from Sacrificer!" , math.floor(3/2*PHP*1/3) , "damage taken!")

    if AC==3:
      print("\n" , Name , "cast Heal! 10 HP Recovered!")
    if EHP>0: 
      DMG=EATK-PDEF
      PHP=PHP-DMG
      if DMG<1:
        DMG=1
      print("Enemy attacked!" , DMG , "damage taken!")

    if EHP<1:
      print("The Ogre has been defeated! You gained 60 EXP!")
      EXP=EXP+60
      if LVL==4 and EXP>=100:
        LVL=LVL+1
        print("Level Up! You've grown to Level 5!\n\n")
        MaxHP=MaxHP+HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+ManaRaise
        Mana=MaxMana
        PATK=PATK+ATKRaise
        PDEF=PDEF+DEFRaise
      if LVL==5 and EXP>=150:
        LVL=LVL+1
        print("Level Up! You've grown to Level 6!\n\nHeal has been Enhanced!")
        Heal==2
        MaxHP=MaxHP+HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+ManaRaise
        Mana=MaxMana
        PATK=PATK+ATKRaise
        PDEF=PDEF+DEFRaise
      if LVL==6 and EXP>=210:
        LVL=LVL+1
        print("Level Up! You've grown to Level 7!")
        MaxHP=MaxHP+2*HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+2*ManaRaise
        Mana=MaxMana
        PATK=PATK+2*ATKRaise
        PDEF=PDEF+2*DEFRaise
        print("\n\n\nYou've reached Max Level! Congratulations!")

    if PHP<1:
      print("You have died!")
      Dead=1



  while EHP>0 and PHP>0 and Heal==2 and SacrTrue==0:

    print(Name , "HP:" , PHP)
    print(Name , "Mana:" , Mana)
    print("\nEnemy HP: " , EHP)
    AC=int(input("\n\n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Mega Heal: 5 Mana\n\nChoose your move:"))

    if AC!=1 and AC!=2 and AC!=3:
      AC=1

    if AC==2 and Mana<2:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==3 and Mana<5:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==4 and Mana<4:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==1:
      Mana+1
      DMG=PATK-EDEF
      if DMG<1:
        DMG=1

    if AC==2:
      Mana=Mana-2
      DMG=PATK*2-EDEF
      if DMG<1:
        DMG=1

    if AC==3:
      Mana=Mana-5
      PHP=PHP+10
      if PHP>MaxHP:
        PHP=MaxHP

    if AC==1 or AC==2:
      EHP=EHP-DMG
      print("\n" , Name , "attacked!" , DMG , "damage dealt!")

    if AC==3:
      print("\n" , Name , "cast Mega Heal!" , math.ceil(MaxHP/2) , "HP Recovered!")

    if EHP>0: 
      DMG=EATK-PDEF
      if DMG<1:
        DMG=1
      PHP=PHP-DMG

      print("Enemy Attacked!" , DMG , " damage dealt!")


    if EHP<1:
      print("The Ogre has been defeated! You gained 60 EXP!")
      EXP=EXP+60
      if LVL==4 and EXP>=100:
        LVL=LVL+1
        print("Level Up! You've grown to Level 5!\n\n")
        MaxHP=MaxHP+HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+ManaRaise
        Mana=MaxMana
        PATK=PATK+ATKRaise
        PDEF=PDEF+DEFRaise
      if LVL==5 and EXP>=150:
        LVL=LVL+1
        print("Level Up! You've grown to Level 6!\n\nHeal has been Enhanced!")
        Heal==2
        MaxHP=MaxHP+HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+ManaRaise
        Mana=MaxMana
        PATK=PATK+ATKRaise
        PDEF=PDEF+DEFRaise
      if LVL==6 and EXP>=210:
        LVL=LVL+1
        print("Level Up! You've grown to Level 7!")
        MaxHP=MaxHP+2*HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+2*ManaRaise
        Mana=MaxMana
        PATK=PATK+2*ATKRaise
        PDEF=PDEF+2*DEFRaise
        print("\n\n\nYou've reached Max Level! Congratulations!")

    if PHP<1:
      print("You have died!")
      Dead=1




  while EHP>0 and PHP>0 and Heal==1 and SacrTrue==0:

    print(Name , "HP:" , PHP)
    print(Name , "Mana:" , Mana)
    print("\nEnemy HP: " , EHP)
    AC=int(input("\n\n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Heal: 4 Mana\n\nChoose your move:"))

    if AC!=1 and AC!=2 and AC!=3:
      AC=1

    if AC==2 and Mana<2:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==3 and Mana<4:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")
    if AC==1:
      Mana=Mana+1
      DMG=PATK-EDEF
      if DMG<1:
        DMG=1

    if AC==2:
      Mana=Mana-2
      DMG=PATK*2-EDEF
      if DMG<1:
        DMG=1

    if AC==3:
      Mana=Mana-5
      PHP=PHP+10
      if PHP>MaxHP:
        PHP=MaxHP

    if AC==1 or AC==2:
      EHP=EHP-DMG
      print("\n" , Name , "attacked!" , DMG , "damage dealt!")

    if AC==3:
      print("\n" , Name , "cast Heal! 10 HP Recovered!")

    if EHP>0: 
      DMG=EATK-PDEF
      PHP=PHP-DMG
      if DMG<1:
        DMG=1


    if EHP<1:
      print("The Ogre has been defeated! You gained 60 EXP!")
      EXP=EXP+60
      if LVL==4 and EXP>=100:
        LVL=LVL+1
        print("Level Up! You've grown to Level 5!\n\n")
        MaxHP=MaxHP+HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+ManaRaise
        Mana=MaxMana
        PATK=PATK+ATKRaise
        PDEF=PDEF+DEFRaise
      if LVL==5 and EXP>=150:
        LVL=LVL+1
        print("Level Up! You've grown to Level 6!\n\nHeal has been Enhanced!")
        Heal==2
        MaxHP=MaxHP+HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+ManaRaise
        Mana=MaxMana
        PATK=PATK+ATKRaise
        PDEF=PDEF+DEFRaise
      if LVL==6 and EXP>=210:
        LVL=LVL+1
        print("Level Up! You've grown to Level 7!")
        MaxHP=MaxHP+2*HPRaise
        PHP=MaxHP
        MaxMana=MaxMana+2*ManaRaise
        Mana=MaxMana
        PATK=PATK+2*ATKRaise
        PDEF=PDEF+2*DEFRaise
        print("\n\n\nYou've reached Max Level! Congratulations!")

    if PHP<1:
      print("You have died!")
      Dead=1

      #if user is lvl 4 or lvl 7 (max level) encounter final boss
if LVL>=4 and LVL!=7:
  FinalBoss=1

#if user is level 7 (max level) the user will gain the choice to fight the default fake boss or the real final boss
if LVL==7:
  FinalBoss=int(input("Now, player, I doubt this is your first run of this game. If it is your first run, then I congratulate you. You chose the right paths, chose the right chest in the second room, and defeated all the enemies thrown your way. Now, I must ask you a question. Do you want to go with the fake final boss, which is the default one you face if you are not at max level, or do you want to face the real final boss, which will really put you to the test? Enter 1 for Fake...Enter 2 for Real...make your choice, Player: "))
  if FinalBoss==0:
    FinalBoss=3

#lets user encounter the final [true] boss
if FinalBoss==0:
  print("")

if FinalBoss!=0:
  almostthere=input("\n\n\n\n\nYou continue walking and sense a presence... a dangerous one. You can tell some sort of creature is up ahead...")
  almostthere=input("\n\nYou walk into the room...")
  if FinalBoss==2:
    print("There's a demon staring right at you. It growls and charges at you. Engage Battle!")
    EHP=200
    EATK=28
    EDEF=23
    FB=1

#lets user enounter final [default] boss
if FinalBoss==1:
    print("There's a dragon staring at you. It roars and flies towards you. Engage Battle!")
    EHP=150
    EATK=24
    EDEF=18
    FB=1

#lets user encounter the [secret] final boss
if FinalBoss!=1 and FinalBoss!=2 and FinalBoss!=0:
  print("There's some distorted figure... some strange black fog is covering it. You can't tell what it is... somehow you can tell it's staring at you. Engage Battle!")
  FB=1

  EHP=500
  EATK=50
  EDEF=50


#final boss stats during it's fight
if FB==1:

  while EHP>0 and PHP>0 and Heal==2 and SacrTrue==0:

    print(Name , "HP:" , PHP)
    print(Name , "Mana:" , Mana)
    print("\nEnemy HP: " , EHP)
    AC=int(input("\n\n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Mega Heal: 5 Mana\n\nChoose your move:"))

    if AC!=1 and AC!=2 and AC!=3:
      AC=1

    if AC==2 and Mana<2:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==3 and Mana<5:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==4 and Mana<4:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==1:
      Mana=Mana+1
      DMG=PATK-EDEF
      if DMG<1:
        DMG=1

    if AC==2:
      Mana=Mana-2
      DMG=PATK*2-EDEF
      if DMG<1:
        DMG=1

    if AC==3:
      Mana=Mana-5
      PHP=PHP+10
      if PHP>MaxHP:
        PHP=MaxHP

    if AC==1 or AC==2:
      EHP=EHP-DMG
      print("\n" , Name , "attacked!" , DMG , "damage dealt!")

    if AC==3:
      print("\n" , Name , "cast Mega Heal!" , math.ceil(MaxHP/2) , "HP Recovered!")

    if EHP>0: 
      DMG=EATK-PDEF
      if DMG<1:
        DMG=1
      PHP=PHP-DMG
      print("Enemy Attacked!" , DMG , " damage taken!")

    #user beat the final boss
    if EHP<1:
      print("You did it! The treasure is right there! You made it through the dungeon and you've won the game!! Congratulations!!")
      Complete=1

#user died to the final boss
    if PHP<1:
      print("You died! It's such a shame! This was the last battle, too... Better Luck Next Time!")

#[True] final boss stats during it's fight
  while EHP>0 and PHP>0 and Heal==2 and SacrTrue==1:

    print(Name , "HP:" , PHP)
    print(Name , "Mana:" , Mana)
    print("\nEnemy HP: " , EHP)
    AC=int(input("\n\n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Mega Heal: 5 Mana\n4 - Sacrificer: 6 Mana and 1/3 of your current HP\nChoose your move:"))

    if AC!=1 and AC!=2 and AC!=3 and AC!=4:
      AC=1

    if AC==2 and Mana<2:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==3 and Mana<5:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==4 and Mana<6 or AC==4 and PHP<3:
      AC=1
      if Mana<6:
        print("You don't have enough Mana for that! You do a Normal Attack instead!")
      if PHP<3:
        print("You don't have enough HP for that! You do a Normal Attack instead!")

    if AC==1:
      Mana=Mana+1
      DMG=PATK-EDEF
      if DMG<1:
        DMG=1

    if AC==2:
      Mana=Mana-2
      DMG=PATK*2-EDEF
      if DMG<1:
        DMG=1

    if AC==3:
      Mana=Mana-5
      PHP=PHP+math.ceil(MaxHP/2)
      if PHP>MaxHP:
        PHP=MaxHP

    if AC==4:
      DMG=PATK*3-EDEF
      Mana=Mana-6
      PHP=math.ceil(2/3*PHP)

    if AC==1 or AC==2 or AC==4:
      EHP=EHP-DMG
      print("\n" , Name , "attacked!" , DMG , "damage dealt!")

      if AC==4:

        print(Name , "took damage from Sacrificer!" , math.floor(3/2*PHP*1/3) , "damage taken!")

    if AC==3:
      print("\n" , Name , "cast Mega Heal!" , math.ceil(MaxHP/2) , "HP Recovered!")

    if EHP>0: 
      DMG=EATK-PDEF
      if DMG<1:
        DMG=1
      PHP=PHP-DMG
      print("Enemy attacked!" , DMG , "damage taken!")


    if EHP<1:
      print("You did it! The treasure is right there! You made it through the dungeon and you've won the game!! Congratulations!!")
      Complete=1

    if PHP<1:
      print("You died! It's such a shame! This was the last battle, too... Better Luck Next Time!")  

  while EHP>0 and PHP>0 and Heal==1 and SacrTrue==1:

    print(Name , "HP:" , PHP)
    print(Name , "Mana:" , Mana)
    print("\nEnemy HP: " , EHP)
    AC=int(input("\n\n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Heal: 4 Mana\n4 - Sacrificer: 6 Mana and 1/3 of your current HP\nChoose your move:"))

    if AC!=1 and AC!=2 and AC!=3 and AC!=4:
      AC=1

    if AC==2 and Mana<2:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==3 and Mana<5:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==4 and Mana<6 or AC==4 and PHP<3:
      AC=1
      if Mana<6:
        print("You don't have enough Mana for that! You do a Normal Attack instead!")
      if PHP<3:
        print("You don't have enough HP for that! You do a Normal Attack instead!")

    if AC==1:
      Mana=Mana+1
      DMG=PATK-EDEF
      if DMG<1:
        DMG=1

    if AC==2:
      Mana=Mana-2
      DMG=PATK*2-EDEF
      if DMG<1:
        DMG=1

    if AC==3:
      Mana=Mana-4
      PHP=PHP+10
      if PHP>MaxHP:
        PHP=MaxHP

    if AC==4:
      DMG=PATK*3-EDEF
      Mana=Mana-6
      PHP=math.ceil(2/3*PHP)

    if AC==1 or AC==2 or AC==4:
      EHP=EHP-DMG
      print("\n" , Name , "attacked!" , DMG , "damage dealt!")

      if AC==4:

        print(Name , "took damage from Sacrificer!" , math.floor(3/2*PHP*1/3) , "damage taken!")

    if AC==3:
      print("\n" , Name , "cast Heal! 10 HP Recovered!")

    if EHP>0: 
      DMG=EATK-PDEF
      if DMG<1:
        DMG=1
      PHP=PHP-DMG
      print("Enemy attacked!" , DMG , "damage taken!")


    if EHP<1:
      print("You did it! The treasure is right there! You made it through the dungeon and you've won the game!! Congratulations!!")
      Complete=1

    if PHP<1:
      print("You died! It's such a shame! This was the last battle, too... Better Luck Next Time!") 

  #[secret] final boss stats during it's fight
  while EHP>0 and PHP>0 and Heal==1 and SacrTrue==0:

    print(Name , "HP:" , PHP)
    print(Name , "Mana:" , Mana)
    print("\nEnemy HP: " , EHP)
    AC=int(input("\n\n1 - Attack\n2 - Fire Spell: 2 Mana\n3 - Heal: 4 Mana\n\nChoose your move:"))

    if AC!=1 and AC!=2 and AC!=3:
      AC=1

    if AC==2 and Mana<2:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==3 and Mana<5:
      AC=1
      print("You don't have enough Mana for that! You do a Normal Attack instead!")

    if AC==4 and Mana<6 or AC==4 and PHP<3:
      AC=1
      if Mana<6:
        print("You don't have enough Mana for that! You do a Normal Attack instead!")
      if PHP<3:
        print("You don't have enough HP for that! You do a Normal Attack instead!")

    if AC==1:
      Mana=Mana+1
      DMG=PATK-EDEF
      if DMG<1:
        DMG=1

    if AC==2:
      Mana=Mana-2
      DMG=PATK*2-EDEF
      if DMG<1:
        DMG=1

    if AC==3:
      Mana=Mana-5
      PHP=PHP+10
      if PHP>MaxHP:
        PHP=MaxHP

    if AC==4:
      DMG=PATK*3-EDEF
      Mana=Mana-6
      PHP=math.ceil(2/3*PHP)

    if AC==1 or AC==2 or AC==4:
      EHP=EHP-DMG
      print("\n" , Name , "attacked!" , DMG , "damage dealt!")

      if AC==4:

        print(Name , "took damage from Sacrificer!" , math.floor(3/2*PHP*1/3) , "damage taken!")

    if AC==3:
      print("\n" , Name , "cast Heal! 10 HP Recovered!")

    if EHP>0: 
      DMG=EATK-PDEF
      if DMG<1:
        DMG=1
      PHP=PHP-DMG
      print("Enemy attacked!" , DMG , "damage taken!")


    if EHP<1:
      print("You did it! The treasure is right there! You made it through the dungeon and you've won the game!! Congratulations!!")
      Complete=1

    if PHP<1:
      print("You died! It's such a shame! This was the last battle, too... Better Luck Next Time!") 

    #ending for the final boss fight
if Complete==1 and LVL!=7:
  print("\n\nHowever...you didn't reach the full potential you could have reached...try playing through again. Maybe you'll do better.")

#ending for the [True] final boss fight
if Complete==1 and LVL==7 and FinalBoss==2:
  print("\n\nYou are incredible. You reached Max Level and beat the True Final Boss. There is no way to be better at this game. Thank you for playing. Thank you.")

#ending if you didn't fight the [True] final boss
if Complete==1 and LVL==7 and FinalBoss==1:
  print("\n\nWhat's wrong? You reached Max Level, a good feat in itself, but why didn't you face the True Final Boss? Scared, perhaps? Maybe there was another reason...maybe you were just curious. Anyway, thank you for playing. I appreciate it. Try beating the True Final Boss now!")

#ending for the [secret] final boss
if Complete==1 and FinalBoss!=0 and FinalBoss!=1 and FinalBoss!=2:
  print("You entered a secret Class number, didn't you? That's the only way you could have beaten this.")
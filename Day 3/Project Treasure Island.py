print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island\nyour mission is to find the tressure")
move1 = input ("You're at a cross road. Where Do you wanna go? Type 'left' or 'right'   \n").lower()
if move1=="left":
    move2=input("You cam to a Lake.There is an island in the middle ofthe lake.Type 'wait' to wait for a boat.Type 'swim' to swim across you. \n").lower()
    if move2=="wait":
        move3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.Which colour do you choose? \n ").lower()
        if move3=='blue':
            print("game over")
        elif move3=='red':
            print("game over")
        elif move3=='yellow':
            print("You win!!! You got the treasure")
        else:
            print("you chose a door that doesn't exist")
    else:
        print("game over!!")
else:
    print('game over')    
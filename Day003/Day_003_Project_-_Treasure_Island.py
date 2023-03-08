# Indentation is VERY IMPORTANT
# Use three single apostrophe (''') to print multiple lines

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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome To Treasure Island.")
print("Your mission is to find the treasure")

choice1 = input('You\'re at the crossroad. Where do you want to go? Type "left" or "right"').lower()

if choice1 == 'left':
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or type "swim" to swim across').lower()
    if choice2 == 'wait':
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?').lower()
        if choice3 == 'red':
            print("It is a room of fire. You burn to death. Game Over")
        elif choice3 == 'yellow':
            print("You found the treasure! You Win!")
        elif choice3 == 'blue':
            print("There was a monster there. He ate")
        else:
            print("You fell out of the world. Game Over")
    else:
        print("You got attacked by a shark. Game Over")
else:
    print("YOu have fallen into a hole. Game Over")
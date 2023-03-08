import random

rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_
'''

paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|       
'''

scissors = '''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ 
|___/\___|_|___/___/\___/|_|  |___/
'''

options = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid choice")
else:
    print(f"You chose\n {options[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"The computer chose\n {options[computer_choice]}")

    # Recall that the if/else statement works sequentially and checks all of them from top to bottom
    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose :(")
    elif computer_choice > user_choice:
        print("You Lose :(")
    elif computer_choice == user_choice:
        print("It is a draw")

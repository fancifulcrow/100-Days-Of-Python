import random

EASY_LEVEL = 10
HARD_LEVEL = 5
logo = '''
  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ 
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                              
'''


def game():
    def set_difficulty():
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
        if difficulty == "easy":
            return EASY_LEVEL
        elif difficulty == "hard":
            return HARD_LEVEL

    turns = set_difficulty()

    def check_answer(user_choice, computer_choice, no_of_lives):
        if user_choice > computer_choice:
            print("Too High")
            return no_of_lives - 1
        if user_choice < computer_choice:
            print("Too Low")
            return no_of_lives - 1
        else:
            print("You got it!")
            print(f"the answer is {computer_choice}")
            return no_of_lives

    print(logo)
    print("Welcome to The Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    # print(answer)
    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns <= 0:
            print("You have run out of guesses, You lose.")
            # we wrapped the entire code in a function in order to use the return keyword and exit the loop
            return
        elif guess != answer:
            print("Guess Again")


game()

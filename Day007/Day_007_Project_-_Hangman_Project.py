# Use a flow chart to make things simple to plan and understand
# You can use draw.io to make a flowchart

# STEP 1 - Picking a random word
# TODO-1 - Randomly choose a word form the word_list and assign it to a variable called chosen_word.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen word

# STEP 2 - Replacing Blanks both Guesses
# TODO-1 - Create an empty list called display. For each letter in chosen_word add a "_" to display.
# TODO-2 - Loop through each position in chosen_word. If the letter at that position matches guess, then reveal that letter in display at that position
# TODO-3 - Print "display" and you should see the guessed letter in the correct possitons and every other letter replaced with "_"

# STEP 3 - Checking if the Player has Won
# TODO-1 - Use a while loop to let the user guess again. The loop should only stop once the suer has guessed all the letters in chosen_word and display has no more blanks("_")

# STEP 4 - Keeping Tracks of thr Player's Lives
# TODO-1 - Create a variable called "lives" to keep track of the number of lives left.
# TODO-2 - If guess is not a letter in the chosen_word, then reduce 'lives' by 1. If lives goes down to 0, then the game should stop and it should print "You lose."
# TODO-3 - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

# STEP 5 - Improving the User Experience
# TODO-1 - Update word_list to use the word_list from hangman_words.py
# TODO-2 - Import the stages from hangman_art.py
# TODO-3 - Import the logo from hangman_art.py and print it at the start of the game
# TODO-4 - If the user has entered a letter they've already guessed, print the letter and let them know.
# TODO-5 - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

import random
import hangman_art
from hangman_words import word_list

chosen_word = random.choice(word_list)
length_of_chosen_word = len(chosen_word)
end_of_game = False
lives = 6
guess_list = []

print(hangman_art.hangman_logo)

display = []
for letters in chosen_word:
    display.append("_")
print(display)

while not end_of_game:
    guess = input("Guess a letter:").lower()

    if guess not in guess_list:
        guess_list.append(guess)
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = guess

        if guess not in display:
            lives -= 1
            print(hangman_art.stages[lives])
            print(f"{guess} is not in the word. You have lost a life.")

        print(display)

        if "_" not in display:
            end_of_game = True
            print("You Win")

        if lives == 0:
            end_of_game = True
            print("You Lose")

    else:
        print(f"You have already guessed {guess}")
        guess_list.append(guess)
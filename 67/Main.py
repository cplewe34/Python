import wordle_functions  #imports all the functions from the wordle_functions.py file

#this is the introduction to the game and how to play it
print("Welcome to Wordle!!\n"
    "\nYou have 6 attempts to guess the 5-letter word.\n",
    "\nG = correct letter in the correct position\n"
    "Y = correct letter in the wrong position\n"
    "- = letter not in the word")

#starts the game by calling the play function from the wordle_functions.py file
wordle_functions.play()

#makes it so that the user can play again if they want to
play_again = input("Do you want to play again? (y/n): ").lower()
if play_again == 'y':
    wordle_functions.play()
else:
    print("Thanks for playing Wordle!")
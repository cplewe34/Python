#Generate Random Number
import random
def play_game():

    #Set up guesses and tries
    secret_number = random.randint(1, 100)
    guess = 0
    tries = 0

    #Game Loop for guessing the number
    while guess != secret_number:
        guess = int(input("Guess the number (1-100): "))
        tries += 1

        #print functions if wrong guess
        if guess > 100 or guess < 1:
                print("Please guess a number between 1 and 100.")
        elif guess < secret_number:
                print("Guess higher!")
        elif guess > secret_number:
                print("Guess lower!")
        else:
                print(f"Congratulations! You guessed the number.")
                print(f"It took you {tries} tries.")

            #print different messages based on the number of tries
    if tries <= 3:
                print("Excellent job!")
    elif tries <= 5:
                print("Impressive!")
    elif tries <= 7:
                print("Good Job!")
    elif tries <= 9:
                print("Took you quite a few tries!")
    elif tries > 9:
                print("Lock in")


#Play again Function
play_again = ("y")
while play_again == "y":
    play_game()
    play_again = input("Do you want to play again? (y/n): ").lower()
 
import random



def one_play(s): 

    print("Welcome to the Higher/Lower Guessing Game!")

    #get a ranodm number for user to guess
    solution = random.randint(1, 100)
    guess = 0
    tries = 0


    while guess != solution:

        guess = int(input("Guess a number between 1 and 100: "))


    #validate user imput to make sure it is between 1 and 100
        while not (guess >= 1 and guess <= 100):
            print("Please guess a number between 1 and 100.")
            guess = int(input("Guess a number between 1 and 100: "))

        tries += 1

        #determine the result
        if guess < solution:
            print("Too low!")
        elif guess > solution:
            print("Too high!")
        elif guess == solution:
            print("Congratulations! You guessed the number!")


    print(f"It took you {tries} guesses")
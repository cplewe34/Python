import random

def play_game():
    secret_number = random.randint(1, 100)
    guess = 0
    attempts = 0

    while guess != secret_number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"You got it! The secret number was {secret_number}.")
            print(f"It took you {attempts} tries.")

            if attempts <= 3:
                print("Amazing!")
            elif attempts <= 5:
                print("Impressive!")
            elif attempts <= 7:
                print("Good job!")
            elif attempts <= 9:
                print("Took a little longer, but you got there!")
            else:
                print("You need to lock in.")


play_again = "yes"

while play_again.lower() == "yes":
    play_game()
    play_again = input("Play again? (yes/no): ")

print("Thanks for playing!")
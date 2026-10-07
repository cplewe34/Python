import random


def computer_choice():
    computer = random.choice(["rock", "paper", "scissors"])
    return computer

def player_choice():
    while True:
        choice = input("Choose: Rock, Paper, or Scissors: ")
        choice = choice.lower().strip()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice please try again")

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "loss"


player_wins = 0
computer_wins = 0

print("Welcome to Rock, Paper, Scissors!")

while True:
    number_of_games = int(input("How many number of games would you like to play? (Must enter an odd number) "))

    if number_of_games % 2 == 0:
        print("Please enter an odd number")
    else:
        break
print(f"{number_of_games} games")

games_played = 0

while games_played < number_of_games:
    print(f"\nGame {games_played + 1} of {number_of_games}")

    player = player_choice()
    computer = computer_choice()

    print(f"You chose: {player}")
    print(f"The computer chose: {computer}")

    result = determine_winner(player, computer)

    if result == "tie":
        print("It's a tie! Play again.")
        continue  # tie doesn't count as a game
    elif result == "win":
        print("You Win!!")
        player_wins += 1
    else:
        print("Computer Wins!!")
        computer_wins += 1

    games_played += 1

print("\nFinal Score")
print(f"You: {player_wins}")
print(f"Computer: {computer_wins}")

if player_wins > computer_wins:
    print("You won the match!")
else:
    print("The computer won the match!")
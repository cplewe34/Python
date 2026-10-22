import random #makes it so the program can choose a random word from the list of words

#list of words to choose from
words = ["about", "above", "adult", "alien", "angel", "basic", "beach", "begin", "bland", "blind", "block", "blond", "brain", "brick", "brown", "chair", "charm", "chart", "chase", "chief", "child", "clamp", "clean", "clear", "climb", "cloud", "crane", "crisp", "dance", "dream", "drink", "drive", "earth", "flame", "flash", "fresh", "front", "ghost", "giant", "glare", "globe", "grape", "graph", "grasp", "great", "heart", "house", "human", "judge", "laugh", "learn", "light", "magic", "march", "money", "month", "mouse", "music", "night", "noise", "north", "ocean", "paint", "party", "peach", "phone", "piano", "plant", "plumb", "point", "pride", "prize", "quick", "raise", "range", "rival", "robin", "shape", "sharp", "shine", "shirt", "smile", "smoke", "snake", "spare", "spice", "stone", "storm", "sugar", "table", "thing", "think", "tiger", "trace", "trade", "train", "unity", "voice", "watch", "water"]

#The computer chooses a random word from the list
def choose_word():
    return random.choice(words).upper()


#gets the users guess and checks if it is valid (5 letters and not already guessed)
def get_guess(previous_guesses):
    while True:
        user_guess = input("Enter your guess: ").upper()
        if len(user_guess) != 5:
            print("Invalid guess. Please enter a word with 5 letters.")
        elif user_guess in previous_guesses:
            print("You already guessed that word. Try a different one.")
        else:
            return user_guess


#Checks the user's guess against the computer's word and provides feedback on each letter
def evaluate_guess(user_guess, computer_word):
    feedback = []
    for i in range(len(user_guess)):
        if user_guess[i] == computer_word[i]:
            feedback.append("G")
        elif user_guess[i] in computer_word:
            feedback.append("Y")
        else:
            feedback.append("-")
    return feedback

#uses this to display feedback in a readable format
def display_guess(user_guess, feedback):
    print(" ".join(user_guess))
    print(" ".join(feedback))

#Checks if user won the game
def has_won(user_guess, computer_word):
    if user_guess == computer_word:
        print("Congratulations! You've guessed the word correctly!")
        return True
    return False

#this function is the main game loop that controls the flow of the game
def play():
    computer_word = choose_word()
    max_attempts = 6
    previous_guesses = []

    #this loop allows the user to make a maximum of 6 guesses, calls from all other functions to join informtion together and provide feedback to the user
    for attempt in range(1,7):
        print(f"\nAttempt {attempt} of {max_attempts}")
        user_guess = get_guess(previous_guesses)
        previous_guesses.append(user_guess)
        feedback = evaluate_guess(user_guess, computer_word)
        display_guess(user_guess, feedback)

        #validates if the user has won the game and ends the game if they have
        if has_won(user_guess, computer_word):
            return

    #tells you that you lost and tells you the word
    print(f"\nOut of attempts! The word was {computer_word}.")
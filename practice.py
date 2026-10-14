import random
sentence = ["Yes", "No"]


def yes_no():
    computer = random.choice(sentence)
    if computer == "Yes":
            print("You selected Yes.")
    else:
        print("You selected No")



print(yes_no)
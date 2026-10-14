has_error = True

while has_error:
    try:
        number = int(input("Enter Number: "))
        print(number)

        has_error = False

    except ValueError:
        print("Invalid number")
    except KeyboardInterrupt:
        print("You stopped the program")
        continue
    except:
        print("You got some rando error")
        break
    finally:
        print("You finished")
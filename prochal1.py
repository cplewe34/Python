blah = [1, 17, 19, 22]
even_number = 0
odd_number = 0 

for number in blah:
    if number % 2 == 0:
        even_number += 1
        print(f"{number} is even")
    else:
        odd_number += 1
        print(f"{number} is odd")

print(f"Total even numbers: {even_number}")
print(f"Total odd numbers: {odd_number}")
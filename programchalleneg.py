#1. positive Negative, or zero
#requirements:
numbers = [7, 60, -3, 0, 5]
current_number = 0
positive_count = 0
negative_count = 0
zero_count = 0

    # Use a loop to collect the numbers
for number in range(0,5):
    current_number =numbers[number]

    if current_number > 0:
        positive_count += 1
    elif current_number < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zero numbers: {zero_count}")

    #keep counts of each category and display totals at the end
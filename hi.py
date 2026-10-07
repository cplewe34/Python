spend = float(input(f"What is youre monethly allowance? "))

print(spend)



total_purchases = 0
while True:
    purchases = float(input(f"How much did you spend already? "))
    if purchases == 0:
          break
    total_purchases += purchases
    print(f"Your total spending is {total_purchases}")

remaining_balance = spend - total_purchases


print(f"Starting allowance: {spend}")
print(f"Total spent: {total_purchases}")
print(f"Remaining Balance: {remaining_balance}")
      

        

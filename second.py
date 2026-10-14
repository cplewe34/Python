from bankfunction import withdraw
balance = 100

try:
    amount = int(input("Please enter the amount you would like to withdraw: "))

    balance = withdraw(amount, balance)
except:
    print("Why you so broke")
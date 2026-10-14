def withdraw(amount, balance):
    if amount <= balance: 
        raise Exception("You Broke")

        return balance - amount
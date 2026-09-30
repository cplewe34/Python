#Size Limits
SMALL_LIMIT = 25
LARGE_LIMIT = 100

#Enter all expenses
def get_expenses():
    expenses = []

    while True:
        entry = input("Enter an expense (or 0 to finish): $")
        amount = float(entry)

        if entry < 0:
            print("Expenses cannot be negative. Please try again.")
        
        else:
            amount = float(entry)
            if amount == 0:
                break
            expenses.append(amount)

    return expenses


#Put ex   penses into categories
def classify_expenses(expenses):
    small = 0
    moderate = 0
    large = 0

    for expense in expenses:
        if expense < SMALL_LIMIT:
            small += 1
        elif expense <= LARGE_LIMIT:
            moderate += 1
        else:
            large += 1

    return small, moderate, large


#print receipt
def main():
    print("=== Personal Expense Analyzer ===")
    expenses = get_expenses()

    if len(expenses) == 0:
        print("\nNo expenses were entered.")
        return

    small, moderate, large = classify_expenses(expenses)

    total = sum(expenses)
    average = total / len(expenses)
    smallest = min(expenses)
    largest = max(expenses)

    print("\n=== Expense Summary ===")
    print(f"Total number of expenses: {len(expenses)}")
    print(f"Total expenses:           ${total:,.2f}")
    print(f"Average expense:          ${average:,.2f}")
    print(f"Smallest expense:         ${smallest:,.2f}")
    print(f"Largest expense:          ${largest:,.2f}")
    print(f"Small expenses:           {small}")
    print(f"Moderate expenses:        {moderate}")
    print(f"Large expenses:           {large}")


main()
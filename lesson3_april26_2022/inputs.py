

def bill_calculator():
    print("Welcome to the Tip Calculator!")
    bill = float(input("What was the total bill? $"))
    tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
    people = float(input("How many people to split the bill? "))
    bill_split = ((bill) / (people)) + ((tip / 100) * bill)
    final_amount = round(bill_split, 2)
    print(f"Each person should pay: ${final_amount}")
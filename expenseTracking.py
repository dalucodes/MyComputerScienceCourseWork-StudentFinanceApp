from datetime import datetime
def addexpenses():   
    while True:
        date_input= input("Enter a date YYYY-MM-DD")
        try:
            date=datetime.strptime(date_input, "%Y-%m-%d").date
            break
        except ValueError:
            print("Input valid date in format YYYY-DD-MM example(2025-12-05)")

    amount =int(input("How much did you spend today"))
    while True:
        print("Amount can not be less than 0")
        amount =int(input("ENTER AN AMOUNT GREATER THAN 0"))
    category=input("Food, Bills etc")
    merchant = input("What is the name of the store")
    max_length = 100
    passing=True
    while passing:
        notes= input("DO you have any reflective notes, like why you purcahsed etc")
        if len(notes) <=max_length:
            passing =False
        else:     
            print("Notes must be less than 100 characters ")
    return {
        "amount":amount,
        "category":category,
        "merchant":merchant,
        "notes":notes,
        "date": date

    } 

expense_record=addexpenses()
print(expense_record)
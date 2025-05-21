from datetime import datetime

def expense_input():
    category = ""
    while not category:
        category = input("Introduce the category of your expense (ex. food, transport, etc): ")
        
    description = ""
    while not description:
        description = input("Introduce a title or description for your expense: ")
        
    while True:
        try:
            amount = float(input("Introduce the expense amount: "))
            break
        except ValueError:
            print("Please, introduce a valid number for your expense.")
            
    while True:
        date = input("Introduce the date of the expense (YYYY-MM-DD) or press Enter to use the current date.")
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
            break
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            
    return category, description, amount, date
def add_expenses(expenses, category, description, amount, date):
    expense = {
        "category": category,
        "description": description,
        "amount": amount,
        "date": date,
    }
    if category not in expenses:
        expenses[category] = []
    expenses[category].append(expense)

def show_expenses(expenses):
    for category, expenses_list in expenses.items():
        print(f"Category: {category}")
        for expense in expenses_list:
            print(f"Description: {expense['description']}")
            print(f"Amount: {expense['amount']}")
            print(f"Date: {expense['date']}")
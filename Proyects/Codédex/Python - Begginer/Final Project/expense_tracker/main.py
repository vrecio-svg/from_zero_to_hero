import os
from expense_input import expense_input
from expense_management import add_expenses, show_expenses
from file_operations import save_expenses, load_expenses

def main():
    expenses = load_expenses()
    category, description, amount, date = expense_input()
    add_expenses(expenses, category, description, amount, date)
    save_expenses(expenses)
    
if __name__ == "__main__":
    main()



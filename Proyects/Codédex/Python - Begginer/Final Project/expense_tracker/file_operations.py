import os
import json

def save_expenses(expenses, folder="data", filename="expenses.json"):
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(base_path, folder)
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    filepath = os.path.join(data_folder, filename)
    with open(filepath, "w") as f:
        json.dump(expenses, f, indent=4)
    print(f"Thank you! Expenses saved to {filepath}. ✨")

def load_expenses(filename = "expenses.json", folder = "data"):
    base_folder = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(base_folder, folder)
    filepath = os.path.join(data_folder, filename)
    
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
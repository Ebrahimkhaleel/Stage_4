import json
import os
from datetime import datetime
import budget_utils

# Transaction class
class Transaction:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

# Function to add a transaction
def add_transaction(transactions):
    category = input("Enter category : ")
    try:
        amount = float(input("Enter amount: "))
        if amount < 0:
            raise ValueError("Amount cannot be negative!")
        date = datetime.now().strftime("%Y-%m-%d")
        transactions.append(Transaction(date, category, amount))
        print(f"Transaction added: {category}, ${amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

# Function to view transactions by category
def view_by_category(transactions):
    if not transactions:
        print("No transactions recorded.")
        return
    categories = budget_utils.get_categories(transactions)
    print("\nTransactions by Category:")
    for category in categories:
        total = budget_utils.calculate_category_total(transactions, category)
        print(f"{category}: ${total:.2f}")

# Function to save transactions to JSON
def save_to_json(transactions, filename="transactions.json"):
    data = [{"date": t.date, "category": t.category, "amount": t.amount} for t in transactions]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print("Data saved to transactions.json")

# Function to load transactions from JSON
def load_from_json(filename="transactions.json"):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return [Transaction(d["date"], d["category"], d["amount"]) for d in data]
    except json.JSONDecodeError:
        print("Error loading JSON file. Starting with empty list.")
        return []

# Main program
def main():
    transactions = load_from_json()
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Transaction")
        print("2. View by Category")
        print("3. Save and Exit")
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            view_by_category(transactions)
        elif choice == '3':
            save_to_json(transactions)
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-3.")

if __name__ == "__main__":
    main()
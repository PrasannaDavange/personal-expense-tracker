"" 
import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Create the file with headers if it doesn't exist
def initialize_csv():
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Amount", "Category"])
    except FileExistsError:
        pass

# Add a new expense
def add_expense():
    description = input("Enter description: ")
    amount = input("Enter amount: ")
    category = input("Enter category (e.g., food, travel): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount, category])

    print("✅ Expense added!\n")

# View all expenses
def view_expenses():
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found.\n")

# Main menu
def main():
    initialize_csv()
    while True:
        print("📘 Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()

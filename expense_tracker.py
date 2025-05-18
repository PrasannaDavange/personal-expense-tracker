import csv
from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox, ttk

FILENAME = "expenses.csv"

# Create the file with headers if it doesn't exist
def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Amount", "Category"])

# Add a new expense
def add_expense():
    description = description_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not description or not amount or not category:
        messagebox.showwarning("Missing Data", "Please fill all fields.")
        return

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount, category])

    messagebox.showinfo("Success", "Expense added!")
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

# View all expenses
def view_expenses():
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if len(rows) <= 1:
            messagebox.showinfo("Expenses", "No expenses yet.")
            return

        # Create a new window
        top = tk.Toplevel(root)
        top.title("All Expenses")

        tree = ttk.Treeview(top, columns=("Date", "Description", "Amount", "Category"), show='headings')
        for col in ("Date", "Description", "Amount", "Category"):
            tree.heading(col, text=col)
            tree.column(col, width=120)

        for row in rows[1:]:
            tree.insert('', tk.END, values=row)

        tree.pack(expand=True, fill='both')
    except FileNotFoundError:
        messagebox.showerror("Error", "Expense file not found.")

# GUI Setup
initialize_csv()
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("400x300")

tk.Label(root, text="Description").pack()
description_entry = tk.Entry(root, width=40)
description_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root, width=40)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root, width=40)
category_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)
tk.Button(root, text="View Expenses", command=view_expenses).pack()

root.mainloop()

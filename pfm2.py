import tkinter as tk
from tkinter import messagebox

class PersonalFinanceManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Manager")

        # Initialize finance dictionaries
        self.finances = {'income': {}, 'expenses': {}}

        # Set up the GUI layout
        tk.Label(root, text="Select Type:").grid(row=0, column=0)
        self.type_var = tk.StringVar(root)
        self.type_var.set("income")  # set default option
        options = ["income", "expenses"]
        self.option_menu = tk.OptionMenu(root, self.type_var, *options)
        self.option_menu.grid(row=0, column=1)

        tk.Label(root, text="Category/Source:").grid(row=1, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1)

        tk.Label(root, text="Amount:").grid(row=2, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=2, column=1)

        self.add_button = tk.Button(root, text="Add Entry", command=self.add_entry)
        self.add_button.grid(row=3, columnspan=2)

        self.summary_button = tk.Button(root, text="Show Summary", command=self.show_summary)
        self.summary_button.grid(row=4, columnspan=2)

    def add_entry(self):
        # Get the user input
        category = self.category_entry.get()
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid amount.")
            return

        # Update finances dictionary
        finance_type = self.type_var.get()
        if category:
            if category in self.finances[finance_type]:
                self.finances[finance_type][category] += amount
            else:
                self.finances[finance_type][category] = amount
            messagebox.showinfo("Entry Added", f"Added {amount} to {category} under {finance_type}.")
        else:
            messagebox.showerror("Error", "Category/Source cannot be empty.")

        # Clear entries
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def show_summary(self):
        total_income = sum(self.finances['income'].values())
        total_expenses = sum(self.finances['expenses'].values())
        net_balance = total_income - total_expenses

        summary = f"Total Income: ${total_income}\nTotal Expenses: ${total_expenses}\nNet Balance: ${net_balance}"
        messagebox.showinfo("Financial Summary", summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalFinanceManagerGUI(root)
    root.mainloop()

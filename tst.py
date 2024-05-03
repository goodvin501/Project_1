import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from datetime import datetime

class YourApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        self.list_of_expenses = tk.Frame(self.master)
        self.list_of_expenses.pack(fill=tk.BOTH, expand=tk.YES)

        # Column data for the Tableview
        self.coldata = [
            {"text": "№", "width": 50, "stretch": False},  # Row number column
            {"text": "ID", "width": 0, "stretch": False},
            {"text": "Desription"},
            {"text": "Amount", "stretch": False},
            {"text": "Category"},
            {"text": "Date", "width": 150, "stretch": False}
        ]

        # Create Tableview widget
        self.dt = Tableview(
            master=self.list_of_expenses,
            coldata=self.coldata,
            rowdata=self.get_all_expenses(),
            paginated=True,
            searchable=True,
            bootstyle="primary",
            pagesize=25,
            height=25
        )

        self.dt.pack(fill=tk.BOTH, expand=tk.YES)

        # Button to remove a row
        remove_button = tk.Button(self.master, text="Remove Row", command=self.remove_row)
        remove_button.pack()

    def remove_row(self):
        # Remove the selected row from the table
        selection = self.dt.selection()
        if selection:
            self.dt.delete(selection)

            # Update row numbers of subsequent rows
            for i, row_id in enumerate(self.dt.get_children(), start=1):
                self.dt.item(row_id, values=(i, *self.dt.item(row_id, 'values')[1:]))

    def get_all_expenses(self):
        # Replace this method with your actual implementation to get expenses data
        # Return a list of lists where each inner list represents an expense
        expenses_data = [
            ["exp_001", "Description 1", 100.50, "Category A", datetime.now()],
            ["exp_002", "Description 2", 200.75, "Category B", datetime.now()],
            # Add more expense data as needed
        ]

        # Add row numbers to the data
        for i, _ in enumerate(expenses_data, start=1):
            expenses_data[i-1] = [i] + expenses_data[i-1]

        return expenses_data

root = tk.Tk()
app = YourApplication(root)
root.mainloop()

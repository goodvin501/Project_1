from ux.ErrorWindow import ErrorWindow
from ux.ExpenseInputWindow import ExpenseInputWindow

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

class MainWindow(ttk.Window):

    def __init__(self, expenses):
        super().__init__()
        self.colors = self.style.colors
        self.expenses = expenses
        self.config(width=750, height=700)
        self.title("Finance Tracker")
        self.label_your_expenses = ttk.Label(text='Your Expenses:', font=('TkDefaultFont', 20, 'bold'))
        self.label_your_expenses.place(x=20, y=20)

        self.button_add_new_expense = ttk.Button(
            self,
            text="Add new expense",
            command=self.request_expense
        )
        self.button_add_new_expense.place(x=20, y=590, width=270)


        self.list_of_expenses = tk.Listbox(self)
        self.list_of_expenses.place(x=20, y=50)

        self.coldata = [
            {"text": "ID", "width": 50, "stretch": False},
            "Desription",
            {"text": "Amount", "stretch": False},
            "Category"
        ]
    
        self.dt = Tableview(
            master=self.list_of_expenses,
            coldata=self.coldata,
            rowdata=self.expenses.get_all_expenses(),
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            pagesize=25,
            height=25
        )
        self.dt.pack(fill=BOTH, expand=YES)

    def request_expense(self):
        self.created_window = ExpenseInputWindow(self.expenses.get_categories(), callback=self.expense_entered)

    def expense_entered(self, description, amount, category):
        try:
            self.expenses.add_expense(description, amount, category)
            self.dt.insert_row(values=self.expenses.get_all_expenses()[-1])
            self.dt.load_table_data()
            self.created_window.destroy()
        except Exception as err:
            self.error_window = ErrorWindow(err)
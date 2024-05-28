from ux.ErrorWindow import ErrorWindow
from ux.ExpenseInputWindow import ExpenseInputWindow
from ux.PieChartWindow import PieChartWindow

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

class MainWindow(ttk.Window):

    def __init__(self, expenses):
        super().__init__()
        self.colors = self.style.colors
        self.expenses = expenses
        self.config(width=850, height=700)
        self.resizable(0, 0)
        self.title("Finance Tracker")
        self.label_your_expenses = ttk.Label(text='Your Expenses:', font=('TkDefaultFont', 20, 'bold'))
        self.label_your_expenses.place(x=20, y=20)

        self.button_add_new_expense = ttk.Button(
            self,
            text="Add new expense",
            command=self.request_expense
        )
        self.button_add_new_expense.place(x=20, y=590, width=270)

        self.button_delete_expense = ttk.Button(
            self,
            text="Delete chosen expense",
            command=self.delete_expense
        )
        self.button_delete_expense.place(x=300, y=590, width=270)

        self.button_expenses_per_cat = ttk.Button(
            self,
            text="Show expenses per categories",
            command=self.show_expenses_per_cat
        )
        self.button_expenses_per_cat.place(x=20, y=625, width=270)


        self.button_exit = ttk.Button(
            self,
            text="Exit",
            command=self.button_exit_pressed
        )
        self.button_exit.place(x=300, y=625, width=270)


        self.list_of_expenses = tk.Listbox(self)
        self.list_of_expenses.place(x=20, y=50)

        self.coldata = [
            {"text": "№", "width": 50, "stretch": False},
            {"text": "ID", "width": 0, "stretch": False},
            {"text": "Desription"},
            {"text": "Amount", "stretch": False},
            {"text": "Category"},
            {"text": "Date", "width": 150, "stretch": False}
        ]

        self.dt = Tableview(
            master=self.list_of_expenses,
            coldata=self.coldata,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            pagesize=25,
            height=25
        )
        self.reload_table_data()
        self.dt.pack(fill=BOTH, expand=YES)


    def request_expense(self):
        self.created_window = ExpenseInputWindow(self.expenses.get_categories(), callback=self.expense_entered)

    def expense_entered(self, description, amount, category, date):
        try:
            self.expenses.add_expense(description, amount, category, date)
            self.reload_table_data()
            self.created_window.destroy()
        except Exception as err:
            self.error_window = ErrorWindow(err)
    def delete_expense(self):
        lst = self.dt.get_rows(selected=True)
        for el in lst:
            self.expenses.delete_expense(id=el.values[1])
        self.reload_table_data()

    def button_exit_pressed(self):
        self.destroy()

    def show_expenses_per_cat(self):
        self.exp = []
        for expense in self.expenses.get_all_expenses():
            self.exp.append(expense)
        self.pie_chart_window = PieChartWindow(self.exp)
    
    def reload_table_data(self):
        i = 1
        self.dt.delete_rows()
        for expense in self.expenses.get_all_expenses():
            tup = (i, ) + expense
            self.dt.insert_row(values=tup)
            i += 1
        self.dt.load_table_data()
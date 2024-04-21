from ux.ErrorWindow import ErrorWindow
from ux.ExpenseInputWindow import ExpenseInputWindow
from ux.ExpenseDeleteWindow import ExpenseDeleteWindow

import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):

    def __init__(self, expenses):
        super().__init__()
        self.expenses = expenses
        self.config(width=700, height=700)
        self.title("Finance Tracker")
        self.label_your_expenses = ttk.Label(text='Your Expenses:', font=('TkDefaultFont', 20, 'bold'))
        self.label_your_expenses.place(x=20, y=20)

        self.button_add_new_expense = ttk.Button(
            self,
            text="Add new expense",
            command=self.request_expense
        )
        self.button_add_new_expense.place(x=20, y=570, width=270)

        self.button_delete_expense = ttk.Button(
            self,
            text="Delete an expense",
            command=self.delete_expense
        )
        self.button_delete_expense.place(x=20, y=600, width=270)

        self.list_of_expenses = tk.Listbox(
            self,
            height=30,
            width=30, 
            )
        self.list_of_expenses.place(x=20, y=50)
        self.show_all_expenses()

    def request_expense(self):
        self.created_window = ExpenseInputWindow(self.expenses.get_categories(), callback=self.expense_entered, callback_2=self.show_all_expenses)

    def delete_expense(self):
        self.expense_delete_window = ExpenseDeleteWindow(self.expenses.get_categories())


    def expense_entered(self, description, amount, category):
        try:
            self.expenses.add_expense(description, amount, category)
            self.created_window.destroy()
        except Exception as err:
            self.error_window = ErrorWindow(err)

    def show_all_expenses(self):
        self.list_of_expenses.delete(0, 'end')
        for expense in self.expenses.get_all_expenses():                                            
            self.list_of_expenses.insert('end', f"ID:  {expense[0]}")
            self.list_of_expenses.insert('end', f"Description:  {expense[1]}")
            self.list_of_expenses.insert('end', f"Amount:  {expense[2]}")
            self.list_of_expenses.insert('end', f"Category:  {expense[3]}")
            self.list_of_expenses.insert('end', "----------------------------")
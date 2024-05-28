import tkinter as tk
from tkinter import ttk
from ttkbootstrap import DateEntry

class ExpenseInputWindow(tk.Toplevel):

    def __init__(self, categories=[], callback=None):
        super().__init__()
        self.callback = callback
        self.config(width=700, height=700)
        self.resizable(0, 0)
        self.title("Enter Expense")

        #description
        self.label_expense_description= ttk.Label(
            self,
            text="Description:"
        )
        self.label_expense_description.place(x=20, y=20)
        self.expense_description = ttk.Entry(self)
        self.expense_description.place(x=100, y=20, width=260)

        #amount
        self.label_expense_amount = ttk.Label(
            self,
            text="Amount:"
        )
        self.label_expense_amount.place(x=20, y=50)
        self.expense_amount = ttk.Entry(self)
        self.expense_amount.place(x=100, y=50, width=260)

        #category
        self.label_expense_amount = ttk.Label(
            self,
            text="Category:"
        )
        self.label_expense_amount.place(x=20, y=80)
        self.expense_category = ttk.Combobox(self, values=categories)
        self.expense_category.place(x=100, y=80, width=260)

        #date
        self.label_date = ttk.Label(
            self,
            text="Date:"
        )
        self.label_date.place(x=20, y=110)
        self.date_entry = DateEntry(master=self, firstweekday=0, dateformat='%Y-%m-%d')
        self.date_entry.place(x=100, y=110, width=260)

        #submit button
        self.button_submit = ttk.Button(
            self,
            text="Submit",
            command=self.button_submit_pressed
        )
        self.button_submit.place(x=20, y=150, width=210)

        #close button
        self.button_exit = ttk.Button(
            self,
            text="Close",
            command=self.button_close_pressed
        )
        self.button_exit.place(x=250, y=150, width=110)


    def button_submit_pressed(self):
        self.callback(description=self.expense_description.get(),
                      amount=self.expense_amount.get(),
                      category=self.expense_category.get(),
                      date=self.date_entry.entry.get())

    def button_close_pressed(self):
        self.destroy()
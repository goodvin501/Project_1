import tkinter as tk
from tkinter import ttk

class ExpenseDeleteWindow(tk.Toplevel):

    def __init__(self, categories=[]):
        super().__init__()
        self.config(width=700, height=700)
        self.resizable(0, 0)
        self.title("Delete Expense")

        self.label_expense_amount = ttk.Label(
            self,
            text="Category:"
        )
        self.label_expense_amount.place(x=20, y=80)
        self.expense_category = ttk.Combobox(self, values=categories)
        self.expense_category.bind("<<ComboboxSelected>>")
        self.expense_category.place(x=100, y=80, width=260) 
        #close button
        self.button_exit = ttk.Button(
            self,
            text="Close",
            command=self.button_close_pressed
        )
        self.button_exit.place(x=260, y=110, width=120)


    def button_delete_pressed(self):
        pass

    def button_close_pressed(self):
        self.destroy()
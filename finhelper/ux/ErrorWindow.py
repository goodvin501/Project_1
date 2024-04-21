import tkinter as tk
from tkinter import ttk


class ErrorWindow(tk.Toplevel):

    def __init__(self, err):
        super().__init__()
        self.config(width=200, height=100)
        self.resizable(0, 0)
        self.title("Error Window")
        self.label_invalid_data= ttk.Label(
            self,
            text=err
        )
        self.label_invalid_data.place(x=10, y=10)

        self.button_ok= ttk.Button(
            self,
            text="Ok",
            command=self.button_ok_pressed
        )
        self.button_ok.place(x=30, y=40)

    def button_ok_pressed(self):
        self.destroy()
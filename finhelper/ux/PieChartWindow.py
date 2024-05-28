import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkbootstrap import DateEntry

import tkinter as tk
from tkinter import ttk


class PieChartWindow(tk.Toplevel):

    def __init__(self, expenses):
        super().__init__()
        self.config(width=750, height=500)
        self.resizable(0, 0)
        self.title("Pie Chart")
        self.expenses = expenses


        self.from_date_lable = ttk.Label(
            self,
            text="From:"
        )
        self.from_date_lable.place(x=20, y=400)
        self.from_date_entry = DateEntry(master=self, firstweekday=0, dateformat='%Y-%m-%d')
        self.from_date_entry.place(x=60, y=400, width=260)

        self.to_date_lable = ttk.Label(
            self,
            text="To:"
        )
        self.to_date_lable.place(x=350, y=400)
        self.to_date_entry = DateEntry(master=self, firstweekday=0, dateformat='%Y-%m-%d')
        self.to_date_entry.place(x=375, y=400, width=260)

        self.button_exit = ttk.Button(
            self,
            text="Close",
            command=self.button_close_pressed
        )
        self.button_exit.place(x=150, y=450, width=110)

        self.button_show = ttk.Button(
            self,
            text="Show",
            command=self.button_show_pressed
        )
        self.button_show.place(x=20, y=450, width=110)

        self.mainloop()


    def button_close_pressed(self):
        try:
            plt.close(self.fig)
        except:
            pass
        self.destroy()

    def button_show_pressed(self):
        self.count()

        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True

        self.fig, ax = plt.subplots()
        ax.pie(self.sizes, labels=self.labels, autopct=lambda p: '{:.1f} ({:.0f}%)'.format(p, p * sum(self.sizes) / 100))

        self.canvas = FigureCanvasTkAgg(self.fig, 
							master = self) 
        self.canvas.draw()

        self.canvas.get_tk_widget().place(x=0, y=0)

    def count(self):
        self.sizes = []
        self.labels = []
        for expense in self.expenses:
            if expense[-1] >= self.from_date_entry.entry.get() and expense[-1] <= self.to_date_entry.entry.get():
                if not expense[3] in self.labels:
                    self.labels.append(expense[3])
                    self.sizes.append(expense[2])
                else:
                    i = 0
                    while not expense[3] == self.labels[i]:
                        i+=1
                    self.sizes[i] += expense[2]

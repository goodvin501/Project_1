import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
from tkinter import ttk


class PieChartWindow(tk.Toplevel):

    def __init__(self, sizes, labels):
        super().__init__()
        self.config(width=750, height=500)
        self.resizable(0, 0)
        self.title("Pie Chart")

        self.button_exit = ttk.Button(
            self,
            text="Close",
            command=self.button_close_pressed
        )
        self.button_exit.place(x=300, y=400, width=110)

        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True

        self.sizes = sizes
        self.labels = labels

        self.fig, ax = plt.subplots()
        ax.pie(self.sizes, labels=self.labels, autopct=lambda p: '{:.0f} ({:.1f}%)'.format(p, p * sum(self.sizes) / 100))

        self.canvas = FigureCanvasTkAgg(self.fig, 
							master = self) 
        self.canvas.draw()

        self.canvas.get_tk_widget().place(x=0, y=0)


        self.mainloop()


    def button_close_pressed(self):
        plt.close(self.fig)
        self.destroy()
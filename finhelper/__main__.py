
from core.Expenses import Expenses
from ux.MainWindow import MainWindow

def main():
    my_expenses = Expenses()
    main_window = MainWindow(my_expenses)
    main_window.mainloop()

if __name__ == "__main__":
    main()
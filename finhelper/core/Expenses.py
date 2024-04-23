import sqlite3 as db

class Expenses():

    def __init__(self):
        self.conn = db.connect('expenses.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                            (id INTEGER PRIMARY KEY,
                            description TEXT,
                            amount REAL,
                            category TEXT)''')
        self.conn.commit()

    def add_expense(self, description, amount, category):
        self.expense_validate(description, amount, category)
        self.cursor.execute("INSERT INTO expenses (description, amount, category) VALUES (?, ?, ?)", (description, amount, category))
        self.conn.commit()

    def expense_validate(self, description, amount, category):
        try:
            self.amount_f = float(amount)
        except ValueError:
            raise TypeError("Invalid amount")
        if category == '':
            raise ValueError("Category is not selected")
        
    def delete_expense(self, id):
        self.cursor.execute("DELETE FROM expenses WHERE id = ?;", [id])
        self.conn.commit()

    def get_categories(self):
        self.cursor.execute("SELECT DISTINCT category FROM expenses")
        return list(self.cursor.fetchall())
    
    def get_all_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        return self.cursor.fetchall()
    
    def get_expenses_per_category(self, category):
        self.cursor.execute("SELECT amount FROM expenses WHERE category = ?;", [category])
        return self.cursor.fetchall()
        

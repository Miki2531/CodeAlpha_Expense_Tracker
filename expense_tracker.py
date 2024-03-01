import sqlite3
from expense import Expense, input_variables
from datetime import datetime

#connect SQLite 3 database

conn = sqlite3.connect('expense_tracker.db')
cou  = conn.cursor()

#create an expense db table if it does not exist.
cou.execute('''
CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT,
            name TEXT,
            category TEXT,
            description TEXT,
            amount REAL
            
)
''')

conn.commit()
conn.close()


#create the view for create(add)
def add_expense(date, name, category, description, amount):

    expense = Expense(date, name, category, description, amount)

    #connect to the SQLite database
    conn = sqlite3.connect('expense_tracker.db')
    cou = conn.cursor()

    #Insert expense into the db
    cou.execute('''
                INSERT INTO expenses (date, name, category, description, amount)
                VALUES (?, ?, ?, ?, ?)
''', (expense.date, expense.name, expense.category, expense.description, expense.amount))
    
    conn.commit()
    print("Expense addes successfully.")
    conn.close()


def view_expense():
    conn = sqlite3.connect('expense_tracker.db')
    cou = conn.cursor()

    #Retrive and dispaly all expenses
    cou.execute('SELECT * FROM expenses')
    expenses = cou.fetchall()

    print("\nExpense views")
    for expense in expenses:
        print(f"ID: {id} Date: {expense[1]},Name: {expense[2]}, Catagory: {expense[3]}, Description: {expense[4]}, Amount : {expense[5]}")
    conn.close()



def calculate_totals():
    conn = sqlite3.connect('expense_tracker.db')
    cou = conn.cursor()

    #calculate daily, monthly, and yearly expense total
    cou.execute('SELECT SUM(amount) FROM expense WHERE date = DATE()')
    daily_total = cou.fetchone()[0]

    cou.execute('SELECT SUM(amount) FROM expenses WHERE strftime("%Y-%m", date) = strftime("%Y-m%", DATE())')
    monthly_total = cou.fetchone()[0]
    
    cou.execute('SELECT SUM(amount) FROM expenses WHERE strftime("%Y", date) = strftime("%Y", DATE())')
    yearly_total = cou.fetchone()[0]

    #Display the total
    print("\n Expense Total")
    print(f"Daily Total: {daily_total}")
    print(f"Monthly Total: {monthly_total}")
    print(f"Yearly Total: {yearly_total}")


    conn.close()

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Calculate Totals")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            #Adding your expense
            add_expense(input_variables)
            print("Expense Added successfuly!")

        elif choice == 2:
            view_expense()
        elif choice == 3:
            calculate_totals()
        elif choice == 4:
            print("Exiting from Expense Tracker.")
            break
        else:
            print("Invalid choice. Please choose a valid option")

if __name__ == "__main__":
    main()

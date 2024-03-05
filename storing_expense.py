import csv
import ast
from expense import input_variables

#Initialize csv
CSV_FILE = "expense.csv"

#check if the csv file exits: if not create the new csv file.
def create_csv():
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerow(['Date', 'Name', 'Category', 'Descriptions', 'Amount'])

    except FileExistsError:
        print("The file already Exists.")


def add_expense(input_variables):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([input_variables])

def add_expense_menu():
    add_expense(input_variables())
    print("Expense added successfully!!")

def view_expense():
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)

        for index, row in enumerate(reader, start=1):
             expense_data = ast.literal_eval(row[0])
             expense_date, expense_name, expense_category, expense_description, expense_amount = expense_data
             # Print the formatted expense information
             print(f"Index: {index}, Date: {expense_date}, Name: {expense_name}, Category: {expense_category}, Description: {expense_description}, Amount: {expense_amount}")

def calculate_totals():
    daily = 0.0
    monthly = 0.0
    yearly = 0.0

    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            amount = row[5]
            amount = float(amount)

            daily += amount
            monthly += amount
            yearly += amount
    

    print("\n Expense Total")
    print(f"Daily Total: {daily}")
    print(f"Monthly Total: {monthly}")
    print(f"Yearly Total: {yearly}")


def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Create CSV")
        print("2, Add Expense ")
        print("3. View Expense")
        print("4. Calculate Totals")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            create_csv()  
        elif choice == 2:
            add_expense_menu()
        elif choice == 3:
            view_expense()
        elif choice == 4:
            calculate_totals()
        elif choice == 5:
            print("Exiting from Expense Tracker.")
            break
        else:
            print("Invalid choice. Please choose a valid option")

if __name__ == "__main__":
    main()
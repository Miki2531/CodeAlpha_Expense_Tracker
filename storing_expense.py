import csv
from expense import input_variables

#Initialize csv
CSV_FILE = "expense.csv"

#check if the csv file exits: if not create the new csv file.
def create_csv():
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Name', 'Category', 'Descriptions', 'Amount'])

    except FileExistsError:
        print("The file already Exists.")


def add_expense(date, name, category, description, amount):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, name, category, description, amount])

def add_expense_menu():
    add_expense_menu(input_variables)
    print("Expense added successfully!!")

def view_expense():
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            print(f"Date: {row[1]}, Name: {row[2]},  Category:{row[3]}, Description:{row[4]}, Amount:{row[5]}")

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
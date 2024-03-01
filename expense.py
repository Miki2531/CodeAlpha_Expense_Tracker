
class Expense:
    def __init__(self,date, name, category, description, amount):
        self.date = date
        self.name = name
        self.category = category
        self.description = description
        self.amount = amount

    def __repr__(self) -> str:
        return f"<Expense: {self.date}, {self.name}, {self.category}, {self.description}, {self.amount}>"
    

def input_variables():
    date = input("Enter the date(YYYY-MM-DD: ")
    name = input("Enter the name of expense: ")
    category = input("Enter the category: ")
    description = input("Enter the descriptions: ")
    amount = float(input("Enter the amount: "))

    return date, name, category, description, amount

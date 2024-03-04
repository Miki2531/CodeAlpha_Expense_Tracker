from tkinter import *
from expense_tracker import add_expense, updateExpense, deleteExpense
import sqlite3
import tkinter.simpledialog as sd


def add_expense_button_cliked():
    #input elements
    date  = date_entry.get()
    name = name_entry.get()
    category = category_entry.get()
    description = description_entry.get()
    amount = amount_entry.get()

    add_expense(date, name, category, description, amount)
    
    #clear the input fieldss
    date_entry.delete(0, END)
    name_entry.delete(0, END)
    category_entry.delete(0, END)
    description_entry.delete(0, END)
    amount_entry.delete(0, END)

def view_expense():
    view_window = Toplevel(root)
    view_window.title("View Expenses")
    view_window.geometry("400x300")

    conn = sqlite3.connect('expense_tracker.db')
    cou = conn.cursor() 
    cou.execute('SELECT * FROM expenses')
    expenses = cou.fetchall()

    #Add lebel for each fields
    Label(view_window, text='Date', font=("Arial", 10, "bold")).grid(row=0, column=0)
    Label(view_window, text='Name', font=("Arial", 10, "bold")).grid(row=0, column=1)
    Label(view_window, text='Category', font=("Arial", 10, "bold")).grid(row=0, column=2)
    Label(view_window, text='Description', font=("Arial", 10, "bold")).grid(row=0, column=3)
    Label(view_window, text='Amount', font=("Arial", 10, "bold")).grid(row=0, column=4)

    for index, expense in enumerate(expenses, start=1):
        for col, value in enumerate(expense[1:], start=0):
            Label(view_window, text=value).grid(row=index, column=col)
        
    conn.close()
    
def update_expense():
    window_update = Toplevel(root)
    window_update.title('Update Expense')
    window_update.geometry("400x300")

    # Connect to the database
    conn = sqlite3.connect('expense_tracker.db')
    cou = conn.cursor()

    # Retrieve data for the expense with the given ID
    id = get_expense_id_somehow()
    if id != 0:
        cou.execute('SELECT * FROM expenses WHERE id = ?', (id,))
        expense_data = cou.fetchone()
    else: 
        pass

    Label(window_update, text="Date:").pack()
    date_entry = Entry(window_update)
    date_entry.pack()
    date_entry.insert(0, expense_data[1])

    Label(window_update,  text="Name:").pack()
    name_entry = Entry(window_update)
    name_entry.pack()
    name_entry.insert(0, expense_data[2])

    Label(window_update, text="Category:").pack()
    category_entry = Entry(window_update)
    category_entry.pack()
    category_entry.insert(0, expense_data[3])

    Label(window_update, text="Description:").pack()
    description_entry = Entry(window_update)
    description_entry.pack()
    description_entry.insert(0, expense_data[4])


    Label(window_update, text="Amount:").pack()
    amount_entry = Entry(window_update)
    amount_entry.pack()
    amount_entry.insert(0, expense_data[5])

    def update_button_click():
        update_date = date_entry.get()
        update_name = name_entry.get()
        update_category = category_entry.get()
        update_description = description_entry.get()
        update_amount = amount_entry.get()

        updateExpense(update_date, update_name, update_category, update_description, update_amount, id)
        window_update.destroy()

    update_button = Button(window_update, text = "Update Expense", command=update_button_click, font=('Noto Sans CJK TC', 10, 'bold'), bg=hlb_btn_bg)
 
    update_button.pack()



def get_expense_id_somehow():
    expense_id = sd.askinteger("Expense ID", "Enter the ID of the expense to update:")
    return expense_id if expense_id is not None else 0

def update_button_clicked():
    id = get_expense_id_somehow()  
    update_expense(id)

def delete_expense():
    id = get_expense_id_somehow()
    if id is not None:
        deleteExpense(id)
        
root = Tk()
root.title("Personal Expense Tracker")
root.geometry('700x550')
root.resizable(0, 0)

hlb_btn_bg = 'DarkSalmon'
btn_font = ('Gill Sans MT', 13)


date_label = Label(root, text='Date:', font=('Noto Sans CJK TC', 10, 'bold'), bg=hlb_btn_bg)
date_label.grid(column=0, row=0, padx=20, pady=10)

date_entry = Entry(root)
date_entry.grid(column=1, row=0, padx=20, pady=20)

name_label = Label(root, text='Name:', font=('Noto Sans CJK TC', 10, 'bold'), bg=hlb_btn_bg)
name_label.grid(column=0, row=1, padx=20, pady=10)

name_entry = Entry(root)
name_entry.grid(column=1, row=1, padx=20, pady=10)


category_label = Label(root, text='Category:', font=('Noto Sans CJK TC', 10, 'bold'), bg=hlb_btn_bg)
category_label.grid(column=0, row=2, padx=20, pady=10)

category_entry = Entry(root)
category_entry.grid(column=1, row=2, padx=20, pady=10)


description_label = Label(root, text='Descriptions:', font=('Noto Sans CJK TC', 10, 'bold'), bg=hlb_btn_bg)
description_label.grid(column=0, row=3, padx=20, pady=10)

description_entry = Entry(root)
description_entry.grid(column=1, row=3, padx=20, pady=10)


amount_label = Label(root, text='Amount:', font=('Noto Sans CJK TC', 10, 'bold'), bg=hlb_btn_bg)
amount_label.grid(column=0, row=4, padx=20, pady=10)

amount_entry = Entry(root)
amount_entry.grid(column=1, row=4, padx=20, pady=10)

add_button = Button(root, text='Add Expense', command=add_expense_button_cliked, font=btn_font, width=11, bg=hlb_btn_bg)
add_button.grid(column=0, row=5, padx=20, pady=10)

view_button = Button(root, text="View Expenses", command=view_expense, font=btn_font, width=13, bg=hlb_btn_bg)
view_button.grid(column=1, row=5, padx=20, pady=10)

update_button = Button(root, text="Update Expenses", command=update_expense, font=btn_font, width=15, bg="black", fg="white")
update_button.grid(column=2, row=5, padx=20, pady=10)

update_button = Button(root, text="Delete Expenses", command=delete_expense, font=btn_font, width=15, bg="black", fg="white")
update_button.grid(column=3, row=5, padx=20, pady=10)

root.mainloop()
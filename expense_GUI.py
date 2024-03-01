from tkinter import *
from expense_tracker import add_expense


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


root = Tk()
root.title("Personal Expense Tracker")
root.geometry('400x300')


date_label = Label(root, text='Date:')
date_label.pack()

date_entry = Entry(root)
date_entry.pack()

name_label = Label(root, text='Name:')
name_label.pack()

name_entry = Entry(root)
name_entry.pack()


category_label = Label(root, text='Category:')
category_label.pack()

category_entry = Entry(root)
category_entry.pack()


description_label = Label(root, text='Descriptions:')
description_label.pack()

description_entry = Entry(root)
description_entry.pack()


amount_label = Label(root, text='Amount:')
amount_label.pack()

amount_entry = Entry(root)
amount_entry.pack()

add_button = Button(root, text='Add Expense', command=add_expense_button_cliked)
add_button.pack()

root.mainloop()
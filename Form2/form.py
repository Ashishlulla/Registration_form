import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb
from csv import DictWriter
import webbrowser


window = tk.Tk()
window.title("Sai Santosh Travels")
window.geometry("600x300")

label_frame = ttk.LabelFrame(window, text="Welcome to Sai Santosh Travels ")
label_frame.pack(side=tk.TOP, pady=20)

# Creating Labels

name_label = ttk.Label(label_frame, text="Name : ")
name_label.grid(row=1, column=0, pady=2, sticky=tk.W)

age_label = ttk.Label(label_frame, text="Age : ")
age_label.grid(row=2, column=0, pady=2, sticky=tk.W)

gender_label = ttk.Label(label_frame, text="Gender : ")
gender_label.grid(row=3, column=0, pady=4, sticky=tk.W)

phone_label = ttk.Label(label_frame, text="Contact : ")
phone_label.grid(row=4, column=0, pady=4, sticky=tk.W, )

address_label = ttk.Label(label_frame, text="Address : ")
address_label.grid(row=5, column=0, pady=4, sticky=tk.W)

from_label = ttk.Label(label_frame, text="From : ")
from_label.grid(row=6, column=0, padx=4, pady=4, sticky=tk.W)

to_label = ttk.Label(label_frame, text="To : ")
to_label.grid(row=7, column=0, padx=4, pady=4, sticky=tk.W)

# Creating Entry
name_var = tk.StringVar()
name_Box = ttk.Entry(label_frame, textvariable=name_var, width=20)
name_Box.grid(row=1, column=1, padx=4, pady=4)

age_var = tk.StringVar()
age_Box = ttk.Entry(label_frame, width=20, textvariable=age_var)
age_Box.grid(row=2, column=1, padx=4, pady=4)

gender_var = tk.StringVar()
gender_Box = ttk.Entry(label_frame, width=20, textvariable=gender_var)
gender_Box.grid(row=3, column=1, padx=4, pady=4)

phone_var = tk.StringVar()
phone_Box = ttk.Entry(label_frame, width=20,  textvariable=phone_var)
phone_Box.grid(row=4, column=1, padx=4, pady=4)

address_var = tk.StringVar()
address_Box = ttk.Entry(label_frame, width=20,  textvariable=address_var)
address_Box.grid(row=5, column=1, padx=4, pady=4)

# Create ComboBox
from_var = tk.StringVar()
from_var.set('Dhule')
from_Entry = ttk.Entry(label_frame, width=17,textvariable=from_var, state='readonly')
from_Entry.grid(row=6, column=1, padx=4, pady=4, sticky=tk.W)

to_var = tk.StringVar()
to_city = ('Dhule', 'Mumbai', 'Nashik', 'Aurangabad', 'Pune')
to_Combo = ttk.Combobox(label_frame, width=17, textvariable=to_var, state='readonly')
to_Combo['values'] = to_city
to_Combo.current(2)
to_Combo.grid(row=7, column=1, padx=4, pady=4, sticky=tk.W)

# Check Button:
check_var = tk.IntVar()
check_btn = tk.Checkbutton(label_frame, text='Booking cannot be reversed !')
check_btn.grid(row=8, columnspan=2, sticky=tk.W)


#  Create Button

def submit():
    name = name_var.get()
    age = age_var.get()
    gender = gender_var.get()
    phone = phone_var.get()
    address = address_var.get()
    start = from_var.get()
    end = to_var.get()
    check = check_var.get()
    if start == end:
        mb.showwarning('Warning', 'You cannot select same cities!!!')
    elif check == 1:
        mb.showwarning('Warning', 'Mandatory to accept Condition!')
    else:
        with open('file1.csv', 'a') as f:
            f_writer = DictWriter(f, fieldnames=['Name', 'Age', 'Gender', 'Phone', 'Address', 'From', 'To', 'Check'])
            f_writer.writeheader()
            f_writer.writerow({
                'Name': name,
                'Age': age,
                'Gender': gender,
                'Phone': phone,
                'Address': address,
                'From': start,
                'To': end,
                'Check': check,
            })


book = ttk.Button(label_frame, text='Book My Trip', command=submit)
book.grid(row=9, column=1, sticky=tk.W)


def call_back(url):
    webbrowser.open_new_tab(url)


link = tk.Label(window, text='Click Me', fg='Blue')
link.pack(side=tk.TOP)
link.bind("<Button-1>", lambda e: call_back('http://www.google.com'))
window.mainloop()

window.mainloop()

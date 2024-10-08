import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkinter import *


def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        
       
        dob = datetime(year, month, day)
        
       
        today = datetime.now()
        
        
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        
        messagebox.showinfo("Age", f"You are {age} years old.")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid date, month, and year.")


root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")


label_day = tk.Label(root, text="Day:")
label_day.pack(pady=5)
entry_day = tk.Entry(root)
entry_day.pack(pady=5)

label_month = tk.Label(root, text="Month:")
label_month.pack(pady=5)
entry_month = tk.Entry(root)
entry_month.pack(pady=5)

label_year = tk.Label(root, text="Year:")
label_year.pack(pady=5)
entry_year = tk.Entry(root)
entry_year.pack(pady=5)


calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)


root.mainloop()

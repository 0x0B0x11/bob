#!/bin/python3
# ================================================ Загружка библиотек
from tkinter import *
from tkinter import ttk
import re
 
def is_valid(newval):
    return re.match("^\+\d{0,11}$", newval) is not None
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
check = (root.register(is_valid), "%P")
 
phone_entry = ttk.Entry(validate="key", validatecommand=check) 
phone_entry.pack(padx=5, pady=5, anchor=NW)
 
root.mainloop()
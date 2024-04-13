from tkinter import *
from random import randint
import pyperclip  # for clipboard operations

root = Tk()
root.title("Password Generator")
root.geometry("500x300")

def new_rand():
    try:
        # Get desired password length from the entry
        length = int(myentry.get())
        
        # Generate a random password of the desired length
        password = ''.join(chr(randint(33, 126)) for _ in range(length))
        
        # Update the password entry widget with the generated password
        pw_entry.delete(0, END)
        pw_entry.insert(0, password)
    except ValueError:
        # Handle non-integer input in myentry
        pw_entry.delete(0, END)
        pw_entry.insert(0, "Invalid Input")

def copy():
    # Copy the password to the clipboard
    password = pw_entry.get()
    pyperclip.copy(password)

# Label for instruction
lf = Label(root, text="How many Characters?")
lf.pack(pady=20)

# Entry Box for number of characters
myentry = Entry(root, font=("Arial", 25))
myentry.pack(padx=20, pady=20)

# Entry Box to display the generated password
pw_entry = Entry(root, font=("Arial", 25))
pw_entry.pack(pady=20)

# Frame for buttons
myframe = Frame(root)
myframe.pack(pady=20)

# Create buttons
my_button = Button(myframe, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

copy_button = Button(myframe, text="Copy to Clipboard", command=copy)
copy_button.grid(row=0, column=1, padx=10)

root.mainloop()
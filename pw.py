import random
import string
import pyperclip
from tkinter import *


win = Tk()
win.geometry("400x500")  
win.resizable(False, False) # Disable resizing window
win.overrideredirect(True) # Prevent from using toolbar
#win.eval('tk::PlaceWindow  .  center') # Centers the window
win.title("Python Password Generator")
win.configure(bg='skyblue')

output_pass = StringVar()
include_special = BooleanVar()  # Variable to store the state of the checkbox

# Disable the exit [X]
def disable_event():
    pass

def update_all_combi():
    special_chars = string.punctuation if include_special.get() else ""
    return [
        string.ascii_uppercase,
        string.digits,
        string.ascii_lowercase,
        special_chars
    ]

all_combi = update_all_combi()  # Initial list of all possible characters

def randPassGen():
    global all_combi  # Ensure we use the global variable
    all_combi = update_all_combi()  # Update the all_combi list based on the checkbox state
    
    password = ""
    for _ in range(pass_len.get()):
        char_type = random.choice(all_combi)
        if char_type:
            password += random.choice(char_type)
    output_pass.set(password)

# ---- Copy to clipboard function
def copyPass():
    pyperclip.copy(output_pass.get())
    output_pass.set("")  # Clear the output_pass variable

# ----- exit the program
def close():
    win.quit()

# ----- Front-end Designing (GUI)
pass_title = Label(win, text='Python Password Generator', font='arial 18 bold', bg='aliceblue').pack(pady=10)

pass_head = Label(win, text='Password Length', font='arial 14 bold', bg='skyblue').pack(pady=10)
pass_len = IntVar()
length = Spinbox(win, from_=10, to_=40, textvariable=pass_len, width=3, font='arial 16', bg='aliceblue').pack()

# Checkbox for including special characters
special_checkbox = Checkbutton(win, text="Include Special Characters", font='arial 10 bold', bg='skyblue', variable=include_special)
special_checkbox.pack(pady=10)

# ----- Generate password button
Button(win, text="Generate Password", command=randPassGen, font='Arial 10 bold', bg='skyblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

pass_label = Label(win, text='Random Generated Password', bg='skyblue', font='arial 14 bold').pack(pady="30 10")
Entry(win, textvariable=output_pass, width=24, font='arial 16', bg='aliceblue').pack()

# Copy to clipboard button
Button(win, text='Copy to Clipboard', command=copyPass, font='Arial 10 bold', bg='skyblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

# ------ exit button
Button(win, text="Exit", command=close, font='Arial 10', bg='skyblue', fg='black').pack(pady=30)


win.protocol ("WM_DELETE_WINDOW", disable_event)

win.mainloop()

import tkinter as tk
import math

# Function to update the text in the entry widget
def button_click(item):
    current = entry_text.get()
    entry_text.set(current + str(item))

# Function to clear the entry widget
def button_clear():
    entry_text.set("")

# Function to calculate the expression
def button_equal():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except Exception as e:
        entry_text.set("Error")

# Function to perform addition
def add():
    button_click("+")

# Function to perform subtraction
def subtract():
    button_click("-")

# Function to perform multiplication
def multiply():
    button_click("*")

# Function to perform division
def divide():
    button_click("/")

# Function to calculate modulo
def modulo():
    button_click("%")

# Function to calculate square root
def square_root():
    try:
        result = str(math.sqrt(float(entry_text.get())))
        entry_text.set(result)
    except Exception as e:
        entry_text.set("Error")

# Function to calculate reciprocal
def reciprocal():
    try:
        result = str(1 / float(entry_text.get()))
        entry_text.set(result)
    except Exception as e:
        entry_text.set("Error")

# Function to calculate square
def square():
    try:
        result = str(float(entry_text.get()) ** 2)
        entry_text.set(result)
    except Exception as e:
        entry_text.set("Error")

# Function to calculate logarithm (natural log)
def logarithm():
    button_click("math.log()")
    entry.icursor(entry.index(tk.INSERT) - 2)

# Function to calculate exponential
def exponential():
    button_click("math.exp()")
    entry.icursor(entry.index(tk.INSERT) - 2)

# Function to calculate sine
def sine():
    button_click("math.sin(")

# Initialize the main window
window = tk.Tk()
window.title("Calculator")

# Set default window size to medium
window.geometry("400x600")

# Function to exit fullscreen mode on pressing Escape key
def exit_fullscreen(event):
    window.attributes('-fullscreen', False)

# Bind the Escape key to the exit_fullscreen function
window.bind("<Escape>", exit_fullscreen)

# Configure grid to expand with window size
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# Frame to contain the calculator layout
frame = tk.Frame(window)
frame.grid(sticky="nsew")

# Configure frame grid to handle resizing
for i in range(6):
    frame.rowconfigure(i, weight=1)
    frame.columnconfigure(i, weight=1)

# Entry widget to display the expressions and results
entry_text = tk.StringVar()
entry = tk.Entry(frame, textvariable=entry_text, font=('Arial', 24), bd=10, insertwidth=2, borderwidth=4)
entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

# Button layout
buttons = [
    ('C', button_clear),('=', button_equal),('+', add), ('-', subtract),('*', multiply),
    ('/', divide), ('%', modulo), ('sqrt', square_root), ('1/x', reciprocal), ('x²', square),
    ('log', logarithm), ('4', lambda: button_click('4')),  ('3', lambda: button_click('3')), ('2', lambda: button_click('2')), 
    ('1', lambda: button_click('1')), ('7', lambda: button_click('7')), ('8', lambda: buttton_click('8')),('9', lambda: button_click('9')),  ('0', lambda: button_click('0'))
]

# Place buttons on the window
row = 1
col = 0
for (text, func) in buttons:
    tk.Button(frame, text=text, width=5, height=2, font=('Arial', 18), command=func).grid(row=row, column=col, sticky="nsew")
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main loop

window.mainloop()
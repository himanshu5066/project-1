import tkinter as tk


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

# Initialize the main window
window = tk.Tk()
window.title("Calculator")

# Make the window fullscreen
window.attributes('-fullscreen', True)

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
for i in range(5):
    frame.rowconfigure(i, weight=1)
    frame.columnconfigure(i, weight=1)

# Entry widget to display the expressions and results
entry_text = tk.StringVar()
entry = tk.Entry(frame, textvariable=entry_text, font=('Arial', 24), bd=10, insertwidth=2, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Place buttons on the window
row = 1
col = 0
for button in buttons:
    if button == "=":
        tk.Button(frame, text=button, width=5, height=2, font=('Arial', 18), command=button_equal).grid(row=row, column=col, columnspan=2, sticky="nsew")
        col += 1  # Adjust column for = sign taking up two columns
    elif button == "C":
        tk.Button(frame, text=button, width=5, height=2, font=('Arial', 18), command=button_clear).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(frame, text=button, width=5, height=2, font=('Arial', 18), command=lambda b=button: button_click(b)).grid(row=row, column=col, sticky="nsew")
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main loop
window.mainloop()
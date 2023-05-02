# Simple Pocket calculator with GUI (Tkinter)
# It accepts two inputs; Where you choose to perform either of the follwing operations:
# Additiom
# Subtraction
# Multiplication
# Division

import tkinter as tk 
from tkinter import messagebox


def valuechecker(parameter):  
    """Gets value 
    Convert to float if possible;
    Returns the float value
    """
    
    value = parameter.get()
    try:
        float_value = float(value)
    except ValueError:
        return None
    return float_value
                
def are_you_sure():
    if messagebox.askokcancel("Quit App?","Are you sure you want to quit?"):
        window.destroy()
    
def evaluate():
    """Evaluates the type of operation to process"""
    
    value_1 = valuechecker(entry_1)  # Checks if value in entry widget 1 is valid  
    if value_1 == None:
        messagebox.showerror("Parameter 1", "Invalid input!")
        entry_1.focus_get()    # place focus on entry_1 widget  
        return
            
    value_2 = valuechecker(entry_2) # Checks if value in entry widget 2 is valid 
    if value_2 == None: 
        messagebox.showerror("Parameter 2", "Invalid input!")
        entry_2.focus_get()
        return
        
    operation = intvar.get()  # Get number assigned to operations
    if operation == 3 and value_2 == 0: # Check if operation is division and value2 is zero
        messagebox.showerror("", "cannot divide by zero!") # Display error if dividing by zero
        entry_2.focus_get()
        return
        
    if operation == 0: # Check if operation is addition
        result = round(value_1 + value_2, 8)
    elif operation == 1: # Check if operation is subtraction
        result = round(value_1 - value_2, 8)
    elif operation == 2: # Check if operation is multiplication
        result = round(value_1 * value_2, 8)
    else:
        result = round(value_1 / value_2, 8)
    messagebox.showinfo("", "The result is " + str(result))
    
# Sets up master window
value = ""
window = tk.Tk()
window.title("Simple pocket calculator")
window.geometry("310x130") # Set default window size
window.resizable(width=False, height=False) # Restrict user from resizing master window
window.protocol("WM_DELETE_WINDOW", are_you_sure) # Bind mmaster window to are_you_sure callback

# Sets up the first entry widget
stringvar_1 = tk.StringVar()
entry_1 = tk.Entry(window, width=20, textvariable=stringvar_1)
stringvar_1.set(value)
entry_1.grid(row=0, column=0)
entry_1.focus_set()

# Sets up radio buttons (all inside a frame) for selecting operation type
frame = tk.Frame(window)
intvar = tk.IntVar()
intvar.set(0)
radiobutton_1 = tk.Radiobutton(frame, variable=intvar, text="+", value=0)
radiobutton_1.pack()
radiobutton_2 = tk.Radiobutton(frame, variable=intvar, text="-", value=1)
radiobutton_2.pack()
radiobutton_3 = tk.Radiobutton(frame, variable=intvar, text="x", value=2)
radiobutton_3.pack()
radiobutton_4 = tk.Radiobutton(frame, variable=intvar, text="/", value=3)
radiobutton_4.pack()
frame.grid(row=0, column=1)

# Sets up the second entry widget
stringvar_2 = tk.StringVar()
entry_2 = tk.Entry(window, width=20, textvariable=stringvar_2)
stringvar_2.set(value)
entry_2.grid(row=0, column=2)

# Button binded to evaluate
button = tk.Button(window, text="evaluate", command=evaluate)
button.grid(row=1, column=1)
window.mainloop()
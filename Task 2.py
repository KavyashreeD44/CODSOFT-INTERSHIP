# Python program to create a simple GUI 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *

# globally declare the expression variable 
expression = "" 

# Function to update expression 
# in the text entry box 
def press(num): 
    global expression 
    expression += str(num) 
    equation.set(expression) 

# Function to evaluate the final expression 
def equalpress(): 
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except: 
        equation.set(" error ") 
        expression = "" 

# Function to clear the contents 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 

# Driver code 
if __name__ == "__main__": 
    gui = Tk() 
    gui.configure(background="#f0f0f0")  # Set a light grey background
    gui.title("Simple Calculator") 
    gui.geometry("300x300") 

    equation = StringVar() 
    expression_field = Entry(gui, textvariable=equation, font=('Arial', 14), bd=10, insertwidth=2, width=14, borderwidth=4)
    expression_field.grid(columnspan=4, ipadx=8)

    button_color = "#ffcc00"  # Set button color

    # Create buttons
    buttons = [
        ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('+', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
        ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('*', 4, 3),
        ('0', 5, 0), ('.', 6, 0), ('/', 5, 3), ('=', 5, 2),
        ('Clear', 5, 1)
    ]

    for (text, row, column) in buttons:
        if text == '=':
            Button(gui, text=text, fg='black', bg=button_color, command=equalpress, height=2, width=7).grid(row=row, column=column)
        elif text == 'Clear':
            Button(gui, text=text, fg='black', bg=button_color, command=clear, height=2, width=7).grid(row=row, column=column)
        else:
            Button(gui, text=text, fg='black', bg=button_color, command=lambda num=text: press(num), height=2, width=7).grid(row=row, column=column)

    gui.mainloop()

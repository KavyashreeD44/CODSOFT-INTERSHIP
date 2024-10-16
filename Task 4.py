# importing the required libraries and modules  
from tkinter import *  
import random  

# creating the GUI for the application  
guiWindow = Tk()  
guiWindow.title("The Rock Paper Scissors Game")  
guiWindow.geometry("480x480")  
guiWindow.config(bg="#2E8B57")  # Change to a green background
guiWindow.resizable(width=False, height=False)  

# adding a label to the window using the Label() widget  
heading = Label(  
    guiWindow,  
    text='Let\'s play Rock Paper Scissors',  
    font='arial 18 bold',  
    bg='#2E8B57',  # Match with the background
    fg='white'  
).pack()  

# creating column for user selection  
userInput = StringVar()  

subHeading = Label(  
    guiWindow,  
    text='Select any ONE from rock, paper, scissors',  
    font='calibri 14 bold',  
    bg='#66CDAA',  # Light sea green for the subheading
    fg='black'  
).place(  
    x=35,  
    y=110  
)  

Entry(  
    guiWindow,  
    font='calibri 14',  
    textvariable=userInput,  
    bg='#F0FFF0',  # Honeydew for entry box
    fg='black'  
).place(  
    x=110,  
    y=160  
)  

# creating function to begin the game  
res = StringVar()  

def letsPlay():  
    compSelection = random.choice(['rock', 'paper', 'scissors'])  # Randomly select computer's choice
    userSelection = userInput.get().lower()  # Get user input and convert to lowercase
    if userSelection == compSelection:  
        res.set("It's a Tie! You made the same choice as the computer.")  
    elif userSelection == 'rock' and compSelection == 'paper':  
        res.set("Oops! You Lose. Computer selected Paper.")  
    elif userSelection == 'rock' and compSelection == 'scissors':  
        res.set("Congrats! You Win. Computer selected Scissors.")  
    elif userSelection == 'paper' and compSelection == 'scissors':  
        res.set("Oops! You Lose. Computer selected Scissors.")  
    elif userSelection == 'paper' and compSelection == 'rock':  
        res.set("Congrats! You Win. Computer selected Rock.")  
    elif userSelection == 'scissors' and compSelection == 'rock':  
        res.set("Oops! You Lose. Computer selected Rock.")  
    elif userSelection == 'scissors' and compSelection == 'paper':  
        res.set("Congrats! You Win. Computer selected Paper.")  
    else:  
        res.set("Invalid input! Please select - rock, paper, or scissors.")  

# defining a function to reset the game  
def resetGame():  
    res.set("")  
    userInput.set("")  

# defining a function to exit the game  
def exitGame():  
    guiWindow.destroy()  

displayResult = Label(  
    guiWindow,  
    textvariable=res,  
    font='calibri 12 bold',  
    bg='#66CDAA',  # Light sea green for result display
    fg='black'  
).place(  
    x=20,  
    y=240  
)  

playButton = Button(  
    guiWindow,  
    font='calibri 10 bold',  
    text='PLAY',  
    padx=5,  
    bg='#FFD700',  # Gold for play button
    fg='black',  
    command=letsPlay  
).place(  
    x=100,  
    y=300  
)  

resetButton = Button(  
    guiWindow,  
    font='calibri 10 bold',  
    text='RESET',  
    padx=5,  
    bg='#FFD700',  # Gold for reset button
    fg='black',  
    command=resetGame  
).place(  
    x=200,  
    y=300  
)  

exitButton = Button(  
    guiWindow,  
    font='calibri 10 bold',  
    text='EXIT',  
    padx=5,  
    bg='#FFD700',  # Gold for exit button
    fg='black',  
    command=exitGame  
).place(  
    x=300,  
    y=300  
)  

guiWindow.mainloop()  

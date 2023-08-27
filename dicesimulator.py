from tkinter import *
import random

# Defining a GUI window
root = Tk()
root.geometry("644x344")
root.title("Dice Simulator-Bhumi Dahiya")

# Defining a function to get a random dice's output when it's rolled
def roll_dice():
    return random.choice(l)

# Defining a function to return the output for all the dices
def num_dice(number_of_dice):
    return [roll_dice() for i in range(number_of_dice)]

# Defining a function to print the result of dices rolled in the text widget of GUI
def printdata():
    result = print_result()
    text.insert(END, "\n" + result)
    save(result)

# Defining a function to save outputs in a file
def save(result):
    with open("outputs.txt", "a") as f:
        f.write(result)

# Defining a function to print the result of dices rolled in the text widget of GUI
def print_result():
    number_of_dice = int(entry.get())
    dice_values = num_dice(number_of_dice)
    result = ""
    for i, value in enumerate(dice_values):
        result += f"Dice{i+1}: {value}\n"
    return result

# Creating an entry widget
var = IntVar()
entry = Entry(root, textvariable=var)
entry.pack(pady=10)

# Creating a scrollbar attached with text widget
scrollbar = Scrollbar(root, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

# Creating text widget
text = Text(root, width=100, height=50, background="floral white", font=("Helvetica 18 "), yscrollcommand=scrollbar.set)
text.pack(padx=18, pady=18)

scrollbar.config(command=text.yview)

# Creating button to save the data in a file
Button(root, text="save", width=7, height=1, font="Helvetica 19 bold", command=save).pack(padx=10, pady=7)

# Creating button for execution of printdata function
Button(root, text="Roll", width=7, height=1, font=("Arial 12 bold"), activebackground="grey", command=printdata).pack(padx=10, pady=7)

# This list is an analogy of a dice's outputs
l = ["one", "two", "three", "four", "five", "six"]

root.mainloop()
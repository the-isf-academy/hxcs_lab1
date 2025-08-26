# /////////// INSTRUCTIONS /////////////////

# Run this program. How does it change based on your input? 

# 🤔 Can you make any changes to the program so that it can draw a square of size that the user entered?

# 💡 Hint: make use of forward(length) and right(90)

# ❗️ How about other shapes like a triangle or a rectangle? 

# ////////////////////////////////////////////

# Don't delete this line! 
from turtle import *

# This line takes the user input
length = int(input('Enter a number: '))

# This line makes the turtle go forward as long as what the user entered
forward(length)

# This line makes the program wait until the user types something on the keyboard
input("Type any key to close the program.")

# Kerman Rodriguez
# 04/06/2025
# This program will practice library files and functions from these files

# When you import like this you must use math. When callin a function
import math

# Another way to import is this - it will load the function into the interpreter
# from math import sqrt, pi, ceil, floor

# This way - using the * - will load all functions from the library file
# from math import *

import random # Library for randint() and randrange()

# from lab10_myLibrary import displayIntro

# This is shorthand or alias
# import lab10_myLibrary as ml
from lab10_myLibrary import displayIntro as ml
from lab10_myLibrary import sales_price_calc


from time import sleep

def main():

    num1 = num2 = num3 = 0

    #Display intro
    ml()
    print("\n")

    sleep(1) # fractions of a second
    
    # Prompt for a number
    num1 = int(input("Enter a number to see the square root: \n"))

    print("Here coms your answer....")
    sleep(.75)
    
               
    # Display square root of the number
    print(f"The square rrot of your number {num1} is {math.sqrt(num1)}\n")
    

    for name in dir(math):
        print(name, end = ", ")
    print("\n")

    print(math.pi)
    print("\n")

    # Python has a built in round function
    print(round(3.14))
    print(round(3.74))
    print(round(3.141592,3))
    print("\n")

    # The floor function forces a round down, it is part of the math library
    print(math.floor(3.74))
    print("\n")

    # The ceil function forces a round up
    print(math.ceil(3.74))
    print("\n")


    num2 = random.randint(1,100)    # 1 to 100
    num3 = random.randrange (1,101) # also from 1 to 100, not including the last

    print(num2, num3)
    print("\n")

    # On Your own:
    # Create a function on our lab10_myLibrary file that takes 1 float as a formal parameter
    # and prompts for some kind of input, does some kind of calculation with the parameter and the prompt,
    # and produces some output - nothing we have done before - MUST BE UNIQUE

    # Call and use that function here in this file passing it num1 as an argument
    # Add comments around your new code in both files so I know what you did and why

    sales_price_calc(num1) # Call the function from the library file





main()





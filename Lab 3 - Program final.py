# Kerman Rodriguez
# 02/10/2025
# This program calculates the number of claories consumed by a cutomer
# based on th enumber of cookies the customer ate.


# Define main function
# Functions are containers for your code
# Later in this course we will devide our code into several small manageable chunks or functions
# in Python all code must be indented inside a function

def main():
    #Declare a constant
    # each cookie is 75 calories
    CALORIES_PER_COOKIE = 70
    # add a constant to store 300 calories in a soda
    CALORIES_PER_SODA = 300

    # Declare and initialize variables
    # String var for name
    userName = ""
    # Whole number var for cookies eaten, calories consumed
    # add a variable for sodaConsumed
    cookiesEaten = caloriesConsumed = sodaConsumed = 0

    # userName, cookiesEaten = "", 0 # another whay

    # numFloat = 0.0

    # Display "WELCOME TO THE CALORIE COUNTER!!"
    print("WELCOME TO THE CALORIE COUNTER!!\n")

    # Prompt for name by displaying "Please enter your name:"
    userName = input("Please enter your name: ") #Bob
    # Prompt for cookies eaten by displaying "Please enter the number of cookies consumed:"
    # Written like this the imput function executes first and return the "4" (e.g.) as a string
    # The string "4" is passed to the function and it return the integer 4
    # cookiesEaten = input("Please enter the number of cookies consumed: ") # "4" will save a string
    # cookiesEaten = int(input("Please enter the number of cookies consumed: ")) # but it will restrict to a integer
    # cookiesEaten = int(input("Hi ", userName, "Please enter the number of cookies consumed: "))
    # Using concantenation would work if the variable stores string, but.... no fun
    # cookiesEaten = int(input("Hi " + unserName + "Please enter the number of cookies consumed: ")) # old way
    # This is why f formating is so nice - no need to concatenate
    cookiesEaten = int(input(f"\nHi {userName}, \nPlease enter the number of cookies consumed: "))
    # ask the user how many sodas they drank
    sodaConsumed = int(input(f"Now, please enter how many sodas you drank: "))
                       


    # We could type cast in a whole 2nd step or in the math - but...
    # cookiesEaten = int(cookieEaten) "4" -> 4

    # Converting to an int here only does it for this moment in time
    # Does not change what is stored in the var
    # caloriesConsumed = int(cookiesEaten) * 75
    # print(f"\nOkay {userName}, you consumed {caloriesConsumed} Calories!")


    # Calculate calories consumed = cookies eaten * 75 calories per cookie
    caloriesConsumed = (cookiesEaten * CALORIES_PER_COOKIE)+(sodaConsumed * CALORIES_PER_SODA)

    # Display calories consumed calling user by name
    print(f"\nOkay {userName}, in total you consumed {caloriesConsumed} Calories!")
    print(f"{cookiesEaten * CALORIES_PER_COOKIE} calories from cookies\n{sodaConsumed * CALORIES_PER_SODA} calories from sodas")

    # Display outro
    print("\nThank you for using my program!")

# Call or invoke the main function
main ()

# ---Try this on your own--- Put these steps in the appropiate places above so the program makes sense and add the code under each step
# add a constant to store 300 calories in a soda
# add a variable for sodaConsumed
# ask the user how many sodas they drank
# calculate how many calories they drank
# display total calories consumed which is cookies calories plus soda calories


# Add another

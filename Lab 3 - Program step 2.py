# Kerman Rodriguez
# 02/10/2025
# This program calculates the number of claories consumed by a cutomer
# based on th enumber of cookies the customer ate.

# Display "WELCOME TO THE CALORIE COUNTER!!"
print("WELCOME TO THE CALORIE COUNTER!!")

# Prompt for name by displaying "Please enter your name:"
userName = input("Please enter your name: ") #Bob
# Prompt for cookies eaten by displaying "Please enter the number of cookies consumed:"
# Written like this the imput function executes first and return the "4" (e.g.) as a string
# The string "4" is passed to the function and it return the integer 4
#cookiesEaten = input("Please enter the number of cookies consumed: ") # "4" will save a string
cookiesEaten = int(input("Please enter the number of cookies consumed: ")) # but it will restrict to a integer


# We could type cast in a whole 2nd step or in the math - but...
# cookiesEaten = int(cookieEaten) "4" -> 4

# Converting to an int here only does it for this moment in time
# Does not change what is stored in the var
# caloriesConsumed = int(cookiesEaten) * 75
# print(f"\nOkay {userName}, you consumed {caloriesConsumed} Calories!")


# Calculate calories consumed = cookies eaten * 75 calories per cookie
caloriesConsumed = cookiesEaten * 75

# Display calories consumed calling user by name
print(f"\nOkay {userName}, you consumed {caloriesConsumed} Calories!")

# Display outro


# Kerman Rodriguez
# 02/10/2025
# This program calculates the number of claories consumed by a cutomer
# based on th enumber of cookies the customer ate.

# Display "WELCOME TO THE CALORIE COUNTER!!"
print("WELCOME TO THE CALORIE COUNTER!!")

# Prompt for name by displaying "Please enter your name:"
userName = input("Please enter your name: ") #Bob
# Prompt for cookies eaten by displaying "Please enter the number of cookies consumed:"
cookiesEaten = input("Please enter the number of cookies consumed: ") # will save a string

# Calculate calories consumed = cookies eaten * 75 calories per cookie
caloriesConsumed = cookiesEaten * 75

# Display calories consumed calling user by name
print(f"\nOkay {userName}, you consumed {caloriesConsumed} Calories!")

# Display outro


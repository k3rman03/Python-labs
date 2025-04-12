# Kerman Rodriguez
# 02/23/2025
# This program finds an average of numbers entered by user
# This version uses a for loop

def main():
    # Initialize variables
    howManyNumbers = 0
    number = average = total = 0.0
    
    # Display intro
    print("Welcome to my average program!\n")
    
    # Prompt user for number of numbers
    howManyNumbers = int(input("How many numbers are there: "))
    
    # Use a counted loop to ask the use to enter the numbers for as many times
    # as they say they have numbers
    for i in range(howManyNumbers):
        # Prompt user for a number
        number = float(input("Please enter a number: "))
        total = total + number
        
    # Calculate the average
    average = total / howManyNumbers

    # Display average
    print(f"The average of your numbers is {average}")
    
    # Display outro
    print("\nThank, bye")

main()

    
# This version makes the user have to count the numbers in advance
# - not very user friendly


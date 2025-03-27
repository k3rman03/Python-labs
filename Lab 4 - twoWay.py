# Kerman Rodriguez
#02/16/2025
# Lab 4 - This program shows a two-way decision
# This program will display an insurance premium based on an age input

# Define main function
def main():
    # Declare constants for insurance premiums
    # $1000 for 40 or under, $000 for over 40
    # Cut off age of 40
    YOUNGINSCOST = 1000
    OLDINSCOST = 2000
    CUTTOFFAGE = 40
        
    # Declare and intialize string for name
    # and whole var for user age
    userName = ""
    userAge = 0
    
    # Display Intro
    print("Welcome to the Insurance Program\n")
          
    # Prompt for name
    userName = input("Please enter your name: ")
    # Prompt for age
    userAge = int(input(f"Hello {userName}, how old are you? "))
    
    # Display premium based on age
    # If the user 40 or under display the premium is $1000
    # If the user is over 40 display the premium is $2000
    # A 2 way decision has an if  and else only
    # Create a condition to be evaluated as tru or false
    # If the condition is tru the body of the if will execute
    # If the condition is not true the body of the else will execute
    # But only 1 or the other can execute, never both
    if userAge <= CUTTOFFAGE:
        print(f"\nYour insurance premium is ${YOUNGINSCOST}")
    else:
        print(f"\nYour insurance premium is ${OLDINSCOST}")


    # Display an outro
    print(f"\nThank you {userName} for your busniess!")

# Call or invoke the main function
main()



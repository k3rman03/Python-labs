# Kerman Rodriguez
#02/16/2025
# Lab 4 - This program shows a multi-way decision
# This program will display an insurance premium based on an age input

# Define main function
def main():
    # Declare constants for insurance premiums
    # $1000 for 35 or under, $1500 for 35 - 59, and $2000 for 60+
    # Cut off ages of 35 and 59
    YOUNGINSCOST = 1000
    MIDINSCOST = 1500
    OLDINSCOST = 2000
    CUTTOFFAGEYOUNG = 35
    CUTOFFAGEMID = 59
        
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
    # If the user 35 or under display the premium is $1000
    # If the user is 36 - 59 display the premium is $1500
    # If the user is over 59 display the premium is $2000
    # A multi-way decision has only 1 if, as many elif as needed,
    # and only 1 else
    # If the condition in the if is tru the body of the if will execute
    # If the condition in the if is not true the interpreter will move on to
    # the elif and check that condition
    # This will continue for as many elif as we have
    # The else will only execute if none of the conditions above it are true
    # Again only 1 can execute


    if userAge <= CUTTOFFAGEYOUNG:
        print(f"\nYour insurance premium is ${YOUNGINSCOST}")
    elif userAge <= CUTOFFAGEMID:
        print(f"\nYour insurance premium is ${MIDINSCOST}")
    else:
        print(f"\nYour insurance premium is ${OLDINSCOST}")


    # Display an outro
    print(f"\nThank you {userName} for your busniess!")

# Call or invoke the main function
main()



# Kerman Rodriguez
#02/16/2025
# Lab 4 - This program shows a multi-way decision. And a nested decision
# This program will display an insurance premium based on an age input

# Define main function
def main():
    # Declare constants for insurance premiums
    # $1000 for 35 or under, $1500 for 35 - 59, and $2000 for 60+
    # Cut off ages of 35 and 59
    YOUNGINSCOSTSMOKER = 2000
    YOUNGINSCOSTNONSMOKER = 1000
    MIDINSCOSTSMOKER = 2500
    MIDINSCOSTNONSMOKER = 1500
    OLDINSCOSTSMOKER = 3000
    OLDINSCOSTNONSMOKER = 2000
    CUTTOFFAGEYOUNG = 35
    CUTOFFAGEMID = 59
        
    # Declare and intialize string for name
    # and whole var for user age
    userName = smoker = ""
    userAge = 0
    
    # Display Intro
    print("Welcome to the Insurance Program\n")
          
    # Prompt for name
    userName = input("Please enter your name: ")
    # Prompt for age
    userAge = int(input(f"Hello {userName}, how old are you? "))
    # Prompt user if they smoke
    smoker = input("Do you smoke, yes or no? ") #yes
    
    
    # Display premium based on age
    # If the user 35 or under display the premium is $1000
    # If the user is 36 - 59 display the premium is $1500
    # If the user is over 59 display the premium is $2000
    # A nested decision is one decision in the body of the another
    # If the user is 35 or under
        # check to see if they smoke
        # if the user smokes display youngsmoker premium
        # if they do not smoke display the youngnonsmoker premium
    # Else If the user age is between 36 and 59 
        # check to see if they smoke
        # if the user smokes display midsmoker premium
        # if thet do not smoke display midnonsmoker premium
    # Otherwise they must be over 59
        # bue we still nee to check if they smoke
        # if the user smokes display oldsmoker premium
        # if they do not smoke display oldnonsmoker premium
        
    # This is the outher selection structure
    if userAge <= CUTTOFFAGEYOUNG:
        # This is an inner selection structure
        # == means equal to and is used for comparison
        if smoker == "yes":
            print(f"\nYour insurance premium is ${YOUNGINSCOSTSMOKER}")
        elif smoker == "no":
            print(f"\nYour insurance premium is ${YOUNGINSCOSTNONSMOKER}")
        else:
            print("You must enter yes or no")
    elif userAge <= CUTOFFAGEMID:
        if smoker == "yes":
            print(f"\nYour insurance premium is ${MIDINSCOSTSMOKER}")
        elif smoker == "no":
            print(f"\nYour insurance premium is ${MIDINSCOSTNONSMOKER}")
        else:
            print("You must enter yes or no")
    else:
        if smoker == "yes":
            print(f"\nYour insurance premium is ${OLDINSCOSTSMOKER}")
        elif smoker == "no":
            print(f"\nYour insurance premium is ${OLDINSCOSTNONSMOKER}")
        else:
            print("You must enter yes or no")

    # Display an outro
    print(f"\nThank you {userName} for your busniess!")

# Call or invoke the main function
main()



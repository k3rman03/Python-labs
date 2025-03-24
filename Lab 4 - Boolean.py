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
    # and whole var for user age and Household size
    userName = smoker = ""
    userAge = houseHold = 0
    
    # Display Intro
    print("Welcome to the Insurance Program\n")
          
    # Prompt for name
    userName = input("Please enter your name: ")

    # prompt yhe user for household size
    houseHold = int(input("Please enter the number of people in your household: "))

    # This is an outher decision and gets check first
    if houseHold >= 3:
        print("You can get a discount if you enroll all the members in your household")
    
    # Prompt for age
    userAge = int(input(f"Hello {userName}, how old are you? "))

    if userAge < 18:
        print("You must be 18 to buy insurance")
    else:    
        # Prompt user if they smoke
        smoker = input("Do you smoke, yes or no? ") #yes

        if smoker == "yes":
            print ("Wow, you should quit smoking!")
                
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
        if userAge <= CUTTOFFAGEYOUNG and smoker == "yes":
                print(f"\nYour insurance premium is ${YOUNGINSCOSTSMOKER:,.2f}") # $2,000.00
        elif userAge <= CUTTOFFAGEYOUNG and smoker == "no":
                print(f"\nYour insurance premium is ${YOUNGINSCOSTNONSMOKER:,.2f}")
        elif userAge <= CUTOFFAGEMID and smoker == "yes":
                print(f"\nYour insurance premium is ${MIDINSCOSTSMOKER:,.2f}")
        elif userAge <= CUTOFFAGEMID and smoker == "no":
                print(f"\nYour insurance premium is ${MIDINSCOSTNONSMOKER:,.2f}")
        elif userAge > CUTOFFAGEMID and smoker == "yes":
                print(f"\nYour insurance premium is ${OLDINSCOSTSMOKER:,.2f}")
        elif userAge > CUTOFFAGEMID and smoker == "no":
                print(f"\nYour insurance premium is ${OLDINSCOSTNONSMOKER:,.2f}")
        else:
            print("You must enter yes or no")

        # Display an outro
        print(f"\nThank you {userName} for your busniess!")

# Call or invoke the main function
main()

# Now add to the program above
# Before asking their age - prompt the user for number of people in household
# If the number of people is 3 or more, tell them they can get a discount on th insurance if they buy for everyone
# Otherwise, just continue on with the program


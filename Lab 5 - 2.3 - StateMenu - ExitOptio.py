# Kerman Rodriguez
# 02/23/2025
# This Program present an option with 4 possibles states
# then tells the capital of their choise

# Define main function
def main():
    # Declare and initialize variables
    # Strings for name and menuchoice
    userName = menuChoice = ""
    

    # Display Intro
    print("WELCOME TO THE CAPITAL PROGRAM!!\n")

    # Prompt for name
    userName = input("First, let me get your name: ")

           
    # Loop until the user types E
    while menuChoice != "E":
    # we use "and" because all of them toghether must be true for the loop to repeat
        # Display state options
        print("\nPlease choose from the following menu: ")
        print("A) PA \nB) SC \nC) GA \nD) FL \nE) Exit")

        # Prompt for menuchoice
        menuChoice = input("\nEnter your choice here: ")

        # Selection structure to determine which capital to display to user
        if menuChoice == "A" or menuChoice == "a" or menuChoice == "PA":
            print("The capital of Pennsylvania is Harrisburg")
        elif menuChoice == "B" or menuChoice == "b" or menuChoice == "SC":
            print("The capital of South Carolina is Columbia")
        elif menuChoice == "C" or menuChoice == "c" or menuChoice == "GA":
            print("The capital of Georgia is Atlanta")
        elif menuChoice == "D" or menuChoice == "d" or menuChoice == "FL":
            print("The capital of Florida is Tallahassee")
        elif menuChoice == "E":
            print("Sorry to see you go")
        else:
            print("Sorry, you must choose A, B, C, D or E.")

    


    # Display outro
    print(f"\nThank you {userName} for playing my state capitals game!")

# Call the main function
main()

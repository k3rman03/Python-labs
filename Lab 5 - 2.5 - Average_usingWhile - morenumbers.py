# Kerman Rodriguez
# 02/23/2025
# This program finds an average of numbers entered by user
# This version uses a conditional loop with two accumulators

def main():
    # Initialize variables
    moreNumbers = "yes"
    count = 0
    number = average = total = 0.0

    # Display intro
    print("Welcome to my average program!\n")

    # Loop as long as user says yes they do have more numbers
    # must seed the loop - must be true the first time
    while moreNumbers == "yes":
        # Prompt user for a number
        number = float(input("Please enter a number: "))
        total = total + number
        count = count + 1

        # Prompt for additional numbers
        moreNumbers = input("Do you have more numbers, yes or no: ")  # yes

    # Calculate the average
    average = total / count

    # Display average
    print(f"The average of your numbers is {average}")

    # Display outro
    print("\nThanks, bye")

main()

# This version is better - but who wants to type yes over and over

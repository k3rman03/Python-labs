# Kerman Rodriguez
# 02/23/2025
# This program finds an average of numbers entered by user
# This version uses a conditional loop with two accumulators
# and a negative number as a sentinel

def main():
    # Initialize variables
    moreNumbers = "yes"
    count = 0
    number = average = total = 0.0

    # Display intro
    print("Welcome to my average program!\n")

    # Loop as long as user says yes they do have more numbers
    # must seed the loop - must be true the first time
    while number >= 0:
        # Prompt user for a number
        number = float(input("Please enter a number <Negative to quit>: ")) # 5 7 3 -1

        # Selection structure to make sure only positive numbers get added
        if number >= 0:
            total = total + number
            count = count + 1


    # Calculate the average
    average = total / count

    # Display average
    print(f"The average of your numbers is {average}")

    # Display outro
    print("\nThanks, bye")

main()


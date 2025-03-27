# Kerman Rodriguez
# 02/23/2025
# This program finds an average of numbers entered by user
# This version uses a conditional loop with two accumulators
# and an enter as a sentinel

def main():
    # Initialize variables
    startOver = "yes"
    count = 0
    number = average = total = 0.0

    # Display intro
    print("Welcome to my average program!\n")

    # outher loop for START OVER AGAIN
    while startOver == "yes":
        count = total = 0
        average = number = 0.0
       
        

        # Loop as long as user says yes they do have more numbers
        # must seed the loop - must be true the first time
        while number != "":
            # Prompt user for a number
            number = input("Please enter a number <Enter to quit>: ") # "5" "7" "3"

            # Selection structure to make sure
            if number != "":
                total = total + float(number)
                count = count + 1


        # Calculate the average
        average = total / count

        # Display average
        print(f"The average of your numbers is {average}")

        startOver = input("Do you want to start over again (yes or no)? ") # yes

    # Display outro
    print("\nThanks, bye")

main()

# Add a loop that ask the user if they want to start al over and if they say "yes"
# it starts over asking them to enter a number

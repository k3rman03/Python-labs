# Kerman Rodriguez
# 02/23/2025
# Simple while loop examples

def main():
    age = 0
    grade = -1 # because evaluates from 0

    # A conditional (while) loop start before the first line
    # of code you want repeat
    # A while loop will repeat as long as a condition is true
    # It is a pre-test loop
    # The condition mist be true the first time
    # Call it seeding the loop

    while age < 1:
        age = int(input("Age: "))

        if age >= 18:
            print("You can vote now!\n")
        elif age < 1:
            print("Please enter a positive number\n")
        else:
            print("Sorry, you must be 18 to vote\n")


    while grade < 0 or grade > 100:
        grade = int(input("\nPlease enter a grade: "))

        if grade < 0 or grade > 100:
            print("You must enter a grade between 0 and 100")
        else:
            print("Your grade is", grade)

    

    print("bye")

main()

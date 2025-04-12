# Kerman Rodriguez
# 03/30/2025
# The program calculates the number of calories consumed by a customer
# based on the number of cookies the customer ate.

# Define main function
def main():
    # Declare constants
    # each cookie is 75 calories
    CALORIES_PER_COOKIE = 75

    # Declare and initialize variables
    # String var for name
    userName = ""
    # Whole num var for cookies eaten and calories consumed
    cookiesEaten = 0
    caloriesConsumed = 0

    # Display "WELCOME TO THE CALORIE COUNTER!!"
    print("WELCOME TO THE CALORIE COUNTER!!\n\n")

    # Prompt for name by displaying "Please enter your name:"
    # What if the user enters 7 as their name - what happens
    # Their name is just saved as "7"as numbers can be stored as strings
    userName = input("Please enter your name: ")  # "Bob"

    # Ask the user their age. If the user is under 30 continue on with the program
    userAge = 0
    while userAge <= 0:
        try:
            userAge = int(input(f"\nPlease enter your age: "))

            if userAge <=0:
                print("\nSo, you're... un-born? I'm not sure how to process that. Please enter a valid age.\n")
            # If the user is 30 or older tell them they should not be eating very many cookies these days -  Continue on |
            elif userAge >= 30:
                print("\n30+? Your cookie privileges are under review. Please proceed with caution.")
                break

        # If the user tries to spell out their age tell the user they have to type a number not a word and ask again(use a while loop - NOT infinite)
        
        except ValueError:
            print("\nUmm, We need a whole number age, please.")
        except TypeError:
            print("\nInvalid, try again!")
        except:
            print()


    # Prompt for cookies eaten by displaying "Please enter the number of cookies consumed:"
    # What happens if the user spells out three instead of typing 3??? or 3.5
    # so it will crash here
    # we would never want our user to see all that red gibberish. So as programmers we would wnat to customize
    #the error message
    # try must come before the part of the code that will cause the crash

    # while True: (other way)
    
    while cookiesEaten <= 0:
        try:
            cookiesEaten = int(input(f"\n{userName}, Please enter the number of cookies consumed: "))

            # What if they tyoe a ngative number - what will happen - will it crash
            if cookiesEaten <=0:
                print("\nMust be a typo - You had to eat at least 1 cookie!\n")
            #else:
                #break
            
        except ValueError:
            print("\nYou must enter a whole number only - please try again\n")
        except TypeError:
            print("\nInvalid")
        except:
            print()

    # Calculate calories consumed = cookies eaten * calories per cookie
    caloriesConsumed = cookiesEaten * CALORIES_PER_COOKIE

    # Display calories consumed calling user by name
    print(f"\nOkay {userName}, you consumed {caloriesConsumed} calories!")

    # Display outro
    print("\nThank you for using my program!")        

    
# Call or invoke the main function
main()

#---Try this on your own----- Put these steps in the appropriate places above so the program makes sense and add the code under each step
# Ask the user their age. If the user is under 30 continue on with the program
# If the user is 30 or older tell them they should not be eating very many cookies these days -  Continue on |
# If the user tries to spell out their age tell the user they have to type a number not a word and ask again(use a while loop - NOT infinite)





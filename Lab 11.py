# KERMAN RODRIGUEZ
# 04/12/2025
# This programn will show examples of string method

def main():

    # Sometimes users hit the space bar when you don't want then to usually
    # at the beginning of their answer

    mystring = "   word   "

    # Let's add a string with odd cases

    mystring2 = "I love pYthon"

    # Methods always have () even if no arguments can be passed to them
    # These methods are commonly used
    # They can help make sure your output is proper no matter how they type it
    print(mystring2)
    print(mystring2.upper())
    print(mystring2)
    print(mystring2.capitalize())
    print(mystring2.lower())
    print(mystring2.title())

    # We use them to compare to for things like If and while also - that way we can compare
    # their answer to "yes" let's say
    # when we don't know for sure they will type it all lower - making our comparison easier
    #Prompt for user phrase
    answer = input("Do you love Python (yes or no)? ").strip().lower() # Yes -> yes
    # if answer.lower() == "yes":
        # print("Me TOO!")
        # print("This is easier than a bunch of conditions right\n")
    
    if answer == "yes":
        print("Me TOO!")
        print("This is easier than a bunch of conditions right\n")

    print(mystring)

    # lstrip will get of spaces on the left side of the first character
    print(mystring.lstrip())
    # rstrip will get rid of the spaces on the right side of the last character
    print(mystring.rstrip())
    # strip will get rid of the spaces on both sides of any character
    print(mystring.strip())

    # strings are immutable so no permanent change is made
    # after calling those methods on the variable
    print(mystring)

    mystring = mystring.strip() # Here we save over the original
    print(mystring) # Now there are no spaces in the original variable

    # word
    # The center method is useful for user friendliness of output
    print(mystring.center(40))
    # You can even add symbols on either side by passing the center method 2 arguments
    print(mystring.center(40, "*"))

    # What if the hit the space bar in the middle
    name = " Sammy Seahawk "
    print(name)

    #Using any of the strip methods will not get rid of the space in the middle of 2 words
    print(name.lstrip())
    print(name.rstrip())
    print(name.strip())

    # We can use another method though called split to separate the string into 2 variables
    # 1 for first name, and one for last name
    fname, lname = name.split() #When nothing is placed in the () of split it means at the space
    print(fname)
    print(lname)

    # or into 1 list with 2 items, first name, and last name
    nameList = name.split() #Again, when nothing is placed in the () of split it means at the space
    print(nameList)

    # Then we can use slicing to pull out only the first name
    print("Hello", nameList[0])

    # We can also use split when we have values separated by any kind of spearator like a comma
    fruits = "apple,orange,banana"
    fruitList = fruits.split(",") #You can pass 1 argument to split to specify the separator
    print(fruitList)
    
    # Add to the program before submitting:
    # Choose 2 functions or methods listed in PE2 module 2 that we did not cover in this lab already (examples: isalpha, replace, find, etc.)
    # I chose the replace() and find() methods
    # Add them in any way you like, just document what you did
    # Using replace() to change a word in a string
    sentence = "I love Python programming."
    new_sentence = sentence.replace("Python", "Java")
    print(new_sentence)
    # Using find() to locate the position of a substring
    position = sentence.find("Python")
    print("The position of 'Python' in the sentence is:", position)
    # Also add asking the user if they want to play again and store their answer as all upper case using the upper() method and strip away spaces
    # Use a loop with a condition of if they say YES they want to play again then the entire program goes again.
    # If the do not say YES then thank them for playing and end the program
    while True:
        play_again = input("Do you want to play again (yes or no)? ").strip().upper()
        if play_again == "YES":
            main()
        else:
            print("Thank you for playing!")
            break

    
    
    
    
    
    
    

main()

# Add to the program before submitting:
# Choose 2 functions or methods listed in PE2 module 2 that we did not cover in this lab already (examples: isalpha, replace, find, etc.)
# Add them in any way you like, just document what you did
# Also add asking the user if they want to play again and store their answer as all upper case using the upper() method and strip away spaces
# Use a loop with a condition of if they say YES they want to play again then the entire program goes again.
# If the do not say YES then thank them for playing and end the program
    

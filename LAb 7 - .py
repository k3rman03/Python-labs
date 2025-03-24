# Kerman Rodriguez
# 03/19/2025
# More advanced List Practice

def main():
    # This is a list containing 3 items, all strings
    animals = ["dog", "cat", "bird"]
    # This is a list containing 3 items, all integers
    nums = [7,2,99]

    # Indexed positions and slicing
    # We can pull out a single item from the list
    print(nums[0]) # will display the 7
    # We can pull from the right using negative indices
    print(nums[-1]) # will display 99 as that is the last item
    # We can print multiple values (or a range of values) at once using slicing
    print(nums[0:2]) # THis will display 7 and 2 but not the 99 because it will slice position 0 and 1
    # What this will pull out?
    print(animals[1:3]) 
    # We can omit positions sometimes
    # If i want to start at 0, I can omit the 0 like this
    print(nums[:2])
    print(nums[1:]) # when it is blank on the right of the colon it means start at 0

    print("\n")
    
    
    # in and not in operator
    # Will return True or False
    print(99 in nums)
    print(99 not in nums)
    print(8 not in nums)
    print("dog"in animals)
    print("dog" not in animals)
    print("Apple" in animals)
    print("Apple" not in animals)

    print("\n")

    # in will return True if an item is in the list
    if 99 in nums:
        print("99 is almost 100")

    # not in will return True if the item is not on the list
    if "hamster" not in animals:
        print("A hamster is an animal too")

    print("\n")

    # this is an example of using a for loop to populate a list when you need exactly 3 things
    for i in range (3):
        animal = input("Please enter a type of animal that you like: ")
        if animal in animals:
            print("That animal is already in our list")
        else:
            print("Let's add that animal to our list")
            animals.append(animal)
            print(animals)

    print("\n")

    # A while loop can be used also:
    

    animal = ""

    while animal not in animals:
        animal = input("Please enter a type of animal that you like: ")
        if animal in animals:
            print("That animal is already in our list")
            animal = "" # to keep asking for more animals
        else:
            print("Let's add that animal to our list")
            animals.append(animal)

        print(animals)

    print("Bye")

    

    
main()
    



def homework():


    #Add to these 2 things to the program before submitting:

#Create a constant called myName and store your first name in it
    myName = "Kerman"
    
#Create an empty list called names
    names = []
    
#Use a for loop to ask the user to enter a first name (6 times)
    for i in range (6):
        name = input("Please enter a first name: ")
        
#Add the name to the end of the list (using append)
        names.append(name)
        
#If the name entered matches your name stored in the constant - Display something funny to them
    if myName in names:
        print(f"It is funny my name is {myName}")
            
#If they never entered your name tell them you are adding your name too and add your name (the constant)
#to the list
    else:
        print(f'I also will be adding my name "{myName}" to the list')
        names.append(myName)
            
#When finished, sort and display the list of names back to the user
    names.sort()
    print(names)
            
        
def homework2():

    guesses = []
    number = 0
    
#Create a constant to store your favorite number like favNum = 8
    favNum = 4

    print("Welcome to Guess My Favorite Number Game!!\n")

#Then ask the user to guess a number from 1 - 20, add their guess to a new list called guesses.
    while number != favNum:
        number = int(input("Please enter a number from 1 - 20: "))
        if number < 1 or number > 20:
            print("\nYou must enter a number from 1 - 20, try again!")
            guesses.append(number)

#If they guess the same number again on accident, tell them they already guessed that number and
#do not add the number to the list
            
        elif number in guesses:
            print("\nYou already entered that number, try again!")
            guesses.append(number)
        
            
#They must keep guessing until they guess your favorite number
            
        elif number == favNum:
            print(f"\nCongratulations!! you guessed my favorite number")
            guesses.append(number)
        else:
            print("\nWrong number, try again!")
            guesses.append(number)
            
#Once they get it right, count how many numbers they entered (use the len function)
#and show them the list of guessed numbers and the count of how many times it took them
    
    print(f"\nIt took you {len(guesses)} try(s) to guess my favorite number")
    print(f"These are numbers you entered {guesses}")







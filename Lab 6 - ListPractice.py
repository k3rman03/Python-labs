# Kerman Rodriguez
# 03/02/2025
# List Practice

def main():
    # This is a variable storing a single string
    fun = "I love Python"


    # This is a list containing 3 items, all strings
    animals = ["dog", "cat", "bird"]

    # This is a list containing 3 items, all integers
    nums =  [7,2,99]

    # Let's see how each displays
    print(fun)
    print(animals)
    print(nums)
    print("\n")

    # index prositions
    # TO be able to use data from a list we have to be able to access it and pull it out or put it in
    # every item in a list has a numbered (indexed) positions, item are separated by commas
    # indexed positions start count at 0 from left
    # so dog in the list of animals is in indexed position 0
    print(animals[0])
    print(animals[1]) #is a cat
    print(animals[2]) # # is a bird

    # we can also access it from the right side or the end of the list using negative indices
    print(animals[-1]) # will display bird - the last item in the list (or the first from the right)
    print(animals[-2]) # will display cat - the 2nd to last item in the list (or second from the right)

    # Now we will practice using various methods on our lists
    # A method changes a list instantly and permanently since lists are mutable
    # This is not the same on a variable storing a single value

    
    # Some methods cannot be passed any arguments, some must be passed arguments
    # and some can be passed arguments, but do not have to be
    # append adds to be to the end of the list - takes 1 argument
    animals.append("fish") 
    print(animals)
    print("\n")

    # insert adds to a position in the list - must pass 2 arguments
    animals.insert(0, "lizard")
    print(animals)
    print("\n")

    # pop removes from the list - by default the last item if no arguments
    print(animals.pop())
    print(animals)
    print("\n")

    # pop can also remove a location if you pass it 1 argument
    print(animals.pop(0))
    print(animals)
    print("\n")

    # remove will also remove from a list - but a specific item passed to it
    animals.remove("cat")
    print(animals)
    print("\n")

    # del is an instruction not a method - can be used in a list or on a whole list
    del animals[1]
    print(animals)
    print("\n")

    # Let's put 2 things back into the list for the next part
    animals.append("bird")
    animals.append("cat")
    print(animals)
    print("\n")

    # the sort method will make it ascending (a-z) and store it that way
    animals.sort()
    print(animals)
    print("\n")

    # reverse reverses the list so
    # if you want z-a you must first sort a-z
    animals.reverse()
    print(animals)
    print("\n")

    # We've inly been using the list of strings, but it does the same thing with nums
    print(nums)
    nums.sort()
    print(nums)
    print("\n")

    nums.reverse()
    print(nums)
    print("\n")

    # The stored function will dsiplay a-z but not store it in that way
    print(sorted(animals))
    print(animals)
    print("\n")

    # The len function will count items in a list
    print(len(animals))
    print(len(nums))
    print("\n")

    # When you pass a len a string  - it counts number of characters in a string
    print(len(fun))
    print("\n")
    
    # The sum function is a very fast way to add up a bunch of numbers stored in a list
    print(sum(nums))
    print("\n")

    # We can easily find an average of any amount of numbers stored in a list
    # by combining the sum and len function
    print(sum(nums) / len(nums))
    print("\n")

    # we often loop through lists to make more eficient code
    for i in animals:
        print(f"I love {i}s")

    print("\n")

    for number in nums:
        print(number ** 3)

    print("\n")

    # Here is an example checking items in a list
    for num in nums:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
    print("\n")



    # OWN WORK

    number_pets = 0

    pets = []

    listNumber = 1

    print("welcome to The Tale of Tails, a fur story\n")

    number_pets = int(input("Please enter the total pet(s) you have had in your life: "))

    if number_pets <= 0:
        print("\nOhh you should get a pet, they bring joy to us!")
    else:
        print("\nNow enter the type of pet in chronological order:\n")

        for i in range(number_pets):
            pets.append(input(f"Pet number {listNumber}: "))
            listNumber += 1

        pet_types = []
        for pet in pets:
            if pet not in pet_types:
                pet_types.append(pet)

        count_result = ""

        for petType in pet_types:
            count = pets.count(petType)
            count_result += f"{count} {petType}s, " if count > 1 else f"{count} {petType}, "

        if number_pets > 3:
            print('\nWow you love animals, you had', count_result + 'That\'s a happy fur story!')
        else:
            print("\nOnly ", count_result + "you should get another pet, remember try to adopt when getting a new fur-friend!")
        
        
main()
        

    
    

def getScores(): # Does not work this way
    # Declare and initialize empty list
    scores = []

    # Print Intro
    print("Welcome to my number sorting program!")

    for i in range(5):
        scores[i] = int(input("please enter a score: ")) # "90"--> 90

    print(scores)

    

def getScores2(): 
    # Declare and initialize a list with 5 ints
    scores = [0] * 5 # can also be [0,0,0,0,0] but too long

    # Print Intro
    print("Welcome to my number sorting program!")

    for i in range(5):
        scores[i] = int(input("please enter a score: ")) # "90"--> 90

    print(scores)

        
def getScores3():
    # Declare an initialize whole var to store how many scores
    numScores = 0
    # Declare and initialize empty list
    scores = []

    # print intro
    print("Welcome to my number sorting program!")

    # Prompt for how many scores
    numScores = int(input("How many scores do you have to enter? ")) #3

    for i in range(numScores):
        scores.append(int(input("Please enter a score: "))) # "90"-> 90 -> [90, 85, 98]

    print (scores)

def getScores4():
    # Declare an initialize whole var to store how many scores
    numScores = 0
    # Declare and initialize empty list for 3 int
    scores = [] * 3

    # print intro
    print("Welcome to my number sorting program!")

    # Prompt for how many scores
    numScores = int(input("How many scores do you have to enter? ")) #3

    for i in range(numScores):
        scores.append(int(input("Please enter a score: "))) # "90"-> 90 -> [0, 0, 0, 90, 85, 98]

    print (scores)
    
            
    
        
    
    
    
    



    
    
    

    
    
    

    

    
    



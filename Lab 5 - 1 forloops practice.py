# Kerman Rodriguez
# 02/23/25
#For Loop Examples

def main():
    # This will be a counted loop
    # Also known as a for loop
    # A counted loop always executes a predetermined number of times
    # Range is a built in function in Python that allows us to repeat a loop a specific number of times
    # 1 argument passed to range means repeat that many times
    
    for i in range(10):
        # Anything indented is the body of the loop
        # and what will repeat
        print("Happy Birthday")
        print("to you")

    print("\n")

    # count out loud to 3 --- you said 1, 2, 3 right? of course you did, that is what humans  do
    # The range function starts count at 0 though by default - and increments by 1 by default
    # The i is the placeholder variable that basically keep track of each time the loop iterates
    # It doesn't have to be an i, it can be anything relly. We will use other thingf later
    for i in range(3):
        print(i) # This will display from 0 - 2 which is looping 3 times


    print("\n")

    # Now you can really see how usefull the end  keyword is, that we learned earlier
    # When used in a loop it can allow every iteration of the loop to go on the same line
    for i in range(10):
        print(i, end = " ")

    print("\n\n")

    # Passing 2 arguments to the range function
    # - 1st is start position, 2nd stop position
    # it will count from and including the start, up to but not including th stop
    # this is 1-10 displayed
    for i in range (1,11):
        print(i, end = " ")

    print("\n")

    # Class try 5 - 23 on one line separated by tabs
    for i in range(5,24):
        print(i, end = "\t")


    print("\n\n")

    # Passing 3 arguments to the range function
    # 1st argument is still the start, 2nd is still the stop
    # the third argument is now the step - or what we want to increment by, instead of the default of 1
    # this will count by 2's
    for i in range(2,11,2):
        print(i)
        
        
    print("\n")

    # class - display a 5 a tab a 10 a tab a 15
    for i in range(5,16,5):
        print(i, end = "\t")

    print("/n")


    # What if we want to count backwards from 10 to 1, like a count down
    # if we use only 2 argument telling it to start at 10 and end on 1 (stop 0) nothing will happen
    for i in range(10,0):
        print(i)

    print("\n")

    # Any time you want to count backward, even by only 1, you must add a negative step (-1)
    for i in range(10,0,-1):
        print(i)
        

    print("\n")

    # Class - display 10 tab 7 tab 4
    for i in range(10,3,-3):
        print(i)

    print("\n\n")


    # The for loop can also be used to iterate through a list
    # we will learn more about list soon, but for now that list are items placed inside square brackets in Python
    # When we want to iterate through each item in a list we do not use the range function - we use the list
    for i in [-2,3,4,5]:
        print(i**2)

    print("\n")

    # Usually the list is already in the program though like this
    numbers = [2,4,6,8]

    # to make the loop more readable we often use words that make sense instead of just generic i
    for num in numbers:
        print(num)

    print("\n")

    animals = ["cat","dog","bird"]

    for i in animals:
        print(f"I love {i}s")
        
        
    print("\n")

    # we often use loops to accumulate totals
    total = 0

    print(total) # 0 

    for i in range(5):
        # total += 10 is more common
        total = total + 10 # 10 20 30 40 50 
        print(total)

    print("\n")


    for i in range(5):
        # total += i could also be used
        total = total + i
        print(total) # 50+0 50+1 51+2 53+3 56+4

    print("\n")


    for i in range(1,6):
        print(total+i) # 61 62 63 64 65 - we are not accumulating, total value doesn't change

    print("\n")


    # The arguments passed to the range function can be integers, or variables that store integers

    start = int(input("What number do you want to start on? ")) # 1
    stop = int(input("What number de you want to end on? ")) #10

    for i in range(start,stop+1):
        print(i)

    print("\n")

    #OWN WORK

    for i in range (1,4):
        print(f"This is line {i}")

    print("\n")

    for i in range(5,26,5):
        print(f"{i}\t||\t{i**2}")

    
        

    
        



main()

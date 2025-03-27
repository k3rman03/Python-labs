# Kerman Rodriguez
# 03/22/2025
# Fun game that prompts user for data to populate a list and then does fun things with the data


def main():

    #Create an empty list to store the answers in
    bikesList = []

    #Declare a constant that stores your answer to the question (just 1 answer), and one to store the number of items to be entered (5)
    qAnswer = ""
    groupSize = 0
    myFavBike = "Ducati"

    #Declare and initialize a variable for play again
    playAgain = "yes"

    #Display a friendly attractive Title
    print("Welcome to Your Favorite Brands of Motorcyles Game!\n")

    print(f"                          `   `.")
    print(f"   <```--...       .---.//  < `.")
    print(f"    `..     `.___ /       ___`.'")
    print(f"      _`_ .      `      .'\\\\__")
    print(f"    .'---`.`.          / .'---`.")
    print(f"   /.'  _`.\\_\\        / /.'\\\\ `.\\")
    print(f"   ||  <__||_|        | ||  ~  ||")
    print(f"   \\`.___.'/ /________\\ \\`.___.'/")
    print(f"    `.___.'              `.___.'")

    #Display a short intro to the game and any rules they should know
    print(f"\nThis game will ask your group's favorite motorcycles brands, I have my own favorite one. \nLet's create a list and do some fun things with it.\n")
    
    groupSize = int(input("How many people are in your group? "))
    print(f"\nGreat! now the system will ask you for {groupSize} favorite motorcycle brands.\n")
       
    #For every time the user said yes they do want to play again do the following:
    #Ask the user a question 5 times and add their answer from each time to a list      
    #Display your answer to the question - using the constant in the output
    counter = 0
    while playAgain == "yes":
        for i in range(groupSize):
            qAnswer = input(f"Player #{counter + 1} Please enter your favorite motorcycle brand: ").capitalize()
            counter += 1
    #If your answer is also in the list display something like "I see we might know the same person as you wrote 'Your Answer' also!" 
    #(or whatever your question was about if not a name)
            if qAnswer in bikesList:
                print(f"\nIt seems another player likes '{qAnswer}' too!")
            else:
                bikesList.append(qAnswer)
    #Otherwise display something like "I see that you don't have a favorite person named 'Your Answer', let's add that name to our list" 
    # - and Add the name to the end of the list (or whatever your question was about if not a name)
        if myFavBike not in bikesList:        
            print(f"\nIt seems my favorite brand '{myFavBike}' is not on the list, let's add it to our list.")
            bikesList.append(myFavBike)
        else:
            print(f"\nHurrah, there is someone else that likes my favorite brand '{myFavBike}' too!!!")
    #Display the list of answers to the user            
        print(f"\nOur favorite motorcycles brands are: {bikesList}")
       
    #Display "Now let's do some fun things with our list of (whatever the list is of):"
        print(f"\nNow let's do some fun things with our list of favorite motorcycles brands:")
    
    #Sort the list in ascending order using the sort method
        bikesList.sort()
        
    #Display "Here is the list in alphabetical order 'list' "
        print(f"\nHere is our motorcycle's list in alphabetical order: \n{bikesList}")
       
    #Display "The last item in the list now is 'display last item in list' " using -1
        print(f"\nThe last brand in our list now is: {bikesList[-1]}")
       
    #Display "I can count how many items are in the list. There are 'num items in list'  items in the list" (using len)
        print(f"\nIn total we have {len(bikesList)} different motorcycles brands in our list.")
       
    #Use an infinite loop (while True) to ask the user to enter an item to be removed from the list.
    #if the item the user enters is in the list delete it and exit the loop (use break)
        while True:
            itemToRemove = input("If you want to remove one enter the name to remove from the list (or 'exit' to stop): ").capitalize()
            if itemToRemove.lower() == "exit":
                break
            elif itemToRemove in bikesList:
                bikesList.remove(itemToRemove)
                break
    #if the item is not in the list display "Sorry, that item is not in the list, please try again" and keep asking for an item in the list
            else:
                print("\nSorry, that brand is not in the list, please try again.\n")
    
    #Display the number of items in the list now with a friendly sentence
        print(f"\nNow we have {len(bikesList)} different motorcycles brands in our list.")
    
    #Loop through the list and display each item on its own line
        print(f"\nHere is our updated list of favorite motorcycles brands:")
        for brand in bikesList:
            print(brand.capitalize())
            
    #Use 1 additional method we learned (not already used) or slicing to display something fun to the user
        print(f"\nLet's display the first 3 brands in our list:")
        for brand in bikesList[:3]:
            print(f"{brand}")
 
    #Prompt user if they want to play again
        playAgain = input("\nWould you like to play again? (yes/no): ")
        if playAgain.lower() == "yes":
            bikesList.clear()
            counter = 0
            qAnswer = ""
        print("\n")
       
    #Display a simple outro (like we have done in all lectures)
    print("Thank you for playing the game. Have a great day!")
    
main()

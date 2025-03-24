# Kerman Rodriguez
# 02/10/2025
# This Program will explain various math operations and variables

# Programmin languages follow the same math order of operations you already know
# PEDMAS - Parenthesis, exponents, multiplication, division, addition, substraction, left to right

# operantion include +, -, /, //, %. **
# Anything in quotation marks remember is a string literla and will be output as typed
print("2 + 2") # will display as 2 + 2

# so + between 2 numbers adds them (the spaces do not matter - tyoed to make the code more readable)
# As you can see the number are not placed inside quotation marks
print(2 + 2)
print("2" + "2") # A plus between 2 strings concatenates merges them together into 1 string

# - means substract
print(2 - 1) # will display 1

# * is for multiplication (Note that you cannot type x for times)
print(2 * 3) # will display 6

# / is for division - division will always return a float by default
print(11 / 5) # will display 2.2

# // is for integer division and will always display the integer value of the answer
print(11 // 5) # will display 2 not 2.2

# % is known as remainder division and will return the remainder only
print(11 % 5) # will display 1 (5 goes into 11 2 times with remainder of 1)

# ** is to the power of
print(2 ** 3) # means 2 to the power of 3, will display 8

# Order of operations
# What is in parenthesis happens first
print(2 * (3+2)) # will display 10 because 3+2 happens first
print (2 * 3 + 2) # will display 8 because 2 * 3 happens first - multiplication before adition

# these would both be the same answer because the 3 * 2 happens first in both, so no need for ()
print(2 + (3*2))
print(2 + 3 * 2)

# Important to note is that when all the arguments are integers the result will also be an integer
print(2 + 3 * 2)

# but even if 1 argument is a float the result will be a float
print(2.0 + 3 * 2)


print()
print()

# Variables:
# Variables are like virtual containers that store data for use later in the program
# Variables names have rules:
# Cannot start with a number or special character other than _ which is considered a characther (can have a number in the name)
# Cannot contain spaces
# They are case sentitive, so Age is not the same as age
# Must not be the same as any Python reserved word
# Each variable in a program must have an unique name - if you had t2 players maybe player1Name and player2Name, not playerName twice
# I would never call a variable name and store an age in it or call it age and store a user name

# to create a variable we first decide on a name and then put a value in it -
# The variable always  comes first, then an + which means to assign a value, then the value to be assigned to the variable
# So here the value Sammy is now assigned to the variable userName
userName = "Sammy"
userAge = 21

# The way I named the variables uses something we call camel case - many believe it makes it more redeable
# But you could also write user_name or username - all are acceptable variables names (never user name as spaces are not allowed)
# Coose a style that you prefer and name all your variables that way

# The data stored in a variable can change throughout a program (even change data type)
myVariable = 5
# Since myVariable is not in "" it will not print literally
# Instead what displays is the value stored in the variable myVariable wich is 5
print(myVariable)

print()
# I can then change what is stored in myVariable
myVariable = "Now it's a phrase"
print(myVariable)

# to display multiple variables you can use comma separated arguments, concatenation, or f formatting
print(userName, "is", userAge)

# Using concatenations only works if the variables contain strings
print(userName + " is " + myVariable) # Samy is
# If the variables contain numbers, the program will crashunless you convert the number to a string
# print(userName + "is" + userAge) this crashes because you cannot concatenate a word and a number
print(userName + " is " + str(userAge))

# if I use f formating for output put the variables inside curly braces and any data type can be used
print(f"{userName} is {userAge}")

print()
print("2 + 2= ", 2+2)
print()
# we can even do math inside the curly braces in f formating
print(f"2 + 2 = {2+2}")
print()


# Try these on your own before submitting this lab
# Create a variable called myName and store your first name in it
myName = "Kerman"
# Create a variable called myPhrase and stored in it (any silly phrase)
myPhrase = "Cookies & Cream Ice Cream"
# Using comma separated arguments, display your name then the word likes and then the silly
# phrase (using the variable except for the word likes)
print(myName, "likes", myPhrase)

# Now use f formating to display the same output
print(f"{myName} likes {myPhrase}")

#Next, create these 4 variables A = 3, B = 4, C = 2, D = 5

A = 3
B = 4
C = 2
D = 5

# Now use print statements to display the correct answers to the equations (Keppe in maind proper math order of operations)
# Display the answer to this equation 4A - 2BC
print(4 * A - 2 * B * C)

# Display the answer to this equation -> D plus B devided by A minus C
print((D + B) / (A - C))











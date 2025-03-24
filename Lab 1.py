# Name: Kerman Rodriguez
# Date: 02/10/2025
# Desc: This program will show some basic output examples

# Display Intro
print("Welcome to my program!")
# An empty print statement will make a blank line
print()
print("Line 2")

# Dsplay your name
print("My name is")
print("Kerman Rodriguez")

# The backslash \ in Pyhton is known as the escape character - it makes the next character after it, not display as a literal
# \n used thogether inside the "" will make an error, for 2 enters you must use 2 - \n\n
# Each time you type a \ it only escapes the single next character so \nn would make an enter and then show the second n
print("Bye\n")
print("Bye\nn")
print("Bye\n\n")

# Dsplay your name
print("My name is\nKerman Rodriguez")

# The keyboard argument end= will replace the built in enter with whatever you use there
# Dsplay your name
print("My name is", end = " ")
print("Kerman Rodriguez")

# This is passing 2 arguments to the print function
# a comma usually makes a space
print("My name is", "Kerman Rodriguez", ".")

# This variable called name that is holding the value Kerman
name = "Kerman"

print("My name is", name, ".")
# Using concatenation you can merge 2 strings - only strings
print("My name is", name + ".")

# keyboard sep = will change what happens at the comma
print("My name is", name, ".", sep = "*")


# Next let's discuss the difference between one ', two " and three """

# single line print works with double " or single '
print("This displays")
print('So does this')
# print("This will not') - you cannot mix them

# so why do we use one over the other?

# It really just depends on each programmers personal style preference.
# In this case I will mainly use double quotation marks though

# print('I'm cool!')this won't work
# But this will
print("I'm coll!")

# A bacslash character in python is the scape character
print('I\'m cool!')

# print("Hello "John", how are you")
print('Hello "John", how are you')

print("Hello \"John\", how are you")


# This shows displaying single and double quote using """
print("""I'm "coll"!""")

# Single line comments vs multi-line comments
"""This
is
a multi-line
comment
"""

# I can type on 2 lines in single print but thisplay on
# 1 using a " on each line
print("This is written on 2 "
      "lines but displayed on 1")

print("This displays on")
print("2 lines")

#this makes an enter \n
print("This displays on\n2 lines")

# Or I can type on 2 lines and display on
# 2 lines using """
print("""This displays on
2 lines""")

# Phyton literals
# So everything tyoed above is what we call strings literals. What displays exactly waht we type.
# A string can be thought of as a word. But a number can be stored as a word, so a 2 can be a string if we want it to be
print("I am a string literal - I will display eactly as typed")
print("2")

# The next data type we will learn will be what is called an integer - A whole number like 18 - Integers have no decimals
print(2)

# There doen's appear to be a difference, but in the next section we will see
# that math cannot be done with strings, only with numbers

# The third data type we will learn is called a float - It is a real number so will have a decimal value
print(3.75)

# *****************Now you add some code of your own before submitting this Follow Allong Lab*********

# Use end = " " at the end of the first print below to make what is typed in 2 different print statements appear on line 1
# Display I am learning to do cool things with Python
# Display like display on 1 line what is printed on 2 in the program code

print("I am learning to do cool things with Python", end = " ")
print("like display on 1 line what is printed on 2 in the program code.")

# Use sep = " - ", and comma separate arguments for each string in the print statement below to get the -'s betwee sections
# Display I can even - put symbols - between - the arguments displayed!
print("I can even", "put symbols", "between", "the arguments displayed!", sep = " - ")

# Display some kind of desing using print statements and symbols from your keyboard (like the arrow in Netcad - but not an arrow)

print("                               o")
print("                              /\\")
print("                             /::\\")
print("                            /::::\\")
print("              ,a_a         /\\::::/\\")
print("             {/ ''\\_      /\\ \\::/\\ \\")
print("             {\\ ,_oo)    /\\ \\ \\/\\ \\ \\")
print("             {/  (_^____/  \\ \\ \\ \\ \\ \\")
print("   .=.      {/ \\___)))*)    \\ \\ \\ \\ \\/")
print("  (.=.`\\   {/   /=;  ~/      \\ \\ \\ \\/")
print("      \\ `\\{/(   \\/\\  /        \\ \\ \\/")
print("       \\  `. `\\  ) )           \\ \\/")
print("   jgs  \\    // /_/_            \\/")
print("         '==''---))))\n")
# The scape "\" had to be used several times because of the shape of the figure


















# Kerman Rodriguez
# 02/10/2025
# COP1000C
# Program for basic output examples

# Display Intro
# "Sep" parameter is used to add "-" between arguments 
print("Lab", "Program ", " for module 2 ", " Sections 1 & 2!", sep="-")

# Display name and last name using "end" to define what to print at the end of the argument
print('\nThe "Hello World!" Program', end=" ") # Used the scape charater "\" to add a line between the intro and name "\n" 
print("and Python literals.\n") # \n will be use several times to add lines, \n\n... can be use to add more than one line

# Module objetive
print("The sections of this module demostrates basic Python's programing outputs")
print("using the function \"print\" and different types of arguments.\n")

# String literals will print exactly what is typed
print("Example of a String literal:")
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

# Strings can be written in two lines but print only one, or the other way around.
print("We can display several written lines in one, "
      "e.g. The aligator is holding"
      "a flag, GO GATORS!!\n")


print("Also, one written line can be displayed in several lines using the \"\\n\" escape:")
print("e.g. The aligator is holding", "\na flag, GO GATORS!!\n")

# Integers & floats
print("The section 2.2 of the module 2 shows us the differences between ints & floats\n")
print("In programing Integers are whole numbers like,", 6, "and floats are decimal fractions like,", 6.8, sep=" ")

# Booleans
print("\nAt last, in Paython's literals, are two other conditions know as \"Boolean values\".\n"
      "The program answers according to these boolean values (< >), Yes = True or False.\n")

print(True < False)
print(True > False)

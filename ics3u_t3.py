# Here is a program to show how to use "if - elif - else"
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Mr. Jugoon
# Upper Canada College

# Put down some options for the user to choose from...
print("What's something you're looking forward to today?")
print("1 - School")
print("2 - Sleep")
print("3 - Sports")
print("4 - Lunch \n")
print(" ")
print("Choose one of the number options above")

activity1 = int(input("What is your current mood? \n"))

if mood == 1:
    print("It's Great to learn! \n")
elif activity1 == 2:
    print ("Tired eh? Late night or early morning \n")
elif activity1 == 3:
    print ("Nice and healthy! \n")
elif activity1 == 4:
	print("Sounds good to me! \n")
else:
    print ("This is not a valid choice")
    print ("Hope you have a great day anyway!")


# This is a way to gracefuly exit the program
input("Press ENTER to quit the program")

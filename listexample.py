print("Hopefully, this program will open a file and read it")

f = open("listwords.txt", "r")

#This will read the whole file
print(f.read())
print("")

favactivity = str(input("What is your favorite activity? \n"))

print("You wrote: "+favactivity)

f.close()

f = open("listwords.txt", "a")
f.write ("\n" + favactivity + "\n")
f.close()

f = open("listwords.txt", "r")
print (f.read())



input("Press ENTER to end the program")
print("\n")
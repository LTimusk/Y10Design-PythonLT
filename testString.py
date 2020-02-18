givenString = "Hello"
numChars = len(givenString)
print (numChars)
newString = ""
for x in range(0, numChars, 2):
    # print (newString)
    print (newString + givenString[x])
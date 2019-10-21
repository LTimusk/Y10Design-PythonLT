import json
import requests

#*************************** RETRIEVING DATA ******************************************

request = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t=Toronto")
request_text = request.text

#print(type(data))

data = json.loads(request_text)


#*************************** USER REQUESTS ******************************************

# Assing is =
# If statement is ==

urequest1 = input("What Toronto team would you like to learn about? \n 1: Toronto FC \n 2: Toronto Raptors \n")


if urequest1 == "1":
	urequest2 = input("Which player would you like to learn about? \n 1: Jozy Altidore \n 2: Caleb Patterson-Sewell \n 3: Victor Vazquez \n 4: Gregory van der Wiel \n 5: Chris Mavinga ")
elif urequest1 == "2":
	urequest3 = input("Which player would you like to learn about? \n 1: Kyle Lowry \n 2: Marc Gasol \n 3: OG Anunoby \n 4: Serge Ibaka \n 5: Normal Powell ")
else:
	print("Sorry, that isn't a valid answer")
	print("\n ******************** END OF CODE ****************** \n ")
	exit()

if urequest2 == "1":
	urequest4 = input("What would you like to know about Jozy Altidore? \n 1: Date of birth \n 2: Nationality \n 3: Position \n")
	if urequest4 == "1":
		datajson = request.json()
		datapoint1 = datajson ['player'][1]['dateBorn']
		print ("This player's date of birth is: " + datapoint1)
	elif urequest4 == "2":
		datajson = request.json()
		datapoint1 = datajson ['player'][1]['strNationality']
		print ("This player is from: " + datapoint1)
	elif urequest4 == "3":
		datajson = request.json()
		datapoint1 = datajson ['player'][1]['strPosition']
		print ("This players position is: " + datapoint1)









datajson = request.json()
datapoint1 = datajson ['player'][12]['strPlayer']
print (datapoint1)










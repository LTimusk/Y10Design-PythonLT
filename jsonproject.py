import json
import requests

#***** HELPER FUNCTION

def writeHTML(data):
    myfile = open("playerAPI.html","w") # use "a" to "append"
    
    ############### CSS
    
    myfile.write("""
    <html>

      <head >
        <title> Toronto Soccer Team </title>
      </head>

      <body style="background-color: #80e5ff;">
        <h1 style="text-align:center" >Welcome to My Toronto Sport Team Home Page</h1>

        

        <p  style="text-align:center">Below is the information you requested</h1>

        <p style="text-align:center">-The Data you requested is: """+ data+ """</p>



        <p style="text-align:center"> <font size="4" color="red" style="font-family:verdana">Go to <a href='https://apilist.fun/api/the-sports-db'>The Sports DB</a> for additional API Info.</font></p>

      </body>

    </html>""")


    ################# CSS
    myfile.close()



#*************************** RETRIEVING DATA ******************************************

request = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t=Toronto")
request_text = request.text

#print(type(data))

data = json.loads(request_text)


#*************************** USER REQUESTS ******************************************

# Assing is =
# If statement is ==

urequest1 = input("What Toronto team would you like to learn about? \n 1: Toronto FC \n 2: Toronto Raptors \n")
#userrequest2 = input("Which player would you like to learn about? \n 1: Kyle Lowry \n 2: Marc Gasol \n 3: OG Anunoby \n 4: Serge Ibaka \n 5: Normal Powell ")


#******************** TORONTO FC *************************
if urequest1 == "1":
	urequest2 = input("Which player would you like to learn about? \n 1: Jozy Altidore \n 2: Caleb Patterson-Sewell \n 3: Victor Vazquez \n 4: Gregory van der Wiel \n 5: Chris Mavinga \n ")
elif urequest1 == "2":
	userrequest2 = input("Which player would you like to learn about? \n 1: Kyle Lowry \n 2: Marc Gasol \n 3: OG Anunoby \n 4: Serge Ibaka \n 5: Normal Powell \n ")
else:
	print("Sorry, that isn't a valid answer")
	print("\n ******************** END OF CODE ****************** \n ")
	exit()


#***************** PLAYERS DATA **************************

if urequest1 == "2":
	print("")
else:
	if urequest2 == "1":
		urequest4 = input("What would you like to know about Jozy Altidore? \n 1: Date of birth \n 2: Nationality \n 3: Position \n")
		if urequest4 == "1":
			datajson = request.json()
			datapoint1 = datajson ['player'][1]['dateBorn']
			print("Calling the HTML helper function")
			writeHTML(datapoint1)
			print ("This player's date of birth is: " + datapoint1)
		elif urequest4 == "2":
			datajson = request.json()
			datapoint2 = datajson ['player'][1]['strNationality']
			writeHTML(datapoint2)
			print ("This player is from: " + datapoint2)
		elif urequest4 == "3":
			datajson = request.json()
			datapoint3 = datajson ['player'][1]['strPosition']
			writeHTML(datapoint3)
			print ("This players position is: " + datapoint3)

	if urequest2 == "2":
		urequest7 = input("What would you like to know about Caleb Patterson-Sewell? \n 1: Date of birth \n 2: Nationality \n 3: Position \n")
		if urequest== "1":
			datajson = request.json()
			datapoint4 = datajson ['player'][2]['dateBorn']
			print ("This player's date of birth is: " + datapoint4)
		elif urequest7 == "2":
			datajson = request.json()
			datapoint5 = datajson ['player'][2]['strNationality']
			print ("This player is from: " + datapoint5)
		elif urequest7 == "3":
			datajson = request.json()
			datapoint6 = datajson ['player'][2]['strPosition']
			print ("This players position is: " + datapoint6)

	if urequest2 == "3":
		urequest6 = input("What would you like to know about Víctor Vázquez Solsona? \n 1: Date of birth \n 2: Nationality \n 3: Position \n")
		if urequest6 == "1":
			datajson = request.json()
			datapoint7 = datajson ['player'][3]['dateBorn']
			print ("This player's date of birth is: " + datapoint7)
		elif urequest6 == "2":
			datajson = request.json()
			datapoint8 = datajson ['player'][3]['strNationality']
			print ("This player is from: " + datapoint8)
		elif urequest6 == "3":
			datajson = request.json()
			datapoint9 = datajson ['player'][3]['strPosition']
			print ("This players position is: " + datapoint9)

	if urequest2 == "4":
		urequest7 = input("What would you like to know about Gregory van der Wiel? \n 1: Date of birth \n 2: Nationality \n 3: Position \n")
		if urequest7 == "1":
			datajson = request.json()
			datapoint10 = datajson ['player'][4]['dateBorn']
			print ("This player's date of birth is: " + datapoint10)
		elif urequest7 == "2":
			datajson = request.json()
			datapoint11 = datajson ['player'][4]['strNationality']
			print ("This player is from: " + datapoint11)
		elif urequest7 == "3":
			datajson = request.json()
			datapoint12 = datajson ['player'][4]['strPosition']
			print ("This players position is: " + datapoint12)


	if urequest2 == "5":
		urequest8 = input("What would you like to know about Chris Mavinga? \n 1: Date of birth \n 2: Nationality \n 3: Position \n")
		if urequest8 == "1":
			datajson = request.json()
			datapoint13 = datajson ['player'][5]['dateBorn']
			print ("This player's date of birth is: " + datapoint13)
		elif urequest8 == "2":
			datajson = request.json()
			datapoint14 = datajson ['player'][5]['strNationality']
			print ("This player is from: " + datapoint14)
		elif urequest8 == "3":
			datajson = request.json()
			datapoint15 = datajson ['player'][5]['strPosition']
			print ("This players position is: " + datapoint15)


#************************** TORONTO RAPTORS *************************
if urequest1 == "1":
	print("")
else:
	if userrequest2 == "1":
		userrequest4 = input("What would you like to know about Jozy Altidore? \n 1: Date of birth \n 2: Nationality \n 3: Position \n")
		if userrequest4 == "1":
			datajson = request.json()
			datapoint1 = datajson ['player'][1]['dateBorn']
			print ("This player's date of birth is: " + datapoint1)
		elif userrequest4 == "2":
			datajson = request.json()
			datapoint2 = datajson ['player'][1]['strNationality']
			print ("This player is from: " + datapoint2)
		elif userrequest4 == "3":
			datajson = request.json()
			datapoint3 = datajson ['player'][1]['strPosition']
			print ("This players position is: " + datapoint3)

	if userrequest2 == "2":
		userrequest7 = input("What would you like to know about Caleb Patterson-Sewell? \n 1: Date of birth \n 2: Nationality \n 3: Position \n")
		if userrequest7== "1":
			datajson = request.json()
			datapoint4 = datajson ['player'][2]['dateBorn']
			print ("This player's date of birth is: " + datapoint4)
		elif userrequest7 == "2":
			datajson = request.json()
			datapoint5 = datajson ['player'][2]['strNationality']
			print ("This player is from: " + datapoint5)
		elif userrequest7 == "3":
			datajson = request.json()
			datapoint6 = datajson ['player'][2]['strPosition']
			print ("This players position is: " + datapoint6)

	if userrequest2 == "3":
		userrequest6 = input("What would you like to know about Víctor Vázquez Solsona? \n 1: Date of birth \n 2: Nationality \n 3: Position \n")
		if userrequest6 == "1":
			datajson = request.json()
			datapoint7 = datajson ['player'][3]['dateBorn']
			print ("This player's date of birth is: " + datapoint7)
		elif userrequest6 == "2":
			datajson = request.json()
			datapoint8 = datajson ['player'][3]['strNationality']
			print ("This player is from: " + datapoint8)
		elif userrequest6 == "3":
			datajson = request.json()
			datapoint9 = datajson ['player'][3]['strPosition']
			print ("This players position is: " + datapoint9)

	if userrequest2 == "4":
		userrequest7 = input("What would you like to know about Gregory van der Wiel? \n 1: Date of birth \n 2: Nationality \n 3: Position \n")
		if userrequest7 == "1":
			datajson = request.json()
			datapoint10 = datajson ['player'][4]['dateBorn']
			print ("This player's date of birth is: " + datapoint10)
		elif userrequest7 == "2":
			datajson = request.json()
			datapoint11 = datajson ['player'][4]['strNationality']
			print ("This player is from: " + datapoint11)
		elif userrequest7 == "3":
			datajson = request.json()
			datapoint12 = datajson ['player'][4]['strPosition']
			print ("This players position is: " + datapoint12)


	if userrequest2 == "5":
		userrequest8 = input("What would you like to know about Chris Mavinga? \n 1: Date of birth \n 2: Nationality \n 3: Position \n")
		if userrequest8 == "1":
			datajson = request.json()
			datapoint13 = datajson ['player'][5]['dateBorn']
			print ("This player's date of birth is: " + datapoint13)
		elif userrequest8 == "2":
			datajson = request.json()
			datapoint14 = datajson ['player'][5]['strNationality']
			print ("This player is from: " + datapoint14)
		elif userrequest8 == "3":
			datajson = request.json()
			datapoint15 = datajson ['player'][5]['strPosition']
			print ("This players position is: " + datapoint15)






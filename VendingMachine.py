import sys

RunVM = True

# while RunVM:

print("\n")

price_cc = int(round(2.49, 2))
price_ab = int(round(2.49, 2))
price_kk = int(round(2.49, 2))
price_ck = int(round(0.99, 2))
price_cm = int(round(2.99, 2))
price_wm = int(round(2.05, 2))

print("Select your items: \n")
print(" A1: Crispy Crunch ................ $2.49")
print(" A2: Aero Bar  .................... $2.49")
print(" A3: Kit Kat Bar  ................. $2.49")
print(" A4: Cookies ...................... $0.99")
print(" B1: Chocolate Milk ............... $2.99")
print(" B2: White Milk  .................. $2.05")

print("\n")

food = str(input("What items would you like? \n"))

print("\n")




#************************* PRICE MANAGEMENT *******************************



if food == "A1":
	print("The price of the Crispy Crunch is $" + str(round (price_cc, 2)))
	RunVM = False

elif food == "A2":
	print("The price of the Aero Bar is $" + str(round (price_ab, 2)))
	RunVM = False

elif food == "A3":
	print("The price of the Kit Kat Bar is $" + str(round (price_kk, 2)))
	RunVM = False

elif food == "A4":
	print("The price of the Cookies is $" + str(round (price_ck, 2)))
	RunVM = False

elif food == "B1":
	print("The price of the Chocolate Milk is $" + str(round (price_cm, 2)))
	RunVM = False

elif food == "B2":
	print("The price of the White Milk is $" + str(round (price_wm, 2)))
	RunVM = False
else:
	print("invalid choice")
	print("************************* END OF CODE ************************")
	sys.exit()

quant = int(input("How many would you like? "))

print("\n")

#************************* QUANTITY MANAGEMENT *******************************

print ("\n")

if food == "A1":
	print("Your final price is: \n$" + str(price_cc * quant))
	RunVM = False

elif food == "A2":
	print("Your final price is: \n$" + str(price_cc * quant))
	RunVM = False

elif food == "A3":
	print("Your final price is: \n$" + str(price_cc * quant))
	RunVM = False

elif food == "A4":
	print("Your final price is: \n$" + str(price_cc * quant))
	RunVM = False

elif food == "B1":
	print("Your final price is: \n$" + str(price_cc * quant))
	RunVM = False

elif food == "B2":
	print("Your final price is: \n$" + str(price_cc * quant))
	RunVM = False
else:
	print("invalid choice")
	print("************************* END OF CODE ************************")
	sys.exit()


#print("\n")

#if food == "A1":
	#print("Please Insert:" + str(price_cc))
#elif food == "A2":
	#print("Please Insert:" + str(price_ab))
#elif food == "A3":
	#print("Please Insert:" + str(price_kk))
#elif food == "A4":
	#print("Please Insert:" + str(price_ck))
#elif food == "B1":
	#print("Please Insert:" + str(price_cm))
#elif food == "B2":
	#print("Please Insert:" + str(price_wm))










#************************* MONEY MANAGEMENT *******************************





print("\n")

CashIn= float(input("Please insert the required cost: \n"))

if food == "A1":
	if CashIn == int(price_cc * quant):
		print("Thank You!")
		print("************************* END OF CODE ************************")
	else:
		print("Insufficient Funds")
		print("************************* END OF CODE ************************")
		sys.exit()
elif food == "A2":
	if CashIn == int(price_ab * quant):
		print("Thank You!")
		print("************************* END OF CODE ************************")
	else:
		print("Insufficient Funds")
		print("************************* END OF CODE ************************")
		sys.exit()
elif food == "A3":
	if CashIn == int(price_kk * quant):
		print("Thank You!")
		print("************************* END OF CODE ************************")
	else:
		print("Insufficient Funds")
		print("************************* END OF CODE ************************")
		sys.exit()
elif food == "A4":
	if CashIn == int(price_ck * quant):
		print("Thank You!")
		print("************************* END OF CODE ************************")
	else:
		print("Insufficient Funds")
		print("************************* END OF CODE ************************")
		sys.exit()
elif food == "B1":
	if CashIn == int(price_cm* quant):
		print("Thank You!")
		print("************************* END OF CODE ************************")
	else:
		print("Insufficient Funds")
		print("************************* END OF CODE ************************")
		sys.exit()
elif food == "B2":
	if CashIn == int(price_wm * quant):
		print("Thank You!")
		print("************************* END OF CODE ************************")
	else:
		print("Insufficient Funds")
		print("************************* END OF CODE ************************")
		sys.exit()









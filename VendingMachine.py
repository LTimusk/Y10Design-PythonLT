
RunVM = True

# while RunVM:

print("\n")

price_cc = round(2.49, 2)
price_ab = round(2.49, 2)
price_kk = round(2.49, 2)
price_ck = round(0.99, 2)
price_cm = round(2.99, 2)
price_wm = round(2.05, 2)

print("Select your items: \n")
print(" A1: Crispy Crunch ................ $2.49")
print(" A2: Aero Bar  .................... $2.49")
print(" A3: Kit Kat Bar  ................. $2.49")
print(" A4: Cookies ...................... $0.99")
print(" B1: Chocolate Milk ............... $2.99")
print(" B2: White Milk  .................. $2.05")

food = str(input("What items would you like? \n"))

print("\n")

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

print("\n")

CashIn= float(input("Please insert the required cost: \n"))

if food == "A1":
	if CashIn == price_cc:
		print("Thank You!")
	else:
		print ("It sees: " + str(CashIn))
		print("Insufficient Funds")
elif food == "A2":
	if CashIn == price_ab:
		print("Thank You!")
	else:
		print("Insufficient Funds")
elif food == "A3":
	if CashIn == price_kk:
		print("Thank You!")
	else:
		print("Insufficient Funds")
elif food == "A4":
	if CashIn == price_ck:
		print("Thank You!")
	else:
		print("Insufficient Funds")
elif food == "B1":
	if CashIn == price_cm:
		print("Thank You!")
	else:
		print("Insufficient Funds")
elif food == "B2":
	if CashIn == price_wm:
		print("Thank You!")
	else:
		print("Insufficient Funds")








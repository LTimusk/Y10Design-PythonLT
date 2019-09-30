import sys

RunVM = True

# while RunVM:

amount_cc = 10
amount_ab = 10
amount_kk = 10
amount_ck = 10
amount_cm = 10
amount_wm = 10



print("\n")

price_cc = float(2.49)
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
	print("The price of a Crispy Crunch is $" + str(price_cc))
	RunVM = False

elif food == "A2":
	print("The price of an Aero Bar is $" + str(price_ab))
	RunVM = False

elif food == "A3":
	print("The price of a Kit Kat Bar is $" + str(price_kk))
	RunVM = False

elif food == "A4":
	print("The price of a pack of Cookies is $" + str(price_ck))
	RunVM = False

elif food == "B1":
	print("The price of a Chocolate Milk is $" + str(price_cm))
	RunVM = False

elif food == "B2":
	print("The price of a White Milk is $" + str(price_wm))
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
	if CashIn == float(price_cc * quant):
		print("\n Purchase Valid")
	else:
		print("Insufficient Funds")
		sys.exit()
elif food == "A2":
	if CashIn == float(price_ab * quant):
		print("\n Purchase Valid")
	else:
		print("Insufficient Funds")
		sys.exit()
elif food == "A3":
	if CashIn == float(price_kk * quant):
		print("\n Purchase Valid")
	else:
		print("Insufficient Funds")
		sys.exit()
elif food == "A4":
	if CashIn == float(price_ck * quant):
		print("\n Purchase Valid")
	else:
		print("Insufficient Funds")
		sys.exit()
elif food == "B1":
	if CashIn == float(price_cm* quant):
		print("\n Purchase Valid")
	else:
		print("Insufficient Funds")
		sys.exit()
elif food == "B2":
	if CashIn == float(price_wm * quant):
		print("\n Purchase Valid")
	else:
		print("Insufficient Funds")
		sys.exit()


amountleft_cc = 10 - quant
amountleft_ab = 10 - quant
amountleft_kk = 10 - quant
amountleft_ck = 10 - quant
amountleft_cm = 10 - quant
amountleft_wm = 10 - quant


if food == "A1":
	print("\n There are: " + str(amountleft_cc) + " Crispy crunches left \n ")
elif food == "A2":
	print("\n There are: " + str(amountleft_ab) + " Aero bars left \n ")
elif food == "A3": 
	print("\n There are: " + str(amountleft_kk) + " Kit kats left \n ")
elif food == "A4":
	print("\n There are: " + str(amountleft_ck) + " Cookies left \n ")
elif food == "B1":
	print("\n There are: " + str(amountleft_cm) + " Chocolate milks left \n ")
elif food == "B2":
	print("\n There are: " + str(amountleft_wm) + " White milks left \n ") 


print("Thank you for using Timusk Vending Machines")

print("\n ************************** END OF CODE ***************************")






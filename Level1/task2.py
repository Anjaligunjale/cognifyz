# Task 2: Temperature Conversion


Convert = int(input("Enter option for Temperature to be converted 1. fahrenheit & 2. celsius : "))

if Convert==1:		

	celsius = float(input("Enter temperature in celsius: "))	 # Enter Temperature in celsius degree
 
	fahrenheit = (celsius * 1.8) + 32    # Converting the temperature to Fahrenheit
		
	# printing the result
 
	print(str(celsius )+ " degree Celsius is equal to " + str(fahrenheit )+ " degree Fahrenheit.")


elif Convert==2:    

	fahrenheit =float(input("Enter temperature in farenheit: "))  # Enter Temperature in Fahrenheit degree

	
	celsius = (fahrenheit-32)/1.8  # Converting the temperature to celsius

	# printing the result
	print('%.2f Fahrenheit is equivalent to: %.2f Celsius' % (fahrenheit ,celsius))

else:
	print("Eneterd wrong choice")

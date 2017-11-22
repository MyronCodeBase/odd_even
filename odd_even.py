def odd_even():
	num = int(input("Enter a number "))
	if num % 2 == 0:
		print("The number entered is even")
	else:
		print("The number entered is odd")
	if num % 4 == 0:
		print("The number is also a multiple of 4!")
	check = int(input("Enter another number "))
	if num % check == 0:
		print("Numbers divides evenly!")
	else:
		print("Numbers don't divide evenly")

odd_even()
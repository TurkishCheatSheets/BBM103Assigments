def isPrime(n):
	c = 0
	for i in range(2,n):
		if n % i == 0:
			c = c + 1
	if c == 0:
		return True
	else:
		return False			
			
def factorial(n):
	if n < 1:
		return 1
	else:	
		return n * factorial(n-1)


while True:
	selection = raw_input('What do you want to do ? \n 1. List prime numbers to n \n 2. Calculate combination. \n E: Exit \n > ')
	if selection == "1":
		while True:
			n = input('Please enter the value n: ')
			if type(n) is int:
				for i in range(2,n):
					if isPrime(i):
						print i ,
				print "\n"
				break	
	elif selection == "2":
		while True:
			n = input('Please enter the value n: ')
			r = input('Please enter the value r: ')
			if type(n) and type(r) is int:
				if n > r and n > 0 and r > 0:
					print "C(" + str(n) + "," + str(r) + ") = " + str(factorial(n)/(factorial(r)*factorial(n-r)))
					break
				else:
					print "n bigger than r and values must be possitive !"
	elif selection == "E" or selection == "e":
		break
	else:
		pass	
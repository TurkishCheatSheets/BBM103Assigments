def drawSquare(corner):
	for i in range(0,corner):
		print "*" * corner
	
def drawRectangle(row,column):
	for i in range(0,row):
		print "*" * column

def drawTriangle(row):
	for row in range(0,row + 1):
		print "*" * row


while True:
	selection = raw_input('Which shape want you to draw ? \n Square: S \n Rectangle: R \n Triange: T \n E: Exit \n > : ')
	if selection == "S" or selection == "s":
		while True:
			corner = input('Please enter the corner of square: ')
			if type(corner) is int:
				drawSquare(corner)
				break	
	elif selection == "R" or selection == "r":
		while True:
			row = input('Please enter the row of rectangle: ')
			column = input('Please enter the column of rectangle: ')
			if type(row) is int and type(column) is int:
				drawRectangle(row,column)
				break
	elif selection == "T" or selection == "t":
		while True:
			row = input('Please enter the row of triangle: ')
			if type(row) is int:
				drawTriangle(row)
				break										
	elif selection == "E" or selection == "e":
		break
	else:
		pass		
		

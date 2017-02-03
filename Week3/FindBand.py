import Functions

file = open ('concerts.txt')

band = Functions.userInput("Please enter a band: ", "str")
for line in file:
	if band in line:
		print line,

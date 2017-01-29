import Functions

song = []
verses = []
verses.append(Functions.userInput("Please enter the first verse:", "str"))
verses.append(Functions.userInput("Please enter the second verse:", "str"))
verses.append(Functions.userInput("Please enter the third verse:", "str"))
verses.append(Functions.userInput("Please enter the fourth verse:", "str"))
chorus = Functions.userInput("Please enter the chorus:", "str")
repeat = Functions.userInput("Enter the chorus repeat", "int")

counter = 0
for verse in verses:
	song.append(verse)
	counter = counter+1
	if counter == 4:
		song.append((chorus+ " ") * repeat + chorus)
	else:
		song.append((chorus+ " ") * repeat)

song.append("...one more time...")

counter = 0
for verse in verses:
	song.append(verse)
	counter = counter+1
	if counter == 4:
		song.append((chorus+ " ") * repeat + chorus)
	else:
		song.append((chorus+ " ") * repeat)


print song
print ""
for phrase in song:
	print phrase

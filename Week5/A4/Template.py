import Functions.py

# ------------------------------------------------------------
# For a badge do the following:
#
# After each user query print out the bird that has been seen 
# most often.  If there is a tie, print all of birds that are 
# tied for most sightings.
#
# Allow the user to enter a bird name as often as the like.
# When they want to stop entering bird names they can type 
# 'Exit'.
#
# Make the lookup case insensitive.  In other words, I should
# be able to type ROBIN or RoBiN and get the count for Robin.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# ------------------------------------------------------------
def countBirds(filename):
	d = {}
	for line in filename:
		temp = line.split(',')
		bird = temp[0].strip()
		sights = int(temp[1].strip())
		
		if(bird in d):
			sights = sights + d[bird]
		
		d[bird] = sights
	return d

# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser(d):
    bird =  Functions.userInput("Enter a bird name:", "str")
    return [bird, d[bird]]

def main():
	d = countBirds
	bird = askUser(d)
    while not(bird[0].lower() == 'exit'):
		print "%s -> %s" % (bird[0], bird[1])
		bird = askUser(d)
    
main()

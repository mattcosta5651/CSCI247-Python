import Functions

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
	for line in open(filename):
		temp = line.split(',')
		bird = temp[0].strip().lower()
		
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
	if bird == 'exit':
		return [bird, -1] #returns exit prompt
		
	return [bird, d[bird]]

def commonBird(d):
	maxSight = -1
	maxBird = []

	for sight in d.values():
		if sight >= maxSight:
			maxSight = sight
			
	for bird in d.keys():
		if d[bird] == maxSight:
			maxBird.append(bird)
	
	return maxBird

def main():
	d = countBirds("Birds.txt")
	bird = askUser(d)
	while not(bird[0] == 'exit'):
		print "I've seen that bird %s times" % (bird[1])
		print "The most common bird(s): %s" % (commonBird(d))
		bird = askUser(d)
    
main()

# ------------------------------------------------------
# reads the speeds in the specified file (filename)
# and returns them as a list of integers
# ------------------------------------------------------
def readData(filename):
    file = open (filename)
    speeds = [] 
    
    for line in file:
		speeds.append(float(line))
		
    return speeds
# ------------------------------------------------------    
# calculates and returns the average of the numbers
# in the the specified list (l)
# ------------------------------------------------------
def getAverage(l):
	total = 0
	for data in l:
		total = total + data
	return total/len(l)
    
# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or 
# equal to maxSpeed
# ------------------------------------------------------
def countSpeeders(l, maxSpeed):
	speeders = []
	for speed in l:
		if speed >= maxSpeed:
			speeders.append(speed)
	return len(speeders)
    
# ------------------------------------------------------
# Determines the number of people speeding during 
# rush hour and not during rush hour.  Also determines
# the total fines during rush hour and not during 
# rush hour.  A person is considered speeding if they
# are traveling faster than 69 MPH.  The fine for 
# speeding during rush hour is $150.  The fine for 
# speeding not during rush hour is $100.
#
# THE CORRECT OUTPUT IS:
#
# The average speed during rush hour was 63.47.
# The average speed not during rush hour was 64.07.
# There were 4 speeders during rush hour.  Total fine = $600
# There were 6 speeders not during rush hour.  Total fine = $600
# ------------------------------------------------------
def main():
	norush = readData("data-not-rush.txt")
	rush = readData("data-rush.txt")
	
	print "The average speed during rush hour was %.2f" % getAverage(rush)
	print "The average speed not during rush hour was %.2f" % getAverage(norush)
	print "There were %s speeders during rush hour. Total fine is %s" % (countSpeeders(rush, 70),(150*countSpeeders(rush, 70)))
	print "There were %s speeders not during rush hour. Total fine is %s" % (countSpeeders(norush, 70),(100*countSpeeders(norush, 70)))

# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------------------------
main()

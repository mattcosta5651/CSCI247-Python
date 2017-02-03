#Program written by Matthew Costa
#CSCI-247 Assignment 3 

import Functions

temps = []

#reads the temperatures into a list
def readTemps():
	file = open('temps.txt')
	for line in file:
		temps.append(float(line)) #floats are the desired primitive

#calculates the average temperature in a time period
def calcAverageTemp(temps, start, stop):
	tempSpan = []
	
	for index in range(len(temps)):
		if index >= start and index <= stop: #checks that the temperature is within specified range (inclusive)
			tempSpan.append(temps[index])
	
	return Functions.calcAverage(tempSpan) #function that calculates the average of a data set and returns the result
	
#counts temperatures with positive deviation
def count(temps, start, stop):
	posTemps = []
	for index in range(len(temps)):
		if index >= start and index <= stop: #checks that the temperature is within specified range (inclusive)
			if temps[index] > 0: 			 #checks that the temperature is greater than 0
				posTemps.append(temps[index])#appends temperature to array of positive temperatures
				
	return len(posTemps) #returns length of the positive temperatures array

#main function
def main():
	readTemps()
	print 'During the first 81 years, the average deviation from the temperature anomoly is: %s' % (calcAverageTemp(temps, 0, 80))
	print 'During the first 81 years, %s had a positive temperatue anomoly' % (count(temps, 0, 80))
	print 'During the last 35 years, the average deviation from the temperature anomoly is %s' % (calcAverageTemp(temps, len(temps)-35, len(temps)))
	print 'During the last 35 years, %s had a positie temperature anomoly' % (count(temps, len(temps)-35, len(temps)))
	
main()
	

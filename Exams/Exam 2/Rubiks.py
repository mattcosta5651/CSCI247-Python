#dictionary of category to index
d = {"Cube Head (0-9.99)" : 0, 
		"Square Master (10-19.99)" : 1,
			"Advanced Twister (20-29.99)" : 2,
				"Intermediate Turner (30-39.99)": 3,
					"Average Mover (40-59.99)" : 4,
						"Pathetic (60 and beyond)" : 5}

#reads times and returns a dictionary
def readTimes(filename):
	d = {}
	
	for line in open(filename):
		att = line.split(',')
		d[att[0]] = float(att[1].strip())
		
	return d

#sorts dictionary into dictionary of lists and redirects pointer
def sortTimes(dictionary):
	#list of categories: category = dictionary to list
	l = [[],[],[],[],[],[]]

	for key in dictionary.keys():
		l[d.get(categorizeTime(dictionary.get(key)))].append(key)

	return l

#categorizes a single time accordingly
def categorizeTime(time):
	
	if time <= 9.99:
		return "Cube Head (0-9.99)"
	elif time > 9.99 and time <= 19.99:
		return "Square Master (10-19.99)"
	elif time > 19.99 and time <= 29.99:
		return "Advanced Twister (20-29.99)" 
	elif time > 20.99 and time <= 39.99:
		return "Intermediate Turner (30-39.99)"
	elif time > 39.99 and time <= 59.99:
		return "Average Mover (40-59.99)"
	else:
		return "Pathetic (60 and beyond)"

def main():
	times = readTimes("timings.txt")
	categories = sortTimes(times)

	#for each list in categories
	for l in categories:
		print categorizeTime(times.get(l[0]))+':' #prints the category name by getting the first name and analyzing time
		for name in l: #for each name in the category
			print '\t'+name

	
main();

import Functions
import os

def readFiles():
	files = os.listdir(".")
	
	for fileName in files:
		if not ".txt" in fileName:
			files.remove(fileName)
			
	return files
	

def getHits(term, fileName):
	lines = []
	for line in open(fileName):
		if term.upper() in line.upper():
			lines.append(line.upper().strip())
			
	return lines

def main():
	files = readFiles()
	
	term = Functions.userInput("Enter a search term:", "str")
	print ""
	
	hits = {}
	for fileName in files:
			hits[fileName] = getHits(term, fileName)
			
	for hit in hits.keys():
		for line in hits.get(hit):
			print "%s : %s" % (hit, line) 

main()

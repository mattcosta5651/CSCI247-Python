import json
import Functions

def readFile(filename):
	classes = ""
	for line in open(filename):
		line = line.strip()
		classes = classes+line
	return json.loads(classes)

def validateInput(classes, name):
	if not type(name) is str:
		print "That was not a string"
	else: 
		found = False
		for classObj in classes:
			if name in classObj.values():
				found = True
		if not found:	
			print "That professor is not in the JSON"

		
def printResult(classes, name):
	for classObj in classes:
		if classObj["Professor"].upper() == name.upper():
			print classObj["Title"]
	
def main():
	classes = readFile("classes.json")
	name = Functions.userInput("Enter a professor's last name:", "str")
	validateInput(classes, name)
	printResult(classes, name)
	
	
main()

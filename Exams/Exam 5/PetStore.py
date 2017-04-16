import json
import Functions

#reads JSON from a file
def readFile(filename):
	products = ""
	for line in open(filename):
		line = line.strip()
		products = products+line
	return json.loads(products)

#maps categories to list of products in category
def mapCategories(json):
	d = {}
	
	for obj in json:
		if not(obj.get("Category") in d.keys()):
			d[obj.get("Category")] = []
		
		d.get(obj.get("Category")).append(obj.get("Product"))
	
	return d

def getPrice(name, products):
	for obj in products:
		if obj.get("Product").upper() == name.upper():
			return obj.get("Price") 

#performs correct search given input
def findProduct(readLine, products, categories):
	#######################################################################
	#Category search
	if readLine.upper() == "C":
		category = Functions.userInput("Enter a category:", "str")
		
		for key in categories.keys():
			if key.upper() == category.upper():
				for product in categories.get(key):
					print "%s - %s" % (product, getPrice(product, products))
	########################################################################		
	#Keyword search	
	elif readLine.upper() == "K":
		keyword = Functions.userInput("Enter a keyword:", "str")
		
		for obj in products:
			if keyword.upper() in obj.get("Product").upper():
				print "%s - %s" % (obj.get("Product"), obj.get("Price"))
	########################################################################
	#Invalid input
	else:
		print "Try again with valid input"

def main():
	products = readFile("PetStore.json")
	categories = mapCategories(products)
	
	readLine = Functions.userInput("Search by category (c) or keyword (k):", "str")
	findProduct(readLine, products, categories)  
	
main()

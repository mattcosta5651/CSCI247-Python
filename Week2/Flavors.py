import Functions

ratings = []
flavors = ['vanilla', 'chocolate', 'strawberry', 'bacon']

for flavor in flavors:
	ratings.append(Functions.userInput("Please rate %s from 1 to 5:" % flavor, "str"))

counter = 0
for rate in ratings:
	print flavors[counter]+" was rated as a %s" % rate
	counter = counter + 1

import Functions

def makeClues():
	d = {}
	d["weapons"] = ["Candlestick", "Wrench", "Pipe"]
	d["suspects"] = ["Miss Scarlet", "Col Mustard", "Mr Green"]
	
	return d

def calcPossibilities(clues, clue=None):
	if not(clue == None): 
		for l in clues.values():
			if clue in l:
				l.remove(clue)
		
	possibilities = []
	
	lists = []
	for l in clues.values():
		lists.append(l)
		
	for w in lists[0]:
		for s in lists[1] :
			possibility = "%s with the %s" % (s, w)
			possibilities.append(possibility)
	
	return possibilities

def getClue(clues):
		#gets the type of clue
	def getType():
		category = Functions.userInput("Is the clue a weapon (w) or a suspect (s)?", "str")
		
		if category.upper() == "W":
			return "weapons"
		elif category.upper() == "S":
			return "suspects"
		else:
			print "Enter a valid category."
			return getType()
	
	#gets the item from appropriate list
	def getItem(t):
		n = Functions.userInput("Enter the name:", "str")
		
		if n.title() in clues.get(t):
			return n.title()
		else:
			print "That isn't in the list!"
			return getItem(t)
			
	typ = getType()
	return getItem(typ)
	
	
def main():
	#make all the options
	options = makeClues()
	
	#nothing is known, so all options are possible
	clues = makeClues()
	
	#list of every possibility
	p = calcPossibilities(clues)
	
	found = False
	while not(found):
		if len(p) == 1:
			found = True
			print "\nIt was %s" % p[0]
		else:
			print "%s possibilities left\n" % len(p)
			clue = getClue(clues)
			p = calcPossibilities(clues, clue)
			print "---------------------------"
main()

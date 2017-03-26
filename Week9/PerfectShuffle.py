import Functions

ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

def buildDeck():	
	return [rank+" of "+suit for rank in ranks for suit in suits]

def shuffle(deck):
	half1 = deck[:len(deck)/2]
	half2 = deck[len(deck)/2:]
	
	newDeck = []
	
	count = 0
	for i in range(len(deck)):
		if i%2 == 0:
			newDeck.append(half1[count])
		else:
			newDeck.append(half2[count])
			count = count + 1
	
	return newDeck
	
def deal(deck):
	return deck[:5]
	
def main():
	deck = buildDeck()
	
	shuffleCount = Functions.userInput("How many times would you like to shuffle?", "int")
	
	for i in range(0, shuffleCount):
		deck = shuffle(deck)
		
	print deal(deck)
	
main()

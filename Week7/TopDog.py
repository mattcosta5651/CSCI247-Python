import Functions
import random
import time

contestants = {"Tom": 0, "Sally": 0, "Fred": 0}
cash = 100

def getGuess():
	global cash
	guess = {}
	name = Functions.userInput("Guess a winner (%s, %s, %s): " % (contestants.keys()[0],contestants.keys()[1],contestants.keys()[2]) , "str")
	
	#prevents invalid name
	if name in contestants.keys():
		guess["name"] = name
	else:
		print "Contestant does not exist; Try again"
		getGuess()
		
	bet =  Functions.userInput("Enter a bet (cash = %i):" % cash, "int")
	
	#prevents invalid bet
	if(bet <= cash):
		guess["bet"] = bet
		cash = cash - bet
	else:
		print "Bet exceeds cash; Try again"
		getGuess()
	
	#returns a dictionary of name and bet
	return guess

def eat():
	eating = True
	global contestants
	
	while eating:
		#increments hot dogs
		print "chomp chomp chomp..."
		#time.sleep(1)
		for contestant in contestants.keys():
			contestants[contestant] = contestants.get(contestant) + random.randrange(1, 6)
			print "%s : %i dogs" % (contestant, contestants.get(contestant))
		
		#checks to see if there is a winner
		for dogs in contestants.values():
			if dogs > 50:
				for contestant in contestants.keys():
					if contestants.get(contestant) == dogs:
						return contestant
						eating = False

def checkGuess(guess, winner):
	global cash
	global contestants
	print "Top Dog is %s \n" % winner
	
	if guess["name"] == winner:
		print "You guessed right!"
		print "You won $%i!\n" % (guess["bet"]*3)
		cash = cash + guess["bet"]*3
	else:
		print "You guessed wrong!"
		print "You lost $%i!\n" % guess["bet"]
	
	if(cash > 0 ):
		contestants = {"Tom": 0, "Sally": 0, "Fred": 0}
		main()
	else:
		print "You're out of cash!"

def main():
	guess = getGuess()
	checkGuess(guess, eat())
	
main()

import Functions
import random

cards = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']

def makeDeck():
    deck = cards
    deck.append(cards[random.randrange(0, len(cards))])
    
    return deck

def pickCard(first, deck):
    if(first):
        index = Functions.userInput("Pick the first card to turn over (0 to 9): ", "int")
    else:
        index = Functions.userInput("Pick the second card to turn over (0 to 9): ", "int")
    
    return index

def validate(c1, c2, deck):
    if((c1 >=0 and c1 <=9) and (c2 >=0 and c2 <=9)):
        if(not(c1 == c2)):
            return True
    
    print "Invalid choices. You must pick different cards and the card must be a number 0-9"

def checkWin(c1, c2):
    if(c1 == c2):
        return True
    return False

def main():
    deck = makeDeck()
    random.shuffle(deck)
    
    tries = 0
    
    while(True):
        tries = tries + 1
        c1 = pickCard(True, deck)
        c2 = pickCard(False, deck)
        
        if(validate(c1, c2, deck)):
            print "Card %s is a %s" % (c1, deck[c1])
            print "Card %s is a %s" % (c2, deck[c2])            
            if(checkWin(deck[c1], deck[c2])):
                break
        else:
            continue
        
    print "You win! It took you %s tries." % tries

main()
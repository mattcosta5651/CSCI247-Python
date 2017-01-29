# importing module from folder up?
#import sys
#sys.path.insert(0, '/home/Documents/Programming in Python/CSCI247-Python/')

import Functions
	
adjective = Functions.userInput("Enter an adjective :", "str")
adjective2 = Functions.userInput("Enter another adjective:", "str")
pluralNoun = Functions.userInput("Enter a plural noun:", "str")
pluralNoun2 = Functions.userInput("Enter another plural noun:", "str")
noun = Functions.userInput("Enter a noun:", "str")
celebrity = Functions.userInput("Enter a celebrity:", "str")

sentence = ("In the shadowy world of spies, a/an ADJ1 organization like the US Government uses spies to infiltrate ADJ2 groups for "
"the purpose of obtaining top secret PLN1. A teacher, CEL,"
" or even the little old PLN2 with a cane and fifteen pet NOUN could be a spy." )
sentence = sentence.replace ("ADJ1", adjective)
sentence = sentence.replace ("ADJ2", adjective2)
sentence = sentence.replace ("PLN1", pluralNoun)
sentence = sentence.replace ("PLN2", pluralNoun2)
sentence = sentence.replace ("NOUN", noun)
sentence = sentence.replace ("CEL", celebrity)

print sentence

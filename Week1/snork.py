print "Please enter a sentence:",
sentence = raw_input()

length = len(sentence)
encrypted = sentence
encrypted = sentence.replace("a", str(length))
encrypted = encrypted.replace("e", str(length+1))
encrypted = encrypted.replace("i", str(length+2))
encrypted = encrypted.replace("o", str(length+3))
encrypted = encrypted.replace("u", str(length+4))

print "The encrypted sentence is %s" % encrypted
print "The decrypted sentence is %s" % sentence

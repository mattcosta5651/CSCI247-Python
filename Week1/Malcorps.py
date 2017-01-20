print "How many malcorps did you find on Exflon?",
e = raw_input()
print "How many malcorps did you find on Mobile?",
m = raw_input()
print "How many malcorps did you find on Monsan?",
x = raw_input()

total = int(e)+int(m)+int(x)
print "You found %s malcorps!" % total 
print "The average malcorps per planet is %.2f" % (total/3.0)

print "Enter the amount of flour (cups)",
flour = float(raw_input())
print "Enter the amount of water (cups)",
water = float(raw_input())
print "Enter the amount of salt (teaspoons)",
salt = float(raw_input())
print "Enter the amount of yeast (teaspoons)",
yeast = float(raw_input())
print "Enter the loaf adjustment factor (e.g. 2.0 to double the size",
factor = float(raw_input())

print " "
print "--Modified Recipe--"
print "Flour: %.2f cups." % (flour*factor)
print "Water: %.2f cups." % (water*factor)
print "Salt: %.2f teaspoons." % (salt*factor)
print "Yeast: %.2f teaspoons." % (yeast*factor)
print " "
print "Happy Baking!"
print " "
print " "
print "--Modified Recipe in Grams--"
print "Flour: %.2fg." % (flour*factor*136)  #128 = bread flour cups to grams
print "Water: %.2fg." % (water*factor*230)  #230 = water cups to grams
print "Salt: %.2fg." % (salt*factor*5)      #4.93 = salt tsp to grams 
print "Yeast: %.2fg." % (yeast*factor*3)    #2.83 = yeast tsp to grams
print " "
print "Happy Baking!"

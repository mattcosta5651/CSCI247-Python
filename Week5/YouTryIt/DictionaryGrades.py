d = {}
for line in open("DictionaryGrades.txt"):
	temp = line.split(":")
	tempGrades = temp[1].split(',')
	grades = []
	for grade in tempGrades:
		grades.append(grade.strip())
		
	d[temp[0]] = grades	
	
print "Enter a name: "
name = raw_input()

if name in d.keys():
	print d[name]
else:
	print "That name is unsupported"

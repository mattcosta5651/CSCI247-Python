#@param prompt - the prompt for the user's input
#@param returnType - the intended type of the input
#@return - the raw_input as appropriate type  
def userInput(prompt, returnType):
	print prompt,
	val = raw_input()
	if returnType == "str":
		return str(val)
	elif returnType == "int":
		return int(val)
	elif returnType == "float":
		return float(val)
	elif returnType == "list":
		return [val]
	else: #no type specified 
		return val
	
	

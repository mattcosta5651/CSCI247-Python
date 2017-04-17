import json
import Functions
import urllib2
import urllib

def readWeather():
	location = Functions.userInput("Enter a zip code or city name:", "str")
			
	data = {}
	data["key"] = "713b8c0fa59e4548820201255173003"
	data["q"] = location
	
	values = urllib.urlencode(data)
	
	url = "https://api.apixu.com/v1/current.json"+"?"+values
	
	weather = ""
	data = ""
	
	#error handling
	try:
		weather = urllib2.urlopen(url)
	except urllib2.HTTPError as e:
		print "Please enter a valid location.\n"
		return readWeather()
		
	data = weather.read()
	return json.loads(data)

def askAgain():
	again = Functions.userInput("Would you like to get weather for another location? (y/n)", "str")
	if again.lower() == "y":
		print ""
		return True
	elif again.lower() == "n":
		print ""
		return False
	else:
		print "Please enter a valid command"
		askAgain()

def main():
	while(True):
		weather = readWeather()
		
		units = Functions.userInput("Enter a temperature unit (F/C)", "str")
		
		print""
		print "Here is the current weather for %s, %s \n" % (weather.get("location").get("name"), weather.get("location").get("region")),
		print "%s and %s degrees (%s)\n" % (weather.get("current").get("condition").get("text"), weather.get("current").get("temp_"+units.lower()), units.upper()),
		print "It actually feels like %s degrees (%s)" % (weather.get("current").get("feelslike_"+units.lower()), units.upper())
		print ""
				
		if askAgain():
			continue
		else:
			break

	
main();

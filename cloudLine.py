import json, requests, urllib2, time

location = raw_input ("Enter location: ")

location = urllib2.quote (location)

print "Loading weather ..."

url = "http://api.openweathermap.org/data/2.5/forecast/daily?q="+location+"&mode=json&units=metric&cnt=3"

response = requests.get (url)

if response.status_code == 200:
	weather = response.json()
	days = weather['list']
	for day in days:
		date = time.strftime ("%B %d, %a %Y", time.localtime (int(day['dt'])))
		main = day['weather'][0]['main']
		description = day['weather'][0]['description']
		temp_min = day['temp']['min']
		temp_max = day['temp']['max']
		pressure = day['pressure']
		humidity = day['humidity']
		print date
		print ("--%s (%s)") % (main, description)
		print ("--Temperature")
		print ("----min: %s") % (temp_min)
		print ("----max: %s") % (temp_max)
		print ("--Pressure: %s") % (pressure)
		print ("--Humidity: %s") % (humidity)

else:
	print "Err. Can't load resource. :("
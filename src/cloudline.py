#!/usr/bin/python

import json, requests, urllib2, time

import sys, getopt

"""
# Command line arguments:
	-l "location string" - location to get weather for
	-d int - count of days to show weather
"""

params, args = getopt.getopt(sys.argv[1:],"l:d:")

location = ""
days = 3
error = False

for p,a in params:
	if p == "-l":
		if a:
			location = a
		else:
			error = True
	elif p == "-d":
		try:
			days = int (a)
		except ValueError:
			error = True

if error or not location:
	# print help message
	print "Usage: cloudline -l \"location string\" -d day_count"
	sys.exit (0)

location = urllib2.quote (location)

url = "http://api.openweathermap.org/data/2.5/forecast/daily?q="+location+"&mode=json&units=metric&cnt="+str(days)

#print url

response = requests.get (url)

if response.status_code == 200:
	weather = response.json()
	code = weather['cod']
	if code == "404":
		print "Sorry, location not found."
		sys.exit (0)
	elif code == "200":
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
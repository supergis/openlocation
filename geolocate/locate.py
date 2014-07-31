from geoip import geolite2

strIP = '17.0.0.1'
match = geolite2.lookup(strIP)
if match is not None:
	print "IP:" + strIP
	print "=>Country: "+match.country
	print "=>Continent: "+match.continent
	print "=>Timezone: "+match.timezone
	print "=>SubDiv: "+str(match.subdivisions)
	print "=>Location: "+str(match.location)

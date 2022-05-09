from geopy.geocoders import GoogleV3
geolocator = GoogleV3()

location = geolocator.geocode("29 Lascelles Boulevard, Toronto, Ontario", timeout=10)
print location
print (location.longitude, location.latitude)

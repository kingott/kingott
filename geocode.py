#import the csv module
import csv
#import the shutil module for creating a copy of our original csv
import shutil
#import time for time delay
import time

from geopy.geocoders import GoogleV3

geolocator = GoogleV3(api_key="insert key here")

#create copy of our raw file for backup
shutil.copyfile("raw.csv","processed.csv")

#open the file and assign it to the var f
f = open('raw.csv')

#create a blank array for addresses
addresses = []

#use the csv reader
csv_f = csv.reader(f)

#iterate through each row, and only grab column 1, and add it to the address array
for row in csv_f:
   addresses.append(row[0])

#close original file
f.close()

#create a new empty array called locations
locations = []
address = []

#for each value in the addresses array that we created earlier geocode it and save it to a variable called location, we'll then append that single location to the locations variable
for val in addresses:
   location = geolocator.geocode([val], timeout=30)
   print (location.longitude, location.latitude), location
   locations.append((location.longitude, location.latitude))
   address.append(location)
   #time.sleep(1)
  
#Create a header row for our new csv
header = ['Type','Full Address','Street','City','Province','Country','Postal','COORDINATES','Address']

#open the original csv and grab all the data, place it in a var called data, and close the file again
f = open('raw.csv')
data = [item for item in csv.reader(f)]
f.close()

#create a blank array
new_data = []

#for each item in data append a location, then add the complete item to the new data variable
for i, item in enumerate(data):
   item.append(locations[i])
   item.append(address[i])
   new_data.append(item)
   

#open the new csv and write the header row followed by a row for each object in the new_data array
f = open('processed.csv', 'w')
csv.writer(f, lineterminator='\n').writerow(header)
csv.writer(f, lineterminator='\n').writerows(new_data)
f.close()

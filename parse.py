import requests
import json

origin = raw_input("Please Enter Origin: ");
destination = raw_input("Please Enter Destination: ")

response = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin="+origin+"&destination="+destination+"&key=AIzaSyCICZw-UdjfKnICOvkPsHySr007pgeEdPo")
output = ""
coordinates = []

for i in response.json()['routes'][0]['bounds']:
	coordinates.append(response.json()['routes'][0]['bounds'][i])


output+="Coordinates of Starting Point: Latitude= {}, Longitude={}\n".format(coordinates[0]['lat'], coordinates[0]['lng'])
output+="Coordinates of EndPoint: Latitude= {}, Longitude={}\n".format(coordinates[1]['lat'], coordinates[1]['lng'])
output+="Distance Apart: {} \n".format(response.json()['routes'][0]['legs'][0]['distance']['text'])
output+="Steps involved in getting to destination: \n"

for i in range(len(response.json()['routes'][0]['legs'][0]['steps'])):
	distance = response.json()['routes'][0]['legs'][0]['steps'][i]['distance']['text']
	lat = response.json()['routes'][0]['legs'][0]['steps'][i]['end_location']['lat']
	lon = response.json()['routes'][0]['legs'][0]['steps'][i]['end_location']['lng']
	output+="Step {}, Latitude: {}, Longitude: {}, Distance: {} \n".format(i, lat, lon, distance)

print output

with open('data.txt', 'w') as f:
  f.write(output)
  f.close()












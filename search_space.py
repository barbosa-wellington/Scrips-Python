import urllib.request
import json
import turtle


url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ', lat)
print('Longitude: ', lon)

# Identificando no mapa a possição da space

screen = turtle.Screen()
screen.setup(1336, 640)
#screen.bgcolor("blue")
screen.setworldcoordinates(-180,-90, 180, 90)
screen.bgpic('world-map.png')

# This command will create a turtle shape on the map
astronalt = turtle.Turtle()
print(type(astronalt))
astronalt.shape("turtle")
astronalt.setheading(100)
astronalt.penup()
astronalt.goto(lon, lat)

#import ImageTk, Image
#img = ImageTk.PhotoImage(Image.open("worldmap.png"))  
#l=Label(image=img)
#l.pack()

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
screen.setup(1200, 600)
#screen.bgcolor("blue")
#screen.done()
screen.setworldcoordinates(-180,-90, 180, 90)
screen.bgpic('world-map.png')

#import ImageTk, Image
#img = ImageTk.PhotoImage(Image.open("worldmap.png"))  
#l=Label(image=img)
#l.pack()

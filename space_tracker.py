import requests
import webbrowser
import time
import turtle

astronaut_data = 'http://api.open-notify.org/astros.json'

result = requests.get(astronaut_data).json()

print('People in space {}'.format(result['number']))

for person in result['people']:
    print(person['name'] + ' in ' + person['craft'])

iss_location = 'http://api.open-notify.org/iss-now.json'

result = requests.get(iss_location).json()

while True:
    timestamp = result['timestamp']
    lat = result['iss_position']['latitude']
    lon = result['iss_position']['longitude']
    print(str(timestamp)+ ' ' + lat + ' ' + lon)

    screen = turtle.Screen(visible=False)
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('NASA_World_Map.gif')
    turtle.Turtle()
    screen.register_shape('ISS.gif')
    iss = turtle.Turtle()
    iss.shape('ISS.gif')
    iss.penup()
    iss.goto(float(lat), float(lon))
    iss.showturtle()
    turtle.mainloop()

    time.sleep(.1)



#gmaps_iss = "http://maps.google.com/?q={},{}".format(lat, lon)
#webbrowser.open_new_tab(gmaps_iss)

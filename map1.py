import folium
import pandas


map = folium.Map(location=[35.56, -99.90], zoom_start=6, tiles = "Stamen Terrain")
data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'         


fg = folium.FeatureGroup(name="My Map")
# fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[38.01, -99.1], popup="Hi I am a Second Marker", icon=folium.Icon(color='blue')))



for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el) +" meters",
     fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))
   

map.add_child(fg)

map.save("Map1.html")
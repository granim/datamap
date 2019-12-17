import folium
import pandas


map = folium.Map(location=[35.56, -99.90], zoom_start=6, tiles = "Stamen Terrain")
data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])


fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[38.01, -99.1], popup="Hi I am a Second Marker", icon=folium.Icon(color='blue')))

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt,ln], popup="Hi I am a Marker", icon=folium.Icon(color='purple')))
   

map.add_child(fg)

map.save("Map1.html")
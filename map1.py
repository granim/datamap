import folium
import pandas


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

#Create the map object             
map = folium.Map(location=[35.56, -99.90], zoom_start=6, tiles = "Stamen Terrain")
#Feature group for Volcanoes in the US
fgv = folium.FeatureGroup(name="Volcanoes")
#Add information to the FG Volcanoes
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el) +" meters",
     fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))

#Feature group for Population density
fgp = folium.FeatureGroup(name="Population")
#Add information to the FG Population
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000 
else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))




# PJG54ERUYT5
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
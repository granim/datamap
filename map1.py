import folium

map = folium.Map(location=[35.56, -99.90], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[38.01, -99.1], popup="Hi I am a Second Marker", icon=folium.Icon(color='blue')))
map.add_child(fg)

map.save("Map1.html")
import folium

# Create my map object
map = folium.Map(location=[42.3601, -71.0689], zoom_start=10)

#Global ToolTip
tool_tip = 'Click For More Info'

#Create custom marker icon 
# logoIcon = folium.features.CustomIcon('logo.png', icon_size=(50,50))

# Create Markers
folium.Marker([42.363600, -71.0995500], popup='<strong>Location One', tooltip=tool_tip,
               icon=folium.Icon(color='purple')).add_to(map)
folium.Marker([42.333600, -71.109500], popup='<strong>Location One', tooltip=tool_tip,
               icon=folium.Icon(icon='cloud')).add_to(map)
folium.Marker([42.433600, -71.109500], popup='<strong>Location One', tooltip=tool_tip,
               icon=folium.Icon(color='white', icon='leaf', icon_color='green')).add_to(map) 
# folium.Marker([42.234300, -71.239500], popup='<strong>Location One', tooltip=tool_tip,
#                icon=logoIcon).add_to(map) 

#Circle marker
folium.CircleMarker(
    location=[42.466470, -70.942110],
    radius=50,
    popup='Some Text',
    color="#428bca",
    fill=True,
    fill_color='#428bca'
).add_to(map)



#Generate html file
map.save("SecondMap.html")
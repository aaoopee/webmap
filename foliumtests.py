import folium
import pandas

data = pandas.read_csv("volcanoes.csv")

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])


map = folium.Map(
    location=[64.962090, 25.366749],
    zoom_start=15,
    tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, nm in zip(lat, lon, name):
    fg.add_child(folium.Marker(
        location=[lt, ln],
        popup=nm,
        icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")



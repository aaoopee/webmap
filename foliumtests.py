import folium
import pandas

def select_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


volc_data = pandas.read_csv("volcanoes.csv")
world_data = open("world.json", "r", encoding="utf-8-sig").read()

lat = list(volc_data["LAT"])
lon = list(volc_data["LON"])
name = list(volc_data["NAME"])
elev = list(volc_data["ELEV"])


map = folium.Map(
    location=[64.962090, 25.366749],
    zoom_start=2,
    tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nm, el in zip(lat, lon, name, elev):
    fgv.add_child(folium.CircleMarker(
        location=[lt, ln],
        popup = nm + ", "+str(el)+".",
        radius = 6, 
        fill_color = select_color(el),
        fill_opacity = 0.7,
        color='grey'))

fgw = folium.FeatureGroup(name="Countries")
fgw.add_child(folium.GeoJson(
    world_data,
    style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgw)

map.add_child(folium.LayerControl())

map.save("Map1.html")



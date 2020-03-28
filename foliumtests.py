import folium

map = folium.Map(
    location=[64.962090, 25.366749],
    zoom_start=15,
    tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(
    location=[64.962090, 25.366749],
    popup="Hi, I am a Marker",
    icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")



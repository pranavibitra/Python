import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data['ELEV'])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

def color_pick(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map= folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

feagrpv= folium.FeatureGroup(name="Volcanoes")

#for coordinates in [[38.2, - 99.1],[35.2, - 96.1]]:
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width= 200, height =100)
    feagrpv.add_child(folium.Marker(location=[lt, ln], popup = folium.Popup(iframe), icon = folium.Icon(color = color_pick(el))))

feagrpp= folium.FeatureGroup(name="Population")

feagrpp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(feagrpv)
map.add_child(feagrpp)
map.add_child(folium.LayerControl())

map.save("map1.html")

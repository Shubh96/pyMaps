import folium as fl
import pandas as pd

map = fl.Map(location = [38, -99], tiles = "Mapbox Bright", zoom_start = 6)
volcanoLayer = fl.FeatureGroup(name = "Volcano Layer")
populationLayer = fl.FeatureGroup(name = "Population Layer")

locations = pd.read_csv("Volcanoes_USA.txt")

latitudes = list(locations["LAT"])
longitudes = list(locations["LON"])
volcanoName = locations["NAME"]
elevation = locations["ELEV"]
vtype = locations["TYPE"]
status = locations["STATUS"]

# Color codes
#FCFF00 : Yellow        #62FF00: Green        #008DFF: Blue        #FF6000: Orange        #FF0000: Red        #62FF00: black
styleFunc = lambda sf: {'fillColor': '#FCFF00' if sf['properties']['POP2005'] < 10000000 else '#62FF00' if 10000000<= sf['properties']['POP2005'] < 20000000
            else '#008DFF' if 20000000<= sf['properties']['POP2005'] < 30000000 else '#FF6000' if 30000000<= sf['properties']['POP2005'] < 40000000
            else '#FF0000' if 40000000<= sf['properties']['POP2005'] < 50000000 else '#000000'}

def returnColor(elevation):
    if elevation<= 1000:
        return 'green'
    elif elevation> 1000 and elevation<=2000:
        return 'blue'
    elif elevation> 2000 and elevation<=3000:
        return 'orange'
    elif elevation> 3000 and elevation<=4000:
        return 'red'
    else:
        return 'darkred'

#cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Hyderabad", "Bangalore", "Ahmedabad", "Pune", "Surat"]
#metropolis = [[28.7041, 77.1025], [19.0760, 72.8777], [22.5726, 88.3639], [13.0827, 80.2707], [17.3850, 78.4867], [12.9716, 77.5946], [23.0225, 72.5714], [18.5204, 73.8567], [21.1702, 72.8311]]

populationLayer.add_child(fl.GeoJson(data = (open('Population.json', encoding = 'utf-8-sig')).read(), style_function = styleFunc))

for lat, lon, vname, tp, stat, elev in zip(latitudes, longitudes, volcanoName, vtype, status, elevation):

    #iconType = fl.Icon(color = returnColor(elev), icon_color = 'black', icon = 'fa-circle', prefix = "fa")

    vname = vname.replace("'", "")
    vname = "Volcano Name: " + vname
    tp = tp.replace("'", "")
    tp = "Volcano Type: " + tp
    stat = stat.replace("'", "")
    stat = "Volcano Status: " + stat
    elevInf = "Elevation: " + str(elev) + " meters"

    info = vname + "; " + tp + "; " + stat + "; " + elevInf

    #volcanoLayer.add_child(fl.Marker(location = [lat, lon], popup = info, icon = iconType))
    volcanoLayer.add_child(fl.CircleMarker(location = [lat, lon], popup = info, fill = True, fill_color = returnColor(elev), color = 'grey', fill_opacity = 0.7))

map.add_child(populationLayer)                                                       #adding the population distribution colors to the map layer
map.add_child(volcanoLayer)                                                          #adding the volcano points to the map layer
map.add_child(fl.LayerControl())

map.save("USA_Volcanoes.html")

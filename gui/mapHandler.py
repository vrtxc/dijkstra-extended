import pandas as pd
import xml.etree.ElementTree as ET
import plotly.express as px


def createMap(routeTable):
    tree = ET.parse(routeTable)
    root = tree.getroot()
    value = '#'
    data = []

    for node in root.iter('node'):
        for coordinates in node.iter('data'):
            if coordinates.get('key') == 'lat':
                lat = coordinates.text
                lat = float(lat)
            if coordinates.get('key') == 'lon':
                lon = coordinates.text
                lon = float(lon)
        data.append([node.get('id'), lat, lon, value])
            
    df = pd.DataFrame(data, columns=['id', 'lat', 'lon', 'value'])

    city_start = df.query("id == 'TRIER - VERTEILERKREIS (A 602)'")
    city_dest = df.query("id == 'HEILIGENHAFEN - MITTE (A 1)'")

    route = pd.concat([city_start, city_dest])

    # fig = px.line_mapbox(route, lat="lat", lon="lon", color="value", zoom=3, height=900)

    # fig.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})

        
        
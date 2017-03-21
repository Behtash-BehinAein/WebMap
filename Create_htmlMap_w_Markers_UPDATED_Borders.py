# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 11:49:08 2017

@author: bbehinae
"""

import folium,pandas
df = pandas.read_csv("Volcanoes-USA.txt")

# -----------------------------------------------------------------------------
# Creating a map inside python
map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Mapbox bright')
# -----------------------------------------------------------------------------
#
#
# -----------------------------------------------------------------------------
# Applying methods e.g. markers to the map
#map.simple_marker(location=[45.3288,-121.6625],popup='Mt. Hood Meadows',marker_color='red')

fg = folium.FeatureGroup(name="Volcano Locations")    

for lat,lon,name,elv in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    step  =   int((max(df['ELEV']) - min(df['ELEV']))/3)
    span1_s = int(min(df['ELEV']))
    span1_f = int(span1_s + step)
    span2_s = int(span1_f)
    span2_f = int(span2_s + step)
    if   elv in range(span1_s, span1_f):
        col =  'green'
    elif elv in range(span2_s, span2_f):
        col =  'orange'
    else:
        col =  'red'
    #map.add_child(folium.Marker(location=[lat,lon], popup=name, icon=folium.Icon(color=col)))
    fg.add_child(folium.Marker(location=[lat,lon], popup=name, icon=folium.Icon(color=col,icon_color='green')))

map.add_child(fg)
    
    
map.add_child(folium.GeoJson(data=open('World_population.json'),
                             name='World Population',
                             style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(folium.LayerControl())
# -----------------------------------------------------------------------------
#
#
# -----------------------------------------------------------------------------
# Creating an html map for web
map.save(outfile='test.html')



# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 11:49:08 2017

@author: bbehinae
"""

import folium,pandas
df = pandas.read_csv("Volcanoes-USA.txt")



# -----------------------------------------------------------------------------
# Creating a map inside python
map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles = 'Stamen Terrain')
# -----------------------------------------------------------------------------
#
#
# Color function   ------------------------------------------------------------
#def color(elv):
#    if elv in range(0,1000):
#        col =  'green'
#    elif elv in range(1000,3000):
#        col =  'orange'
#    else:
#        col =  'red'
#    return col
# -----------------------------------------------------------------------------
#
#
# -----------------------------------------------------------------------------
# Applying methods e.g. markers to the map
#map.simple_marker(location=[45.3288,-121.6625],popup='Mt. Hood Meadows',marker_color='red')
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
    map.add_child(folium.Marker(location=[lat,lon], popup=name, icon=folium.Icon(color=col,icon_color='green')))
# -----------------------------------------------------------------------------
#
#
# -----------------------------------------------------------------------------
# Creating an html map for web
map.save(outfile='test.html')



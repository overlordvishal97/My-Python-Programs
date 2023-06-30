import folium
import pandas
#this 'data' can read both text file (or) Csv file.

data = pandas.read_csv("Volcanoes.csv") 
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""    
    
map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Mymap")

#if you want to add multiple markers you have to use 'for' if you want to use only few statements rather than multiple statements.
for lt,ln,el,nm in zip(lat,lon,elev,name):
     iframe = folium.IFrame(html=html % (nm,nm, el), width=200, height=100)
     fg.add_child(folium.Marker(location=[lt, ln] ,popup=folium.Popup(iframe) , icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)
map.save("Map_Color_changing_Marker.html") 
#i don't know why but the each marker is displaying every name of the volcoeno. and i wanted to correct that but to know avail so i will try and post it in the comment section of the udemy course.
# as i only mixed it with the colour changing course and link in popup note so i dont think i saw any mistakes.
#it is working after we changed the name into nm.
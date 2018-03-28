#terry huang
#3/27/2018
#assigntment 41

import folium
#folium for mapmaking

output = 'nycMap.html'
#mapworld = folium.Map(location=[0,0],zoom_start=3)  #centered (0,0), zoomed out size 3
mapnyc = folium.Map(location=[40.75, -74.125], zoom_start=10)
folium.Marker(location=[40.768731,-73.964915], popup = 'Hunter College').add_to(mapnyc) #this is self-explanatory

mapnyc.save(output)

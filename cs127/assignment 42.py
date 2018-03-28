#terry huang
#3/27/2018
#assigntment 42
import folium
import pandas as pd

infile = input("Enter CSV file name: ")


filemap = pd.read_csv(infile)
#filemap = filemap.dropna()
print(filemap)



mapcenter = folium.Map(location=[40.768731, -73.964915])

for index,row in filemap.iterrows():  #iterrows is a generator which yields only the index and row in respective column
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapcenter)

output = input('Enter output file: ')

mapcenter.save(outfile=output)

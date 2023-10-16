import requests, json
import mysql.connector
import pandas as pd

db = mysql.connector.connect(user = 'root', password = '09122003', host = 'localhost', port = '3306', database = 'test 1')

try:
  file=open("T:\Python\AYD\output.csv","r")
  coordinate=file.readlines() 

except FileNotFoundError:
  print("File coordinate.txt not found!")

apikey= "AIzaSyDoTfYByHuGDc6y6j6-fwyafbOLEx4EGXM"
value = []    

for latlng in coordinate:
  serviceURL = "https://maps.googleapis.com/maps/api/elevation/json?locations="+latlng+"&key="+apikey
  
  r = requests.get(serviceURL)
  print(r.text)
  y = json.loads(r.text)
  for result in y["results"]:
    if result["elevation"] >= 0:
          value.append((result["location"]["lat"], result["location"]["lng"],(result["elevation"])))
    

query = "insert into `coordinate` (`lat`, `lon`, `elevation`) values (%s, %s, %s);"

cursor = db.cursor()
create = "CREATE TABLE IF NOT EXISTS coordinate (lat DECIMAL(9,6),lon DECIMAL(9,6), elevation DECIMAL(9,6));"   
cursor.execute(create)
cursor.executemany(query, value)
db.commit()
  


# import geopandas as gpd
# from shapely.geometry import Polygon

# lon_lat_list = [[4.373352367, 52.091372156], [4.373360755, 52.091365819], [4.373384852, 52.091347618], [4.373410766, 52.091360632], [4.37337828, 52.09138517], [4.373352367, 52.091372156]]

# polygon_geom = Polygon(lon_lat_list)
# polygon = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom])       

# polygon.to_file(filename='polygon.geojson', driver='GeoJSON')
# polygon.to_file(filename='polygon.gpkg', driver="GPKG")
# polygon.to_file(filename='polygon.shp', driver="ESRI Shapefile")

# import folium
# m = folium.Map([50.854457, 4.377184], zoom_start=5, tiles='cartodbpositron')
# folium.GeoJson(polygon).add_to(m)
# folium.LatLngPopup().add_to(m)
# m
# # if using Spyder.5
# import webbrowser
# m.save('test.html')
# webbrowser.open_new_tab('test.html')
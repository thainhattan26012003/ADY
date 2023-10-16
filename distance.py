import csv
import math

def get_distance_from_lat_lon_in_km(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the earth in km
    d_lat = deg2rad(lat2 - lat1)  # deg2rad below
    d_lon = deg2rad(lon2 - lon1)
    a = (
        math.sin(d_lat / 2) * math.sin(d_lat / 2) +
        math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) *
        math.sin(d_lon / 2) * math.sin(d_lon / 2)
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c  # Distance in km
    return d

def deg2rad(deg):
    return deg * (math.pi / 180)

with open('T:\Python\AYD\coordinate.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in data:
        slat, slon, elat, elon = row[0], row[1], row[2], row[3]
        distance = get_distance_from_lat_lon_in_km(float(slat), float(slon), float(elat), float(elon))
        print(distance)  






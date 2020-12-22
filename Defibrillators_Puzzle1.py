import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())

target = None
cd = None

for i in range(n):
    defib = input()
    
    #Splitting the data for each data in the input
    defibNum, defibName, defibAdd, defibNum, defibLon, defibLat = defib.split(";")
    
    #Format variables
    nlon = lon.replace(",",".")
    nlat = lat.replace(",",".")
    
    defibLon = defibLon.replace(",",".")
    defibLat = defibLat.replace(",",".")

    
    #Convert variables
    longitude = float(nlon)
    latitude = float(nlat)
    defibLon = float(defibLon)
    defibLat = float(defibLat)

    #Calculating X
    x = (defibLon - longitude) * math.cos((latitude+defibLat)/2)
    
    #Calculating Y
    y = defibLat - latitude
    
    #Calculating D
    d = math.sqrt(math.pow(x,2) + math.pow(y,2))*6371
    df = int(d)
    
    if cd == None:
        cd = df
        target = defibName
    elif df < cd:
        cd = df
        target = defibName


print(str(target))




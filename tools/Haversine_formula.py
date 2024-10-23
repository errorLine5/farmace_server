import math
from Models.Pharmacy import Pharmacy


def haversine_formula(lat1, lng1, lat2, lng2)->float:
    
    R = 6371  # Raggio della terra in km  

    lat1, lng1, lat2, lng2 = map(math.radians, [lat1, lng1, lat2, lng2]) #conversione da float a radianti, servira poi per la formula completa

    dlat=lat2-lat1   #delta tra le due latitudini, differenza

    dlng=lng2-lng1   #delta tra le due longitudini, differenza

    #formula dell'haversine

    a=math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlng/2)**2 

    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    distanza=R*c

    return distanza

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:59:32 2018

@author: Zigan Wang
"""

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)

coordinates = geolocator.reverse("52.509669, 13.376294")
print(coordinates.address)
print((coordinates.latitude, coordinates.longitude))
print(coordinates.raw)


from geopy.distance import vincenty
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(vincenty(newport_ri, cleveland_oh).miles)
print(vincenty(newport_ri, cleveland_oh).km)

from geopy.distance import great_circle
print(great_circle(newport_ri, cleveland_oh).miles)

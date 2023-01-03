# -*- coding: utf-8 -*-
"""
@author: Joachim ANDRE

"""

# Library

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


# Find country

num = ""

mon_num = phonenumbers.parse(num)
localisation = geocoder.description_for_number(mon_num, "fr")
print(localisation)

# find operator

operator = phonenumbers.parse(num)
print(carrier.name_for_number(operator, "fr"))

# find lat - long

key_API = "b2eff95b45b1401095b95082db8d7e76"
coord = OpenCageGeocode(key_API)
request = str(localisation)
response = coord.geocode(request)
lat = response[0]["geometry"]["lat"]
lng = response[0]["geometry"]["lng"]
print(lat, lng)
import requests
import json

def get_place_ids():
    r=requests.get('https://opendomesday.org/api/1.0/county/dby/')
    return(r.json()['places_in_county'])

ids= get_place_ids()
print(ids)


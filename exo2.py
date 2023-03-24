import requests
import json

def get_place_ids():
    """
    get all the places id in Derbyshire

    Returns
    -------
    None.

    """
    r=requests.get('https://opendomesday.org/api/1.0/county/dby/')
    r=r.json()['places_in_county']
    res=list()
    for i in range(len(r)):
        res.append(r[i]['id'])
    return(res)

if __name__ == '__main__':
	ids= get_place_ids()
	print(ids)


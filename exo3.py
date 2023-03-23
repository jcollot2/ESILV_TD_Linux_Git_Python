import requests
import json

def get_manor_ids(place_id):
    url = f"https://opendomesday.org/api/1.0/place/{place_id}/"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Impossible de récuperer les données")

    data = response.json()['manors']
    res=list()
    for i in range(len(data)):
        res.append(data[i]['id'])
    return res

if __name__ == '__main__':
    place_id = 1036
    manor_ids = get_manor_ids(place_id)
    print(f"Manor IDs for {place_id}: {manor_ids}")

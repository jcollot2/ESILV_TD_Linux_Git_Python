import requests
import json
import exo2
import exo3
import pandas as pd
import numpy as np

def get_all_manors():
    """
    List all manors_id in the Derbyshire

    Returns :
    --------
        manors : List of id
    """
    places=exo2.get_place_ids()
    manors=list()
    for i in range(len(places)):
        manors=manors + exo3.get_manor_ids(places[i])
    return manors

def manors_info(manors):
    """
    Create a panda dataframe with all manors id in the Derbyshire, their geld paid and their total ploughs owned

    Parameters
    ----------
    manors : list of id

    Returns
    -------
    df : Dataframe

    """
    geld_paid=list()
    total_ploughs=list()
    for i in range(len(manors)):
        value=manors[i]
        url = f"https://opendomesday.org/api/1.0/manor/{value}/"
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("Impossible de récuperer les données")
            return 404;
        geld_paid.append(response.json()['geld'])
        total_ploughs.append(response.json()['totalploughs'])
    df=pd.DataFrame({'id_manors': manors, 'geld': geld_paid, 'totalploughs': total_ploughs}).replace(np.nan,0.0)
    return df


if __name__ == '__main__':
    df=manors_info(get_all_manors())
    print(df)
    sum_geld_paid= df.geld.sum()
    print(f"\nLa somme total de geld payés est de {sum_geld_paid}")
    sum_ploughs=df.totalploughs.sum()
    sum1=np.sum(df['totalploughs'])
    print(f"\nLa proportion totale de ploughs possédé est de {sum_ploughs}")
    print(sum1)

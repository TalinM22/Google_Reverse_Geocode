import googlemaps
import pandas as pd
import time

## Add key here
gmaps = googlemaps.Client(key='abc123')

## Function to retrieve demographic info based on lat-long from JSON repsonse
def get_location(_lat,_lng):

    r_geocode_result = gmaps.reverse_geocode((_lat, _lng))
    address_components = r_geocode_result[0]['address_components']

    try:
        city = [i['long_name'] for i in address_components if 'sublocality_level_1' in i['types']]
        city = city[0] if city else None
    except:
        city = "NA"

    try:
        state = [i['long_name'] for i in address_components if 'administrative_area_level_1' in i['types']]
        state = state[0] if state else None
    except:
        state = "NA"

    try:
        county = [i['long_name'] for i in address_components if 'administrative_area_level_2' in i['types']]
        county = county[0] if county else None
    except:
        county = "NA"

    try:
        town = [i['long_name'] for i in address_components if all(elem in ['administrative_area_level_3', 'political'] for elem in i['types'])]
        town = town[0] if town else None
    except:
        town = "NA"

    try:
        village = [i['long_name'] for i in address_components if 'locality' in i['types']]
        village = village[0] if village else None
    except:
        village = "NA"

    try:
        postal_code = [i['long_name'] for i in address_components if 'postal_code' in i['types']]
        postal_code = postal_code[0] if postal_code else None
    except:
        postal_code = "NA"

    try:
        country = [i['long_name'] for i in address_components if all(elem in ['country', 'political'] for elem in i['types'])]
        country = country[0] if country else None
    except:
        country = "NA"

    df = pd.DataFrame()
    df = df.append({"S_ID" : city_code, "latitude" : _lat,"longitude" : _lng , "village": village , "town" : town , "city" : city, "state" : state, "county" : county,"country" : country, "Postal Code": postal_code },ignore_index = True)

    return df

## Dummy dataframe
df_loc = pd.DataFrame(
    {
        "City": ["City1", "City2", "City3", "City4", "City5"],
        "Latitude": [-34.58, -15.78, -33.45, 4.60, 10.48],
        "Longitude": [-58.66, -47.91, -70.66, -74.08, -66.86],
    }
)


## initializing an empty dataframe
data = pd.DataFrame()


## Iterating on df_loc
for row in df_loc.itertuples():
    (city_code, lat, lng  ) = (row.City,row.Latitude, row.Longitude)

    try:
        df = get_location(lat,lng)
        data = pd.concat([data, df])
    except:
        pass



print(data)


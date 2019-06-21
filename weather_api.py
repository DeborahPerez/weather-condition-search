import json
import requests
from openweathermap_token import APPID
import google_api
import geocoder

api_token = '&APPID=' + APPID
api_url_base = "http://api.openweathermap.org/data/2.5/weather?"
json_city_ids = 'city.list.json'

headers = {'Content-Type': 'application/json',
	   'Authorization': 'Bearer {0}'.format(api_token)}


# Test capturing data
def get_city_info(lat,lon):
    api_url = '{0}lat={1}&lon={2}{3}'.format(api_url_base, lat, lon, api_token)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


# Search for longitude and latitudes for a city and state 
def get_lon_lat(city, state):
    geo_input = '{0}, {1}'.format(city, state)
    g = geocoder.arcgis(geo_input)
    lat = round(float(g.latlng[0]), 2)
    lng = round(float(g.latlng[1]), 2)
    return [lat, lng]

# ------------------------------------------------------------------------

# Loop through cities
# get longitude and lattitude for each city
# query to openweathermaps using longitude and lattitude
# save object to results if object['weather']['main'] is condition
def get_cities_for_condition(condition):
    results = []
    cities = google_api.main()
    for city in cities:
        name = "{0}, {1}".format(city[0], city[1])
        result = None
        latlng_key = get_lon_lat(city[0], city[1])
        result = get_city_info(latlng_key[0], latlng_key[1])
        if result is not None:
            if result['weather'][0]['main'].lower() == condition.lower():
                weatherCondition = result['weather'][0]['main']
                temp_K = int(result['main']['temp'])
                temp_F = round(((temp_K - 273.15) * float(9/5) + 32), 2)
                windSpeed = result['wind']['speed']
                statement = '{0} is experiencing {1} with temperatures at {2} Fahrenheit and {3} mph wind speed'.format(name, weatherCondition, temp_F, windSpeed)
                results.append(statement)
        else:
            print ('[!] Request failed')

    return results

if __name__ == "__main__":
    condition = 'Rain'
    get_cities_for_condition(condition)

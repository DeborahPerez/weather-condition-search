import json
import requests
from openweathermap_token import APPID

api_token = '&APPID=' + APPID
api_url_base = "http://api.openweathermap.org/data/2.5/weather?"
json_city_ids = 'city.list.json'
lat = '40.71'
lon = '-74.01'
headers = {'Content-Type': 'application/json',
	   'Authorization': 'Bearer {0}'.format(api_token)}


# Unpack compressed json information with city ids
def read_json_file (jsonFile):
    with open(jsonFile, 'r', encoding="latin-1") as fin:
        data = json.load(fin)
#        print (data[0])
        return data


# Test capturing data
def test_city_info():
    api_url = '{0}lat={1}&lon={2}{3}'.format(api_url_base, lat, lon, api_token)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

# Query result
account_info = test_city_info()

if account_info is not None:
    print ("Here's your info: ", account_info)
    name = account_info['name']
    weatherCondition = account_info['weather'][0]['main']
    temp_K = int(account_info['main']['temp'])
    temp_F = round(((temp_K - 273.15) * float(9/5) + 32), 2)
    windSpeed = account_info['wind']['speed']
    print ('In the city of {0} the weather condition is {1} with temperatures at {2} Fahrenheight and a wind speed of {3} mph'.format(name, weatherCondition, temp_F, windSpeed))
else:
    print ('[!] Request failed')

# Read city json file
city_data = read_json_file(json_city_ids)
us_city_count = 0
for data in city_data:
    if data['country'] == "US":
        us_city_count += 1
print ("US city count is: ", us_city_count)

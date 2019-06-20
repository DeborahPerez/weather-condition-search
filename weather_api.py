import json
import requests
from openweathermap_token import APPID

api_token = '&APPID=' + APPID
api_url_base = "http://api.openweathermap.org/data/2.5/weather?id="


headers = {'Content-Type': 'application/json',
	   'Authorization': 'Bearer {0}'.format(api_token)}


def test_city_info():
    api_url = '{0}5128581{1}'.format(api_url_base, api_token)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

account_info = test_city_info()

if account_info is not None:
    print ("Here's your info: ")
    name = account_info['name']
    weatherCondition = account_info['weather'][0]['main']
    temp_K = int(account_info['main']['temp'])
    temp_F = round(((temp_K - 273.15) * float(9/5) + 32), 2)
    windSpeed = account_info['wind']['speed']
    #print (type(account_info))
    #for k, v in account_info['account'].items():
    #    print ('{0}:{1}'.format(k, v))
    print ('In the city of {0} the weather condition is {1} with temperatures at {2} Fahrenheight and a wind speed of {3} miles per hour'.format(name, weatherCondition, temp_F, windSpeed))
else:
    print ('[!] Request failed')

import requests
from dotenv import load_dotenv
import os
import json

url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/almaty?'

load_dotenv()

API = os.environ.get('API_KEY')
params = {
    'unitGroup': 'metric',
    'include': 'days, current',
    'key': API,
    'contentType': 'json'
}

response = requests.get(url, params=params)


data = response.json()

#print(json.dumps(data, indent = 2))

print(f'''City: {data['resolvedAddress']}
Datetime: {data['days'][0]['datetime']}
Temperature: {data['days'][0]['temp']}

Feels Like: {data['days'][0]['tempmax']}

Minimal Temperature: {data['days'][0]['tempmin']}
Maximal Temperature: {data['days'][0]['tempmax']}

Sunrise time: {data['days'][0]['sunrise']}
Sunset time: {data['days'][0]['sunset']}''')

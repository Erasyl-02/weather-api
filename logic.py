import requests
from dotenv import load_dotenv
import os

url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/almaty?'

load_dotenv()

API = os.environ.get('API_KEY')
params = {
    'unitGroup': 'metric',
    'key': API,
    'contentType': 'json'
}

response = requests.get(url, params=params)


response = response.json()
print(response['address'])
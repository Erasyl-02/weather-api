import requests
from dotenv import load_dotenv
import os
import json


load_dotenv()

def load_key():
    API = os.environ.get('API_KEY')
    if not API:
        raise ValueError('Api key doesnt exist in .env')
    return API
    
    

    
def get_data(city, API):
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?'
    params = {
        'unitGroup': 'metric',
        'include': 'days,current',
        'key': API,
        'contentType': 'json'
    }
    response = requests.get(url, params=params, timeout=5)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        raise ValueError('Please check your API key correctness in .env')
    return








# print(json.dumps(data, indent = 2))

def show_data(data):
    print(
f'''{data['resolvedAddress'].title()}
📅 Date: {data['days'][0]['datetime']}
🌡️ Now: {data['currentConditions']['temp']}°C (feels like {data['currentConditions']['feelslike']}°C)
🌡️ Today: {data['days'][0]['tempmin']}°C — {data['days'][0]['tempmax']}°C
☁️ {data['days'][0]['conditions'].title()}
📝 {data['days'][0]['description'].title()}
🌅 Sunrise: {data['days'][0]['sunrise']} | 🌇 Sunset: {data['days'][0]['sunset']}'''
)
    

def show_help():
    return

#data = get_data('almaty')
#show_data(data)
 

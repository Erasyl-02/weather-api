import os
import json

import requests



def load_key() -> str:
    API = os.environ.get('API_KEY')
    if not API:
        raise ValueError('Api key doesnt exist in .env')
    return API
    
    

    
def get_data(city:str, API:str) -> dict:
    try:
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?'
        params = {
            'unitGroup': 'metric',
            'include': 'days,current',
            'key': API,
            'contentType': 'json'
        }
        response = requests.get(url, params=params, timeout=5)
    except requests.exceptions.ConnectionError:
        raise ConnectionError('Please check your internet connection')
    except requests.exceptions.RequestException:
        raise ConnectionError('Issues with connection, try again later')
    
    if response.status_code == 200:
        try:
            return response.json()
        except json.JSONDecodeError:
            raise ValueError('There is problems with data, try again')
        except ValueError:
            raise ValueError('Unexpected error, try again')
    elif response.status_code == 400:
        raise ValueError('Please check correctness of the city name and try again')
    elif response.status_code == 401:
        raise ValueError('Please check your API key correctness in .env')
    elif response.status_code == 404:
        raise RuntimeError('Technical issue, try again later')
    elif response.status_code == 429:
        raise RuntimeError('Too many requests, try again later')
    elif response.status_code == 500:
        raise RuntimeError('Weather service is temporarily unavailable, try again later')
    else:
        raise RuntimeError('Unexpected error, weather service is temporarily unavailable, try again later')






def show_data(data:dict) -> str:
    return f'''{data['resolvedAddress'].title()}
📅 Date: {data['days'][0]['datetime']}
🌡️ Now: {data['currentConditions']['temp']}°C (feels like {data['currentConditions']['feelslike']}°C)
🌡️ Today: {data['days'][0]['tempmin']}°C — {data['days'][0]['tempmax']}°C
☁️ {data['days'][0]['conditions'].title()}
📝 {data['days'][0]['description'].title()}
🌅 Sunrise: {data['days'][0]['sunrise']} | 🌇 Sunset: {data['days'][0]['sunset']}

Enter a new city or q to quit below'''
    

def show_help() -> str:
    print(
'''Available commands:
  q        - exit the program
  /help    - show this help
  <city>   - get current day's weather for the specified city (e.g. "Almaty", "London")'''
)
 

# from dotenv import load_dotenv
# load_dotenv()


import os
import json

import requests

import exceptions



def load_key() -> str:
    API = os.environ.get('API_KEY')
    if not API:
        raise ValueError('Api key doesnt exist in .env')
    return API
    
    

    
def get_data(city:str, API:str):
    try:
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?'
        params = {
            'unitGroup': 'metric',
            'include': 'days,current',
            'key': API,
            'contentType': 'json'
        }
        response = requests.get(url, params=params, timeout=5)
        return response
    except requests.exceptions.ConnectionError:
        raise ConnectionError('Please check your internet connection')
    except requests.exceptions.RequestException:
        raise ConnectionError('Issues with connection, try again later')
    

def validate_data(data):
    if data.status_code == 200:
        try:
            return data.json()
        except json.JSONDecodeError:
            raise ValueError('There is problems with data, try again')
        except ValueError:
            raise ValueError('Unexpected error, try again')
    elif data.status_code == 400:
        raise exceptions.BadRequestError('Please check correctness of the city name and try again')
    elif data.status_code == 401:
        raise exceptions.AuthenticationError('Please check your API key correctness in .env')
    elif data.status_code == 404:
        raise exceptions.EndpointError('Technical issue, try again later')
    elif data.status_code == 429:
        raise exceptions.TooManyRequestsError('Too many requests, try again later')
    elif data.status_code == 500:
        raise exceptions.ExternalServerError('Weather service is temporarily unavailable, try again later')
    else:
        raise exceptions.ApiException('Unexpected error, weather service is temporarily unavailable, try again later')
    

def filter_data(data:dict) -> dict:
    return{'city': data.get('resolvedAddress'),
           'today': data.get('days', [{}])[0].get('datetime', 'Unknown'),
           'current_temp': str(data.get('currentConditions', {}).get('temp', 'Unknown')),
           'feels_like': str(data.get('currentConditions', {}).get('feelslike', 'Unknown')),
           'today_temp_min': str(data.get('days', [{}])[0].get('tempmin', 'Unknown')),
           'today_temp_max': str(data.get('days', [{}])[0].get('tempmax', 'Unknown')),
           'condition': data.get('days', [{}])[0].get('conditions', 'Unknown'),
           'description': data.get('days', [{}])[0].get('description', 'Unknown'),
           'sunrise_time': data.get('days', [{}])[0].get('sunrise', 'Unknown'),
           'sunset_time': data.get('days', [{}])[0].get('sunset', 'Unknown')}






def show_data(data:dict) -> str:
    return f'''{data['city'].title()}
📅 Date: {data['today']}
🌡️ Now: {data['current_temp']}°C (feels like {data['feels_like']}°C)
🌡️ Today: {data['today_temp_min']}°C — {data['today_temp_max']}°C
☁️ {data['condition'].title()}
📝 {data['description'].title()}
🌅 Sunrise: {data['sunrise_time']} | 🌇 Sunset: {data['sunset_time']}

Enter a new city or q to quit below'''
    

def show_help():
    print(
'''Available commands:
  q        - exit the program
  /help    - show this help
  <city>   - get current day's weather for the specified city (e.g. "Almaty", "London")'''
)
 
# API = load_key()
# data = get_data('almaty', API)
# filtered = filtered_data(data)

# # print(json.dumps(filtered, indent=4))
# print(show_data(filtered))


from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
load_dotenv()

import logic
import cache

app = FastAPI()

@app.get('/')
def welcome() -> dict[str,str]:
    return {'message': 'Welcome to the Weather App'}

@app.get('/weather')
def get_weather(city: str='almaty') -> dict[str,str]:
    try:
        key = logic.load_key()
        cached_data = cache.get_from_cache(city.lower())
        if cached_data:
            return cached_data
        else:
            response = logic.get_data(city, key)
            data = logic.validate_data(response)
            filtered = logic.filter_data(data)
            cache.save_to_cache(city.lower(), filtered)
            return filtered
    except (ValueError, ConnectionError, RuntimeError) as e:
        raise HTTPException(status_code=404, detail=str(e))
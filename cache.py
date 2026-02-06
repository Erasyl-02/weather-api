import json
import os

import redis

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')

r = redis.Redis(host=REDIS_HOST, port=int(REDIS_PORT), decode_responses=True)

def save_to_cache(city, data):
    data = json.dumps(data)
    r.set(city, data, ex=3600)

def get_from_cache(city):
    response = r.get(city)
    if response:
        return json.loads(response)
    return None
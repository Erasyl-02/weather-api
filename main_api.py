from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

import logic
import cache

app = FastAPI()

@app.get('/')
def welcome() -> str:
    return 'Welcome to the Weather App'
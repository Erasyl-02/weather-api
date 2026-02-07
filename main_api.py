from fastapi import FastAPI

import logic
import cache

app = FastAPI()

@app.get('/weather')
def get_weather():
    pass
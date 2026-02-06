from dotenv import load_dotenv
load_dotenv()

import logic
import cache




def main(city):
    try:
        while True:
            if city == 'q':
                return
            elif city == '/help':
                logic.show_help()
                city = input('> ').strip()
                continue
            try:
                key = logic.load_key()
                cached_data = cache.get_from_cache(city.lower())
                if cached_data:
                    print(cached_data)
                else:
                    data = logic.get_data(city, key)
                    print(logic.show_data(data))
                    cache.save_to_cache(city.lower(), logic.show_data(data))
            except (ValueError, ConnectionError, RuntimeError) as e:
                print(e)
                return
            city = input('> ').strip()
    except Exception:
         print('Unexpected Error, try againn')
         return
    


if __name__ == '__main__':
    print(
"""Welcome to the Weather App
Please type your city below (or /help for more)"""
    )
    city = input('> ').strip()
    while not city:
            print('Please type name of a city')
            city = input('> ').strip()
    main(city)
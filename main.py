from dotenv import load_dotenv
load_dotenv()

import logic
import cache
import exceptions




def main(city:str) -> None:
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
                    print(logic.show_data(cached_data))
                else:
                    response = logic.get_data(city, key)
                    data = logic.validate_data(response)
                    filtered = logic.filter_data(data)
                    print(logic.show_data(filtered))
                    cache.save_to_cache(city.lower(), filtered)
            except (ValueError, ConnectionError, exceptions.ApiException) as e:
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
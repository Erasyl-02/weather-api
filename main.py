import logic


def main(city):
    try:
        if city == 'q':
            return
        if city == '/help':
            logic.show_help()
            return
        try:
            key = logic.load_key()
            data = logic.get_data(city, key)
        except (ValueError, ConnectionError, RuntimeError) as e:
            print(e)
            return
        logic.show_data(data)
    except Exception:
         print('Unexpected Error, try again')
         return
    


if __name__ == '__main__':
    print(
"""Welcome to the Weather App
Please type your city below (or /help for more)"""
    )
    city = input('> ').strip()
    while not city:
            print('Please type name of a city')
            city = input('>').strip()
    main(city)
import logic


def main(city):
    if city == 'q':
         return
    if city == '/help':
        logic.show_help()
        return
    data = logic.get_data(city)
    logic.show_data(data)
    


if __name__ == '__main__':
    print(
"""Welcome to the Weather App
Please type your city below (or type /help for more)"""
    )
    city = input('> ').strip()
    while not city:
            print('Please type name of a city')
            city = input('>').strip()
    main(city)
import logic


def main(city):
    data = logic.get_data(city)
    logic.show_data(data)
    


if __name__ == '__main__':
    print("""Welcome to Weather APP
    Please type your city below to the weather""")
    city = input()
    main(city)
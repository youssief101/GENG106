def city_country(city_name, country):
    """Returns a city name followed by the country"""
    city_description = f'"{city_name.title()}, {country.title()}"'    
    return city_description

while True:
    """get the city name and the country"""
    print('enter q to quit at anytime')
    city = input('city name: ')
    if city == 'q':
        break
    country = input('country name: ')
    if country == 'q':
        break
    name = city_country(city, country)
    print(name)

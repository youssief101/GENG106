def describe_city(city_name, country='Egypt'):
    """Prints the name of the city and it's country"""
    print(f"{city_name} is in {country}.")

describe_city('Cairo')
describe_city('Paris', 'France')
describe_city('Roma', 'Italy')
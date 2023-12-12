def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
describe_pet('willie', 'dog') # positional argument
describe_pet(animal_type='hamster', pet_name='harry') # keyword argument
describe_pet('kattie')

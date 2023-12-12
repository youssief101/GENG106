def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print(f"\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    # get the user first name
    f_name = input("first name: ")
    if f_name == 'q':
        break   # this code breaks the loop, and stop the execution

    # get the user last name
    l_name = input("last name: ")
    if f_name == 'q':
        break   # this code breaks the loop, and stop the execution
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")
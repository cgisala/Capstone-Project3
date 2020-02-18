"""Groups all the prompts for neater apearance
"""

# Prompts the user to enter the name and email of the artist
def artist_info():
    name = input('\nEnter artist name: ')
    email = input ('Enter artist email: ')

    return name, email

# Prompts the user to enter info for the artwork such as the artist name, name of the artwork and price
def artwork_info():
    name = input('\nEnter artist name: ').lower()
    artwork = input('Enter artwork name: ').lower()
    price = input('Enter artwork price: ')

    return name, artwork, price

def artist_name():
    name = input('\nEnter artist name: ')

    return name

def artist_email():
    email = input('\nEnter artist email: ')

    return email
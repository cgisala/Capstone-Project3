"""Groups all the repeating prompts and prints for neater apearance
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

# Prompts the user to enter artist name
def artist_name():
    name = input('\nEnter artist name: ')

    return name

# Prompts the user to enter artist email
def artist_email():
    email = input('\nEnter artist email: ')

    return email

# Prompts the user to enter artwork name
def artwork_name():
    artwork = input('\nEnter the artworks\'s name: ')

    return artwork

# Prints information for artworks that are available 
def for_sale_artwork(r):
    print(f"\nArtist: {r['artist']}\nArtwork: {r['name']}\nPrice: ${r['price']}\nStatus: for sale")

# Prints information for artworks that are sold
def sold_artwork(r):
    print(f"\nArtist: {r['artist']}\nArtwork: {r['name']}\nPrice: ${r['price']}\nStatus: sold")

# Prompts the user to enter the status of an artwork
def artwork_availability():
    print('\nOptions: sold or for sale')
    status = input('Enter the availability of the artwork: ')

    return status
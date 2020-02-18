from artist import Artist
from artwork import Artwork
import get
import sqlite3
import os

db = os.path.join('database', 'art_catalog.db')

def main():
    while True:
        menu()
        choice = input('choice: ')
        if choice == '1':
            name, email = get.artist_info() # Prompt user to enter the artist info
            add_artist(name, email) 
        elif choice == '2':
            name = get.artist_name()  # Prompts for the artist name
            search_artwork(db, name)
        elif choice == '3':
            name = get.artist_name()
            display_artwork(db, name)
        elif choice == '4':
            name, artwork, price = get.artwork_info()  # Prompt user to enter info
            add_artwork(db, name, artwork, price)
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice == '7':
            break
        else:
            print('\nChoice is not in the menu')

def menu():
    print('\nMenu: \n'
    '1: add new artist\n'
    '2: search for all artwork by artist\n'
    '3: display available work by artist\n'
    '4: add new artwork\n'
    '5: delete an artwork\n'
    '6: change availability status of an artwork\n'
    '7: Quit\n')

def add_artist(name, email):
    new_artist = Artist(name.lower(), email.lower())
    new_artist.add_artist()
    
def add_artwork(db, name, artwork, price):
    """
    Checks first to see if the artist is in the database if not prompts the user to enter the artist info
    prior to entering the artwork info.
    """
    try:
        get_artist_sql = 'SELECT name, * FROM artist WHERE name = ?'

        con = sqlite3.connect(db) # Opens a connection with the databse
        con.row_factory = sqlite3.Row # This row_factory allows access to the data row name
        rows = con.execute(get_artist_sql, (name,) )
        artist = rows.fetchone()
        con.close()
        """ 
        Checks to see if the artist is in the database prior to entering the artwork info.
        If the artist is not in the database the artist is added first to the artist table first before the artwork is added to the database.
        """
        if artist == None:
            print('\nThe artist is not in the database.\n')
            email = get.artist_email() 
            add_artist(name, email) # Calls the add artist function
            new_artwork(name,artwork, price)
        else:
            new_artwork(name,artwork, price)
    except sqlite3.Error as e:
        print('Name not found')
    finally:
        con.close()

# Creates artwork object and adds the info on the artwork table
def new_artwork(name, artwork, price):
    new_artwork = Artwork(name, artwork, price)
    new_artwork.add_artwork()

def search_artwork(db, artist):
    get_artwork_by_name_sql = 'SELECT name, * FROM artwork WHERE artist = ?'

    con = sqlite3.connect(db) # Creates or opens connections to db file
    con.row_factory = sqlite3.Row # This row_factory allows access to data by row name
    rows = con.execute(get_artwork_by_name_sql, (artist, ) )

    # Prints the search result
    for r in rows:
        if r['availability'] == '1':
            print(f"\nArtist: {r['artist']}\nArtwork: {r['name']}\nPrice: ${r['price']}\nStatus: for sale")
        if r['availability'] == '0':
            print(f"\nArtist: {r['artist']}\nArtwork: {r['name']}\nPrice: ${r['price']}\nStatus: sold")
        
def display_artwork(db, artist):
    get_artwork_by_name_sql = 'SELECT name, * FROM artwork WHERE artist = ?'

    con = sqlite3.connect(db) # Creates or opens connections to db file
    con.row_factory = sqlite3.Row # This row_factory allows access to data by row name
    rows = con.execute(get_artwork_by_name_sql, (artist, ) )

    # Prints the search result
    for r in rows:
        if r['availability'] == '1':
            print(f"\nArtist: {r['artist']}\nArtwork: {r['name']}\nPrice: ${r['price']}\nStatus: for sale")
        

def delete_artwork():
    pass

def change_availability():
    pass

if __name__=='__main__':
    main()
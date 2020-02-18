from artist import Artist
from artwork import Artwork
import sqlite3
import os

db = os.path.join('database', 'art_catalog.db')

def main():
    while True:
        menu()
        choice = input('choice: ')
        if choice == '1':
            # Prompt user to enter the artist info
            name = input('Enter artist name: ')
            email = input ('Enter artist email: ')

            add_artist(name, email)
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            # Prompt user to enter info
            name = input('Enter artist name: ').lower()
            artwork = input('Enter artwork name: ').lower()
            price = input('Enter artwork price: ')
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
        if artist == None:
            print('\nThe artist is not in the database.\n')
            email = input("Enter artist email: ")
            con.close()
            add_artist(name, email) # Calls the add artist function
            new_artwork = Artwork(name, artwork, price)
            new_artwork.add_artwork()
        else:
            new_artwork = Artwork(name, artwork, price)
            new_artwork.add_artwork()
    except sqlite3.Error as e:
        print('Name not found')
        print(e)
    finally:
        con.close()

def search_artwork():
    pass

def display_artwork():
    pass

def delete_artwork():
    pass

def change_availability():
    pass

if __name__=='__main__':
    main()
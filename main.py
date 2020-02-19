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
        if choice == '1': # Add new artist
            name, email = get.artist_info() 
            add_artist(name, email) 
        elif choice == '2': # Search for all artwork by artist
            name = get.artist_name()  
            search_artwork(db, name)
        elif choice == '3': # Display available artwork for artist
            name = get.artist_name()
            display_artwork(db, name)
        elif choice == '4': # Add new artwork
            name, artwork, price = get.artwork_info()  
            add_artwork(db, name, artwork, price)
        elif choice == '5': # Delete artwork
            artwork = get.artwork_name()
            delete_artwork(db, artwork)
        elif choice == '6': # Change availability of artwork
            artwork = get.artwork_name() 
            status = get.artwork_availability()
            change_availability(db, artwork, status)
        elif choice == '7': # Exit program
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

# Adds the artist info to the artist table
def add_artist(name, email):
    new_artist = Artist(name, email)
    new_artist.add_artist()

# Adds the artwork to the database
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

        # Checks if the artist is in the database
        if artist == None:
            print('\n**The artist is not in the database**\n')
            email = get.artist_email() 
            add_artist(name, email) # Calls the add artist function
            new_artwork(name,artwork, price)
        else:
            new_artwork(name,artwork, price)
    except sqlite3.Error as e:
        print('Name not found')
        print(e)
    finally:
        con.close()

# Creates artwork object and adds the info on the artwork table
def new_artwork(name, artwork, price):
    new_artwork = Artwork(name, artwork, price)
    new_artwork.add_artwork()

# Searches for all the artwork of an artist regardless if it is sold or not
def search_artwork(db, artist):
    get_artwork_by_name_sql = 'SELECT name, * FROM artwork WHERE artist = ?'

    con = sqlite3.connect(db) # Creates or opens connections to db file
    con.row_factory = sqlite3.Row # This row_factory allows access to data by row name
    rows = con.execute(get_artwork_by_name_sql, (artist, ) )

    # Prints the search result
    for r in rows:
        if r['availability'] == 'for sale':
            get.for_sale_artwork(r)
        if r['availability'] == 'sold':
            get.sold_artwork(r)

    con.close()

# Displays the available artwork for a specified artist
def display_artwork(db, artist):
    get_artwork_by_name_sql = 'SELECT name, * FROM artwork WHERE artist = ?'

    con = sqlite3.connect(db) # Creates or opens connections to db file
    con.row_factory = sqlite3.Row # This row_factory allows access to data by row name
    rows = con.execute(get_artwork_by_name_sql, (artist, ) )

    # Prints the search result
    for r in rows:
        if r['availability'] == 'for sale':
            get.for_sale_artwork(r)

    con.close()

# Deletes a record from the database
def delete_artwork(db, name):

    con = sqlite3.connect(db)
    curs = con.cursor()
    curs.execute("DELETE FROM artwork WHERE name = (?)", (name,) )
    con.commit() # Save changes to database
    con.close() # Close connection

# Modifies the artwork availablity 
def change_availability(db, artwork, availability):
    try:
        con = sqlite3.connect(db)

        # Updates the artwork availability
        con.execute('''UPDATE artwork SET availability = ? WHERE name = ?''', (availability, artwork))
        con.commit() # Saves changes to the database
        con.close() # Close connection
    except:
        print('\nError: Something broke')

if __name__=='__main__':
    main()
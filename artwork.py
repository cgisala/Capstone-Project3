import sqlite3
import os

db = os.path.join('database', 'art_catalog.db')

class Artwork:
    """
    Represent one artwork in the program
    """

    def __init__(self, artist, artwork, price, availability=True):
        self.artist = artist
        self.artwork = artwork
        self.price = price
        self.availability = availability

    def add_artwork(self):
        conn = sqlite3.connect(db)

        #Adds artist to the artist table
        conn.execute('INSERT INTO artwork (artist, name, price, availability) VALUES (?, ?, ?, ?)',(self.artist, self.artwork, self.price, self.availability) ) 
        conn.commit()
        conn.close()

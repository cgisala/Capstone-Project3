import sqlite3
import os

db = os.path.join('database', 'art_catalog.db')

class Artist:

    """
    Represents one artist in the program.
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def add_artist(self):
        conn = sqlite3.connect(db)

        #Adds artist to the artist table
        conn.execute('INSERT INTO artist (name, email) VALUES (?, ?)',(self.name, self.email) ) 
        conn.commit()
        conn.close()

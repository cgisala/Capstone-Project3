import main
import unittest
import os

input_db = os.path.join('database', 'art_catalog.db')

class TestMain(unittest.TestCase):

    def test_artist_info(self):

        input_name = 'ROBIN HOOD'
        name = 'robin hood'
        input_email = 'ROBIN HOOD'
        email = 'robin.hood@email.com'

        self.assertEqual(name, email, main.add_artist(input_name, input_email))


    def test_add_artwork(self):

        input_name = 'ROBIN HOOD'
        name = 'robin hood'
        input_artwork = 'MONA LISA'
        artwork = 'mona lisa'
        input_price = '123'
        price = 123
        db = os.path.join('database', 'art_catalog.db')

        self.assertEqual(db, name, artwork, price, main.add_artwork(input_db, input_name, input_artwork, input_price) )

    def test_new_artwork(self):
        input_name = 'ROBIN HOOD'
        name = 'robin hood'
        input_artwork = 'MONA LISA'
        artwork = 'mona lisa'
        input_price = '123'
        price = 123

        self.assertEqual(name, artwork, price, main.new_artwork(input_name, input_artwork, input_price))

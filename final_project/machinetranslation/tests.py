""" This file holds the unit tests to test the functions in translator.py """
import unittest
from translator import french_to_english, english_to_french

class UnitTests(unittest.TestCase):

    def test_null_french_to_english(self):
        result = french_to_english('')
        assert result == ''

    def test_null_english_to_french(self):
        result = english_to_french('')
        assert result == ''

    def test_hello_english_to_french(self):
        result = english_to_french('Hello')
        assert result == 'Bonjour'

    def test_bonjour_french_to_english(self):
        result = french_to_english('Bonjour')
        assert result == 'Hello'

if __name__ == "__main__":
    unittest.main()
""" This file holds the unit tests to test the functions in translator.py """
import unittest

from machinetranslation.translator import french_to_english, english_to_french

class UnitTests(unittest.TestCase):

    def test_assertequal_french_to_english(self):
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello', "Not equal")

    def test_assertnotequal_french_to_english(self):
        result = french_to_english('Bonjour')
        self.assertNotEqual('Bonjour', result, "Equal")

    def test_assertequal_english_to_french(self):
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour', "Not Equal")

    def test_assertnotequal_english_to_french(self):
        result = english_to_french('Hello')
        self.assertNotEqual('Hello', result, "Equal")

if __name__ == "__main__":
    unittest.main()
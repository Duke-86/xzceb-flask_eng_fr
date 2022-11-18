import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french_1(self):
        self.assertNotEqual(english_to_french(0), 0)

    def test_english_to_french_2(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english_1(self):
        self.assertNotEqual(french_to_english(0), 0)

    def test_french_to_english_2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()

import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), "Hello",
                          'Error translating given text to English!')
        self.assertNotEqual(french_to_english(''),'','Error input field is null')

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), "Bonjour",
                          'Error translating given text to English!')
        self.assertNotEqual(english_to_french(''),'','Error input field is null')

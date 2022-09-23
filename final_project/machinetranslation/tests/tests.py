import unittest

from translator import englishToFrench, frenchToEnglish

class TranslatorTest(unittest.TestCase):
    def test_english_french(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
    def test_french_english(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    
if __name__ == '__main__':
    unittest.main()

    
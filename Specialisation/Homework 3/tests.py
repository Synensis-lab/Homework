from homework_week3 import generate_phrase
import unittest


class TestsToTest(unittest.TestCase):

    def testSameInBoth(self):
        self.assertTrue(generate_phrase("Testingthisworks123 !£$%^", "Testingthisworks123 !£$%^"))

    def testCharactersLessThanPhrase(self):
        self.assertFalse(generate_phrase("cbacba", "aabbccc"))

    def testCharactersAllUpper(self):
        self.assertFalse(generate_phrase("HELLO", "hello"))

    def testPhraseAllUpper(self):
        self.assertFalse(generate_phrase("hello", "HELLO"))

    def testPhraseSpaces(self):
        self.assertFalse(generate_phrase("HELLO", "HELLO   "))

    def testWhiteSpace(self):
        self.assertTrue(generate_phrase("HELLO   ", "HELLO   "))

    def testEmptyStrings(self):
        self.assertTrue(generate_phrase("", ""))

    def testEmptyCharacter(self):
        self.assertFalse(generate_phrase("", "GreenTrees"))

    def testEmptyPhrase(self):
        self.assertTrue(generate_phrase("GreenTrees", ""))








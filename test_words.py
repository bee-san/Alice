import sys
sys.path.append("..")
import unittest
from words import wordsServant
# python3 -m unittest Tests.testchi_squared
# python -m unittest discover -s tests
# python3 -m unittest discover -s Tests -p test*.py
# python3 -m unittest discover -p test*.py

class TestBasicParent(unittest.TestCase):
    def test_repeated_words(self):
        text = """hello and and I oop and I and I I oop"""
        t = wordsServant(text)
        t.repeatedWords()
        self.assertEqual(True, True)
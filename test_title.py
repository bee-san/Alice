import sys
sys.path.append("..")
import unittest
from title import titleServant
# python3 -m unittest Tests.testchi_squared
# python -m unittest discover -s tests
# python3 -m unittest discover -s Tests -p test*.py
# python3 -m unittest discover -p test*.py

class TestBasicParent(unittest.TestCase):
    def test_capitalisation_1(self):
        text = """# hello this is a h1 title\n## hello this is a h2 title"""
        t = titleServant(text, mdorhtml = "md", capitaliseTitles = False)
        t.getTitles()
        t.titleBreakdown()
        self.assertEqual(True, True)
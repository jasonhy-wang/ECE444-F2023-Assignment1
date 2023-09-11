import unittest
from utils import Utils

class TestUtils(unittest.TestCase):
    def test_reversed(self):
        util = Utils()
        self.assertEqual(util.reversed(12345), 54321)
        self.assertRaises(TypeError, util.reversed, "abc")
        self.assertRaises(TypeError, util.reversed, 1.23)
        
    def test_formatter(self):
        util = Utils()
        self.assertEqual(util.formatter(12345), ("11000000111001", "30071"))
        self.assertRaises(TypeError, util.formatter, "invalid")
        self.assertRaises(TypeError, util.formatter, 1.23)

if __name__ == "__main__":
    unittest.main()

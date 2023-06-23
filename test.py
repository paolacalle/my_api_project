import unittest
from disney_characters_api.py import get_formt


class test_disney_api(unittest.TestCase):
    def test_get_formt(self):
        self.assertEqual(get_formt("My Name is Paola"), "My%20Name%20is%20Paola")


if __name__ == '__main__':
    unittest.main()
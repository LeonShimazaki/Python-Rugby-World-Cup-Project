import unittest
from controller import setup

class TestRWC(unittest.TestCase):

    def setUp(self):
        self.rwc = setup()

    def test_a_has_year(self):
        self.assertTrue(hasattr(self.rwc, 'year'))
        self.assertTrue(type(self.rwc.year) == int)

    def test_b_rwc_sets_year(self):
        self.assertTrue(self.rwc.year, 2019)

if __name__ == '__main__':
    unittest.main(verbosity=3)

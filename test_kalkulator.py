import unittest
from kalkulator import dodaj, odejmij, mnoz, dziel

class TestKalkulator(unittest.TestCase):
    def test_dodaj(self):
        self.assertEqual(dodaj(2, 3), 5)

    def test_odejmij(self):
        self.assertEqual(odejmij(5, 3), 2)

    def test_mnoz(self):
        self.assertEqual(mnoz(4, 3), 12)

    def test_dziel(self):
        self.assertEqual(dziel(10, 2), 5)
    
    def test_dziel_przez_zero(self):
        with self.assertRaises(ValueError):
            dziel(5, 0)

if __name__ == '__main__':
    unittest.main()

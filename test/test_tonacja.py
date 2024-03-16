import unittest

import tonacja


# Testy działają

class MyTestCase(unittest.TestCase):
    def test_podaj_nazwe_tonacji(self):
        testowa_tonacja_1 = tonacja.Tonacja('C')
        self.assertEqual(testowa_tonacja_1.podaj_nazwe(), "C")

    def test_czy_dur_1(self):
        testowa_tonacja_1 = tonacja.Tonacja('C')
        self.assertEqual(testowa_tonacja_1.czy_dur(), True)

    def test_czy_dur_2(self):
        testowa_tonacja_2 = tonacja.Tonacja('a')
        self.assertEqual(testowa_tonacja_2.czy_dur(), False)

    def test_podaj_liste_nazw_dzwiekow(self):
        testowa_tonacja_3 = tonacja.Tonacja('C')
        self.assertEqual(testowa_tonacja_3.podaj_liste_nazw_dzwiekow(), ['c', 'd', 'e', 'f', 'g', 'a', 'h'])


if __name__ == '__main__':
    unittest.main()

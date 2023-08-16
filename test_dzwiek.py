import unittest
import dzwiek

class MyTestCase(unittest.TestCase):
    def test_konstruktora_1(self):
        d = dzwiek.Dzwiek(1, 'c')

    def test_konstruktora_2(self):
        with self.assertRaises(ValueError):
            d = dzwiek.Dzwiek(2, 'cbbb')

    def test_podaj_oktawe1(self):
        d = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d.podaj_oktawe(), 1)

    def test_podaj_nazwe_dzwieku1(self):
        d = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d.podaj_nazwe_dzwieku(), 'd')

    def test_podaj_swoj_stopien_1(self):
        d = dzwiek.Dzwiek(1, 'c')
        self.assertEqual(d.podaj_swoj_stopien('C'), 0)

    def test_podaj_swoj_stopien_2(self):
        d = dzwiek.Dzwiek(1, 'c#')
        self.assertFalse(d.podaj_swoj_stopien('C') == 0)

    def test_podaj_swoj_stopien_3(self):
        d = dzwiek.Dzwiek(1, 'c#')
        self.assertEqual(d.podaj_swoj_stopien('C'), -1)

    def test_podaj_swoj_kod_1(self):
        d = dzwiek.Dzwiek(1, 'c#')
        self.assertEqual(d.podaj_swoj_kod('C'), -1)

    def test_podaj_swoj_kod_2(self):
        d = dzwiek.Dzwiek(1, 'fb')
        self.assertEqual(d.podaj_swoj_kod('C'), -1)

    def test_podaj_swoj_kod_3(self):
        d = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d.podaj_swoj_kod('C'), 8)

    def test_czy_to_ma_sens_1(self):
        d = dzwiek.Dzwiek(2, 'd')
        self.assertEqual(d.podaj_oktawe(), d.podaj_swoj_kod('C')//7)

    def test_czy_to_ma_sens_2(self):
        d = dzwiek.Dzwiek(2, 'd')
        self.assertEqual(d.podaj_swoj_stopien('C'), d.podaj_swoj_kod('C') % 7)

    def test_czy_to_ma_sens_3(self):
        d = dzwiek.Dzwiek(2, 'db')
        self.assertEqual(d.podaj_swoj_stopien('C'), d.podaj_swoj_kod('C'))

if __name__ == '__main__':
    unittest.main()

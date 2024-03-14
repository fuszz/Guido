import unittest
import dzwiek
import tonacja
from enumerations import enum_bledy, enum_nazwy_dzwiekow


# Testy są ok - 14.03.2024

class MyTestCase(unittest.TestCase):
    def test_konstruktora_1(self):
        try:
            dzwiek.Dzwiek(1, "c")
        except:
            self.fail("Konstruktor nie działa.")

    def test_konstruktora_2(self):
        with self.assertRaises(enum_bledy.BladTworzeniaDzwieku):
            d = dzwiek.Dzwiek(2, 'cbbb')

    def test_podaj_oktawe1(self):
        d = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d.podaj_oktawe(), 1)

    def test_podaj_nazwe_dzwieku1(self):
        d = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d.podaj_nazwe_dzwieku().value, enum_nazwy_dzwiekow.NazwyDzwiekow("d").value)

    def test_podaj_swoj_stopien_1(self):
        d = dzwiek.Dzwiek(1, 'c')
        self.assertEqual(d.podaj_swoj_stopien(tonacja.Tonacja('C')), 0)

    def test_podaj_swoj_stopien_2(self):
        d = dzwiek.Dzwiek(1, 'c#')
        self.assertRaises(enum_bledy.BladDzwiekPozaTonacja, lambda: d.podaj_swoj_stopien(tonacja.Tonacja('C')))

    def test_podaj_swoj_kod_1(self):
        d = dzwiek.Dzwiek(1, 'c#')
        self.assertRaises(enum_bledy.BladDzwiekPozaTonacja, lambda: d.podaj_swoj_kod_wzgledny(tonacja.Tonacja('C')))

    def test_podaj_swoj_kod_2(self):
        d = dzwiek.Dzwiek(1, 'fb')
        self.assertRaises(enum_bledy.BladDzwiekPozaTonacja, lambda: d.podaj_swoj_kod_wzgledny(tonacja.Tonacja('C')))

    def test_podaj_swoj_kod_3(self):
        d = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d.podaj_swoj_kod_wzgledny(tonacja.Tonacja('C')), 8)

    def test_spojnosci_oktawy_i_kodu_wzglednego_1(self):
        d = dzwiek.Dzwiek(2, 'd')
        self.assertEqual(d.podaj_oktawe(), d.podaj_swoj_kod_wzgledny(tonacja.Tonacja('C')) // 7)

    def test_spojnosci_oktawy_i_kodu_wzglednego_2(self):
        d = dzwiek.Dzwiek(2, 'd')
        self.assertEqual(d.podaj_swoj_stopien(tonacja.Tonacja('C')),
                         d.podaj_swoj_kod_wzgledny(tonacja.Tonacja('C')) % 7)

    def test_kodu_bezwzglednego_1(self):
        d1 = dzwiek.Dzwiek(1, 'c##')
        d2 = dzwiek.Dzwiek(1, 'd')
        print(d1.podaj_swoj_kod_bezwzgledny())
        self.assertEqual(d1.podaj_swoj_kod_bezwzgledny(), d2.podaj_swoj_kod_bezwzgledny())

    def test_kodu_bezwzglednego_2(self):
        d1 = dzwiek.Dzwiek(1, 'c##')
        d2 = dzwiek.Dzwiek(1, 'db')
        self.assertNotEqual(d1.podaj_swoj_kod_bezwzgledny(), d2.podaj_swoj_kod_bezwzgledny())

    def test_kodu_bezwzglednego_3(self):
        d1 = dzwiek.Dzwiek(1, 'c')
        self.assertEqual(d1.podaj_swoj_kod_bezwzgledny(), 12)

    def test_kodu_bezwzglednego_4(self):
        d1 = dzwiek.Dzwiek(1, 'c#')
        self.assertEqual(d1.podaj_swoj_kod_bezwzgledny(), 13)

    def test_kodu_bezwzglednego_5(self):
        d1 = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d1.podaj_swoj_kod_bezwzgledny(), 14)

    def test_kodu_bezwzglednego_6(self):
        d1 = dzwiek.Dzwiek(1, 'h')
        self.assertEqual(d1.podaj_swoj_kod_bezwzgledny(), 23)

    def test_kodu_bezwzglednego_7(self):
        d1 = dzwiek.Dzwiek(2, 'c')
        self.assertEqual(d1.podaj_swoj_kod_bezwzgledny(), 24)


if __name__ == '__main__':
    unittest.main()

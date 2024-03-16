import unittest
import blad
import tonacja


# Testy działają i są wyczerpujące

class MyTestCase(unittest.TestCase):
    
    def test_konstruktora_1(self):
        """Sprawdza działanie konstruktora dla poprawnie podanych danych"""
        self.assertEqual(tonacja.Tonacja.tonacja_z_symbolu("C").czy_dur(), True)
        self.assertEqual(tonacja.Tonacja.tonacja_z_symbolu("Hb").czy_dur(), True)
        self.assertEqual(tonacja.Tonacja.tonacja_z_symbolu("c").czy_dur(), False)
        self.assertEqual(tonacja.Tonacja.tonacja_z_symbolu("d#").czy_dur(), False)
        self.assertEqual(tonacja.Tonacja.tonacja_z_symbolu("a").czy_dur(), False)

        self.assertEqual(tonacja.Tonacja.tonacja_z_symbolu("C").podaj_liste_nazw_dzwiekow(), ['c', 'd', 'e', 'f', 'g', 'a', 'h'])
        self.assertEqual(tonacja.Tonacja.tonacja_z_symbolu("C#").podaj_liste_nazw_dzwiekow(), ['c#', 'd#', 'e#', 'f#', 'g#', 'a#', 'h#'])
        self.assertEqual(tonacja.Tonacja.tonacja_z_symbolu("a#").podaj_liste_nazw_dzwiekow(), ['a#', 'h#', 'c#', 'd#', 'e#', 'f#', 'g##'])
        self.assertEqual(tonacja.Tonacja.tonacja_z_symbolu("eb").podaj_liste_nazw_dzwiekow(), ['eb', 'f', 'gb', 'ab', 'hb', 'cb', 'd'])

    def test_konstruktora(self):
        """Sprawdza działanie konstruktora dla NIEpoprawnie podanych danych - t durowa:
            a. Nieistniejąca tonacja mollowa
            b. Nieistniejąca tonacja durowa"""

        self.assertRaises(blad.BladTworzeniaTonacji, lambda: tonacja.Tonacja.tonacja_z_symbolu('a###'))
        self.assertRaises(blad.BladTworzeniaTonacji, lambda: tonacja.Tonacja.tonacja_z_symbolu('A###'))
        
    def test_podaj_nazwe_tonacji(self):
        testowa_t_1 = tonacja.Tonacja.tonacja_z_symbolu('C')
        self.assertEqual(testowa_t_1.podaj_symbol(), "C")

    def test_czy_dur_1(self):
        testowa_t_1 = tonacja.Tonacja.tonacja_z_symbolu('C')
        self.assertEqual(testowa_t_1.czy_dur(), True)

    def test_czy_dur_2(self):
        testowa_t_2 = tonacja.Tonacja.tonacja_z_symbolu('a')
        self.assertEqual(testowa_t_2.czy_dur(), False)

    def test_podaj_liste_nazw_dzwiekow(self):
        testowa_t_3 = tonacja.Tonacja.tonacja_z_symbolu('C')
        self.assertEqual(testowa_t_3.podaj_liste_nazw_dzwiekow(), ['c', 'd', 'e', 'f', 'g', 'a', 'h'])


if __name__ == '__main__':
    unittest.main()

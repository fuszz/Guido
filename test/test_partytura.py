import unittest
import akord
import dzwiek
from enumerations import enum_metrum
import partytura
import tonacja


class MyTestCase(unittest.TestCase):
    
    def test_podaj_metrum_1(self):
        p1 = partytura.Partytura(tonacja.Tonacja('C'), "3/4", 2)
        self.assertEqual(p1.podaj_metrum(), enum_metrum.Metrum.TRZY_CZWARTE)

    def test_podaj_metrum_2(self):
        p1 = partytura.Partytura(tonacja.Tonacja('C'), "4/4", 2)
        self.assertEqual(p1.podaj_metrum(), enum_metrum.Metrum.CZTERY_CZWARTE)

    def test_konstruktora_1(self):
        try:
            partytura.Partytura(tonacja.Tonacja('C'), "4/4", 2)
        except:
            self.fail("Niepoprawne działanie konstruktora")

    def test_konstruktora_2(self):
        try:
            partytura.Partytura(tonacja.Tonacja('C#'), "3/4", 2)
        except:
            self.fail("Niepoprawne działanie konstruktora")

    def test_konstruktora_3(self):
        self.assertRaises(ValueError, lambda: partytura.Partytura(tonacja.Tonacja('Z'), "3/4", 1))

    def test_konstruktora_4(self):
        self.assertRaises(ValueError, lambda: partytura.Partytura(tonacja.Tonacja('C'), "9/4", 1))

    def test_podaj_tonacje_1(self):
        p1 = partytura.Partytura(tonacja.Tonacja('C'), "4/4", 1)
        self.assertEqual(p1.podaj_tonacje().podaj_nazwe(), tonacja.Tonacja('C').podaj_nazwe())
        del p1

    def test_podaj_rzeczywista_liczbe_taktow_1(self):
        p1 = partytura.Partytura(tonacja.Tonacja('C'), "4/4", 1)
        for i in range(0):
            p1.zakoncz_takt()
        self.assertEqual(p1.podaj_rzeczywista_liczbe_taktow(), 0)
        del p1
    def test_podaj_rzeczywista_liczbe_taktow_2(self):
        p1 = partytura.Partytura(tonacja.Tonacja('C'), "4/4", 1)
        self.assertEqual(p1.podaj_rzeczywista_liczbe_taktow(), 0)
        del p1

    
    def test_podaj_zadeklarowana_liczbe_taktow(self):
        p1 = partytura.Partytura(tonacja.Tonacja('C'), "4/4", 9)
        self.assertEqual(p1.podaj_zadeklarowana_liczbe_taktow(), 9)
        del p1

    def test_podaj_liste_akordow_1(self):
        p2 = partytura.Partytura(tonacja.Tonacja('D'), "4/4", 3)
        self.assertEqual(p2.podaj_liste_akordow(), [])
        del p2
    def test_podaj_liste_akordow_2(self):
        p1 = partytura.Partytura(tonacja.Tonacja('C'), "4/4", 2)
        d1 = dzwiek.Dzwiek(1, 'c')
        a1 = akord.Akord(d1, d1, d1, d1, 2.0)
        p1.dodaj_akord(a1)
        self.assertEqual(p1.podaj_liste_akordow()[0], a1)

    
    def test_czy_poprawna_liczba_taktow_1(self):
        p1 = partytura.Partytura(tonacja.Tonacja('C'), "3/4", 1)
        p1.zakoncz_takt()
        self.assertEqual(p1.podaj_rzeczywista_liczbe_taktow() == p1.podaj_zadeklarowana_liczbe_taktow(),
                         p1.czy_poprawna_liczba_taktow())


if __name__ == '__main__':
    unittest.main()

import unittest
import akord
import dzwiek
import partytura
import tonacja
from enumerations import enum_metrum, enum_wartosci_nut
import blad


# Testy są ok - 14.03.2024

class MyTestCase(unittest.TestCase):

    def test_podaj_metrum_1(self):
        """Sprawdza, czy partytura poprawnie podaje swoje metrum"""
        p1 = partytura.Partytura(tonacja.Tonacja.tonacja_z_symbolu('C'), enum_metrum.Metrum("3/4"), 2)
        self.assertEqual(p1.podaj_metrum(), enum_metrum.Metrum.TRZY_CZWARTE)

    def test_podaj_metrum_2(self):
        p1 = partytura.Partytura(tonacja.Tonacja.tonacja_z_symbolu('C'), enum_metrum.Metrum("4/4"), 2)
        self.assertEqual(p1.podaj_metrum(), enum_metrum.Metrum.CZTERY_CZWARTE)
        del p1

    def test_konstruktora_1(self):
        """Weryfikuje poprawność użycia konstruktora. Oczekiwane zachowanie: brak błędów."""
        try:
            partytura.Partytura(tonacja.Tonacja.tonacja_z_symbolu('C'), enum_metrum.Metrum("3/4"), 2)
        except:
            self.fail("Niepoprawne działanie konstruktora")

    def test_konstruktora_2(self):
        try:
            partytura.Partytura(tonacja.Tonacja.tonacja_z_symbolu('C#'), enum_metrum.Metrum("3/4"), 2)
        except:
            self.fail("Niepoprawne działanie konstruktora")

    #    def test_konstruktora_3(self):
    #        """Sprawdza, czy możliwe jest utworzenie instancji Partytury z argumentów niepoprawnych typów"""
    #        partytura.Partytura(1, 2, enum_metrum.Metrum("3/4"))

    def test_podaj_tonacje_1(self):
        p1 = partytura.Partytura(tonacja.Tonacja.tonacja_z_symbolu('C'), enum_metrum.Metrum("3/4"), 1)
        self.assertEqual(p1.podaj_tonacje().podaj_symbol(), tonacja.Tonacja.tonacja_z_symbolu('C').podaj_symbol())
        del p1

    def test_podaj_rzeczywista_liczbe_taktow_1(self):
        """Sprawdza, czy partytura poprawnie zwraca liczbę zawartych w niej taktów. Liczba taktów: 1"""
        p1 = partytura.Partytura(tonacja.Tonacja.tonacja_z_symbolu('C'), enum_metrum.Metrum("3/4"), 1)
        for i in range(1):
            p1.zakoncz_takt()
        self.assertEqual(p1.podaj_rzeczywista_liczbe_taktow(), 1)
        del p1

    def test_podaj_rzeczywista_liczbe_taktow_2(self):
        """J.w., lcizba taktów: 0"""
        p1 = partytura.Partytura(tonacja.Tonacja.tonacja_z_symbolu('C'), enum_metrum.Metrum("3/4"), 1)
        self.assertEqual(p1.podaj_rzeczywista_liczbe_taktow(), 0)
        del p1

    def test_podaj_zadeklarowana_liczbe_taktow(self):
        """Sprawdza, czy partytura poprawnie zwraca deklarowaną liczbę taktów"""
        p1 = partytura.Partytura(tonacja.Tonacja.tonacja_z_symbolu('C'), enum_metrum.Metrum("3/4"), 9)
        self.assertEqual(p1.podaj_zadeklarowana_liczbe_taktow(), 9)
        del p1

    def test_podaj_liste_akordow_1(self):
        """Sprawdza, czy partytura poprawnie podaje liczbę akordów, które się w niej znajdują. Zawiera 0 akordów."""
        p2 = partytura.Partytura(tonacja.Tonacja.tonacja_z_symbolu('D'), enum_metrum.Metrum("3/4"), 3)
        self.assertEqual(p2.podaj_liste_akordow(), [])
        del p2

    def test_podaj_liste_akordow_2(self):
        """Sprawdza, czy partytura poprawnie podaje liczbę akordów, które się w niej znajdują. Zawiera 1 akord."""
        p1 = partytura.Partytura(tonacja.Tonacja.tonacja_z_symbolu('C'), enum_metrum.Metrum("3/4"), 2)
        d1 = dzwiek.Dzwiek(1, "c")
        wartosc = enum_wartosci_nut.WartosciNut(4)
        a1 = akord.Akord(d1, d1, d1, d1, wartosc)
        p1.dodaj_akord(a1)
        self.assertEqual(p1.podaj_liste_akordow()[0], a1)

    def test_czy_poprawna_liczba_taktow_1(self):
        p1 = partytura.Partytura(tonacja.Tonacja.tonacja_z_symbolu('C'), enum_metrum.Metrum("3/4"), 1)
        p1.zakoncz_takt()
        self.assertEqual(p1.podaj_rzeczywista_liczbe_taktow() == p1.podaj_zadeklarowana_liczbe_taktow(),
                         p1.czy_poprawna_liczba_taktow())


if __name__ == '__main__':
    unittest.main()

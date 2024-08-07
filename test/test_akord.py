import unittest

import akord
import blad
import dzwiek
import tonacja
from enumerations import enum_wartosci_nut, enum_przewroty, enum_skladnik_funkcji, enum_zdwojony_skladnik_funkcji
import funkcja


class TestyKlasyAKord(unittest.TestCase):
    def test_podaj_dlugosc_nuty(self):
        wartosc = enum_wartosci_nut.WartosciNut(6)
        nowy_akord = akord.Akord(dzwiek.Dzwiek(2, 'c'),
                                 dzwiek.Dzwiek(2, 'c'),
                                 dzwiek.Dzwiek(2, 'c'),
                                 dzwiek.Dzwiek(2, 'c'), wartosc)
        self.assertEqual(nowy_akord.podaj_dlugosc(), enum_wartosci_nut.WartosciNut.POLNUTA_Z_KROPKA)

    def test_ustal_funkcje_1(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        t = tonacja.Tonacja.stworz_z_symbolu('C')
        self.assertTrue(nowy_akord.ustal_funkcje(t) == funkcja.Funkcja.SUBDOMINANTA, t.czy_dur())

    def test_ustal_funkcje_2(self):
        d_b = dzwiek.Dzwiek(2, 'c')
        d_t = dzwiek.Dzwiek(3, 'e')
        d_a = dzwiek.Dzwiek(4, 'g')
        d_s = dzwiek.Dzwiek(4, 'c')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        t = tonacja.Tonacja.stworz_z_symbolu('C')
        self.assertTrue(nowy_akord.ustal_funkcje(t) == funkcja.Funkcja.TONIKA, t.czy_dur())

    def test_ustal_funkcje_3(self):
        d_b = dzwiek.Dzwiek(2, 'g')
        d_t = dzwiek.Dzwiek(3, 'h')
        d_a = dzwiek.Dzwiek(4, 'd')
        d_s = dzwiek.Dzwiek(4, 'g')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(nowy_akord.ustal_funkcje(tonacja.Tonacja.stworz_z_symbolu('C')) == funkcja.Funkcja.DOMINANTA)

    def test_ustal_funkcje_4(self):
        d_b = dzwiek.Dzwiek(2, 'g')
        d_t = dzwiek.Dzwiek(3, 'h')
        d_a = dzwiek.Dzwiek(4, 'd')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(
            nowy_akord.ustal_funkcje(tonacja.Tonacja.stworz_z_symbolu('C')) == funkcja.Funkcja.DOMINANTA_SEPTYMOWA)

    def test_ustal_funkcje_5(self):
        d_b = dzwiek.Dzwiek(2, 'c')
        d_t = dzwiek.Dzwiek(3, 'eb')
        d_a = dzwiek.Dzwiek(4, 'g')
        d_s = dzwiek.Dzwiek(4, 'c')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertEqual(nowy_akord.ustal_funkcje(tonacja.Tonacja.stworz_z_symbolu('c')).name,
                         funkcja.Funkcja.MOLL_TONIKA.name)

    def test_ustal_funkcje_6(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'ab')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(
            nowy_akord.ustal_funkcje(tonacja.Tonacja.stworz_z_symbolu('c')) == funkcja.Funkcja.MOLL_SUBDOMINANTA)

    def test_ustal_funkcje_10(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'd')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'g')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        t = tonacja.Tonacja.stworz_z_symbolu('C')
        self.assertRaises(blad.BladStopienPozaFunkcja, lambda: nowy_akord.ustal_funkcje(t))

    def test_ustal_funkcje_11(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(nowy_akord.ustal_funkcje(tonacja.Tonacja.stworz_z_symbolu('F')) != funkcja.Funkcja.DOMINANTA)

    def test_ustal_przewrot_1(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')

        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(nowy_akord.ustal_przewrot(
            tonacja.Tonacja.stworz_z_symbolu('F')) == enum_przewroty.Przewrot.POSTAC_ZASADNICZA)

    def test_ustal_przewrot_2(self):
        d_b = dzwiek.Dzwiek(2, 'a')
        d_t = dzwiek.Dzwiek(3, 'f')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(
            nowy_akord.ustal_przewrot(tonacja.Tonacja.stworz_z_symbolu('F')) == enum_przewroty.Przewrot.PIERWSZY)

    def test_ustal_przewrot_3(self):
        d_b = dzwiek.Dzwiek(2, 'c')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'f')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(
            nowy_akord.ustal_przewrot(tonacja.Tonacja.stworz_z_symbolu('F')) == enum_przewroty.Przewrot.DRUGI)

    def test_ustal_przewrot_4(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(nowy_akord.ustal_przewrot(
            tonacja.Tonacja.stworz_z_symbolu('Hb')) == enum_przewroty.Przewrot.POSTAC_ZASADNICZA)

    def test_ustal_przewrot_5(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(nowy_akord.ustal_przewrot(
            tonacja.Tonacja.stworz_z_symbolu('hb')) == enum_przewroty.Przewrot.POSTAC_ZASADNICZA)

    def test_ustal_przewrot_6(self):
        d_b = dzwiek.Dzwiek(2, 'd')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertRaises(blad.BladStopienPozaFunkcja,
                          lambda: nowy_akord.ustal_przewrot(tonacja.Tonacja.stworz_z_symbolu('Hb')))

    def test_ustal_przewrot_7(self):
        d_b = dzwiek.Dzwiek(2, 'd')
        d_t = dzwiek.Dzwiek(3, 'g')
        d_a = dzwiek.Dzwiek(4, 'h')
        d_s = dzwiek.Dzwiek(4, 'd')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertEqual(enum_przewroty.Przewrot.DRUGI,
                         nowy_akord.ustal_przewrot(tonacja.Tonacja.stworz_z_symbolu('C')))

    def test_ustal_pozycje_1(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')

        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(nowy_akord.ustal_pozycje(tonacja.Tonacja.stworz_z_symbolu('F')) ==
                        enum_skladnik_funkcji.SkladnikFunkcji.PRYMA)

    def test_ustal_pozycje_2(self):
        d_b = dzwiek.Dzwiek(2, 'a')
        d_t = dzwiek.Dzwiek(3, 'f')
        d_a = dzwiek.Dzwiek(4, 'f')
        d_s = dzwiek.Dzwiek(4, 'c')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(
            nowy_akord.ustal_pozycje(tonacja.Tonacja.stworz_z_symbolu('F')) ==
            enum_skladnik_funkcji.SkladnikFunkcji.KWINTA)

    def test_ustal_pozycje_3(self):
        d_b = dzwiek.Dzwiek(2, 'c')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'f')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(
            nowy_akord.ustal_pozycje(tonacja.Tonacja.stworz_z_symbolu("C")) ==
            enum_skladnik_funkcji.SkladnikFunkcji.PRYMA)

    def test_ustal_pozycje_4(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(nowy_akord.ustal_pozycje(
            tonacja.Tonacja.stworz_z_symbolu('Hb')) == enum_skladnik_funkcji.SkladnikFunkcji.PRYMA)

    def test_ustal_pozycje_5(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertTrue(nowy_akord.ustal_pozycje(
            tonacja.Tonacja.stworz_z_symbolu('hb')) == enum_skladnik_funkcji.SkladnikFunkcji.PRYMA)

    def test_ustal_pozycje_6(self):
        d_b = dzwiek.Dzwiek(2, 'g')
        d_t = dzwiek.Dzwiek(3, 'h')
        d_a = dzwiek.Dzwiek(4, 'd')
        d_s = dzwiek.Dzwiek(4, 'f')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertRaises(blad.BladDzwiekPozaTonacja,
                          lambda: nowy_akord.ustal_pozycje(tonacja.Tonacja.stworz_z_symbolu('D')))

    def test_ustal_zdwojony_dzwiek_jako_skladnik_funkcji_1(self):
        d_b = dzwiek.Dzwiek(2, 'c')
        d_t = dzwiek.Dzwiek(3, 'e')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'g')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertEqual(nowy_akord.podaj_zdwojony_skladnik(tonacja.Tonacja.C_DUR),
                         enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.PRYMA)

    def test_ustal_zdwojony_dzwiek_jako_skladnik_funkcji_2(self):
        d_b = dzwiek.Dzwiek(2, 'g')
        d_t = dzwiek.Dzwiek(3, 'h')
        d_a = dzwiek.Dzwiek(4, 'd')
        d_s = dzwiek.Dzwiek(4, 'h')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertEqual(nowy_akord.podaj_zdwojony_skladnik(tonacja.Tonacja.C_DUR),
                         enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.TERCJA)

    def test_ustal_zdwojony_dzwiek_jako_skladnik_funkcji_3(self):
        d_b = dzwiek.Dzwiek(2, 'g')
        d_t = dzwiek.Dzwiek(3, 'd')
        d_a = dzwiek.Dzwiek(4, 'd')
        d_s = dzwiek.Dzwiek(4, 'h')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertEqual(nowy_akord.podaj_zdwojony_skladnik(tonacja.Tonacja.C_DUR),
                         enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.KWINTA)

    def test_ustal_zdwojony_dzwiek_jako_skladnik_funkcji_4(self):
        d_b = dzwiek.Dzwiek(2, 'a')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'e')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertEqual(nowy_akord.podaj_zdwojony_skladnik(tonacja.Tonacja.A_MOLL),
                         enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.PRYMA)

    def test_ustal_zdwojony_dzwiek_jako_skladnik_funkcji_5(self):
        d_b = dzwiek.Dzwiek(2, 'a')
        d_t = dzwiek.Dzwiek(3, 'e')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'e')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertEqual(nowy_akord.podaj_zdwojony_skladnik(tonacja.Tonacja.A_MOLL),
                         enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.KWINTA)

    def test_ustal_zdwojony_dzwiek_jako_skladnik_funkcji_6(self):
        d_b = dzwiek.Dzwiek(2, 'e')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'c')
        wartosc = enum_wartosci_nut.WartosciNut(2)
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, wartosc)
        self.assertEqual(nowy_akord.podaj_zdwojony_skladnik(tonacja.Tonacja.A_MOLL),
                         enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.TERCJA)


if __name__ == '__main__':
    unittest.main()

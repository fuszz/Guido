import unittest
from partytura import Partytura
from akord import Akord
from enumerations.enum_nazwy_interwalow import NazwaInterwalu
from enumerations.enum_wartosci_nut import WartosciNut
from enumerations.enum_metrum import Metrum
from dzwiek import Dzwiek
from tonacja import Tonacja
import sprawdzarka_warstwa_4 as spr_w_4


class TestWarstwy4Sprawdzarki(unittest.TestCase):

    def test_sygn_i_glosy_z_rownoleglosciami_o_interwal_1(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 4)
        tonika = Akord(Dzwiek(4, "c"),
                       Dzwiek(4, "e"),
                       Dzwiek(4, "g"),
                       Dzwiek(4, "c"),
                       WartosciNut.CWIERCNUTA)
        par.dodaj_akord(tonika)
        par.dodaj_akord(tonika)
        par.zakoncz_takt()
        self.assertEqual([], spr_w_4.sygn_i_glosy_z_rownoleglosciami(par, NazwaInterwalu.KWINTA_CZYSTA))

    def test_sygn_i_glosy_z_rownoleglosciami_o_interwal_2(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 4)
        tonika = Akord(Dzwiek(5, "c"),
                       Dzwiek(4, "e"),
                       Dzwiek(4, "g"),
                       Dzwiek(4, "c"),
                       WartosciNut.CWIERCNUTA)
        dominanta = Akord(Dzwiek(6, "g"),
                          Dzwiek(4, "h"),
                          Dzwiek(5, "d"),
                          Dzwiek(5, "g"),
                          WartosciNut.CWIERCNUTA)
        par.dodaj_akord(tonika)
        par.dodaj_akord(dominanta)
        par.dodaj_akord(tonika)
        par.zakoncz_takt()
        par.dodaj_akord(dominanta)
        par.zakoncz_takt()
        self.assertEqual([(0, 1, "SB "), (0, 2, "SB "), (1, 0, "SB ")],
                         spr_w_4.sygn_i_glosy_z_rownoleglosciami(par, NazwaInterwalu.PRYMA_CZYSTA))

    def test_sygn_i_glosy_z_rownoleglosciami_o_interwal_3(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 4)
        tonika = Akord(Dzwiek(5, "g"),
                       Dzwiek(4, "e"),
                       Dzwiek(4, "c"),
                       Dzwiek(3, "c"),
                       WartosciNut.CWIERCNUTA)
        dominanta = Akord(Dzwiek(6, "d"),
                          Dzwiek(4, "h"),
                          Dzwiek(5, "g"),
                          Dzwiek(4, "g"),
                          WartosciNut.CWIERCNUTA)
        par.dodaj_akord(tonika)
        par.dodaj_akord(dominanta)
        par.zakoncz_takt()
        self.assertEqual([(0, 1, "ST SB ")], spr_w_4.sygn_i_glosy_z_rownoleglosciami(par, NazwaInterwalu.KWINTA_CZYSTA))

    def test_sygn_gdzie_ruch_glosow_w_tym_samym_kierunku_1(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 4)
        par.dodaj_akord(Akord(Dzwiek(1, "c"),
                              Dzwiek(1, "d"),
                              Dzwiek(2, "e"),
                              Dzwiek(2, "c"),
                              WartosciNut.CWIERCNUTA))

        par.dodaj_akord(Akord(Dzwiek(2, "c"),
                              Dzwiek(2, "d"),
                              Dzwiek(3, "e"),
                              Dzwiek(3, "c"),
                              WartosciNut.CWIERCNUTA))

        par.dodaj_akord(Akord(Dzwiek(2, "c"),
                              Dzwiek(3, "d"),
                              Dzwiek(1, "e"),
                              Dzwiek(3, "c"),
                              WartosciNut.CWIERCNUTA))

        par.dodaj_akord(Akord(Dzwiek(0, "c"),
                              Dzwiek(0, "d"),
                              Dzwiek(0, "e"),
                              Dzwiek(0, "c"),
                              WartosciNut.CWIERCNUTA))
        par.zakoncz_takt()
        par.dodaj_akord(Akord(Dzwiek(2, "c"),
                              Dzwiek(3, "d"),
                              Dzwiek(1, "e"),
                              Dzwiek(3, "c"),
                              WartosciNut.CWIERCNUTA))

        par.dodaj_akord(Akord(Dzwiek(0, "c"),
                              Dzwiek(0, "d"),
                              Dzwiek(0, "e"),
                              Dzwiek(0, "c"),
                              WartosciNut.CWIERCNUTA))
        self.assertEqual([(0, 1), (0, 3), (1, 0), (1, 1)], spr_w_4.sygn_gdzie_ruch_glosow_w_tym_samym_kierunku(par))

    def test_sygn_i_glosy_gdzie_ruch_glosu_o_interwal_zwiekszony_1(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 4)
        par.dodaj_akord(Akord(Dzwiek(1, "f"),
                              Dzwiek(1, "f"),
                              Dzwiek(2, "f"),
                              Dzwiek(2, "f"),
                              WartosciNut.CWIERCNUTA))

        par.dodaj_akord(Akord(Dzwiek(2, "h"),
                              Dzwiek(2, "h"),
                              Dzwiek(3, "h"),
                              Dzwiek(3, "h"),
                              WartosciNut.CWIERCNUTA))
        par.dodaj_akord(Akord(Dzwiek(1, "f"),
                              Dzwiek(1, "f"),
                              Dzwiek(2, "f"),
                              Dzwiek(2, "f"),
                              WartosciNut.CWIERCNUTA))

        par.dodaj_akord(Akord(Dzwiek(2, "h"),
                              Dzwiek(2, "h"),
                              Dzwiek(3, "h"),
                              Dzwiek(3, "h"),
                              WartosciNut.CWIERCNUTA))
        self.assertEqual([(0, 1, "SATB"), (0, 2, "SATB"), (0, 3, "SATB")],
                         spr_w_4.sygn_i_glosy_gdzie_ruch_glosu_o_interwal_zwiekszony(par))

    def test_sygn_i_glosy_gdzie_ruch_o_zbyt_duzy_interwal_1(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 4)
        par.dodaj_akord(Akord(Dzwiek(1, "f"),
                              Dzwiek(1, "f"),
                              Dzwiek(2, "f"),
                              Dzwiek(2, "f"),
                              WartosciNut.CWIERCNUTA))

        par.dodaj_akord(Akord(Dzwiek(2, "h"),
                              Dzwiek(2, "h"),
                              Dzwiek(3, "h"),
                              Dzwiek(3, "h"),
                              WartosciNut.CWIERCNUTA))
        self.assertEqual([(0, 1, "SATB")], spr_w_4.sygn_i_glosy_gdzie_ruch_o_septyme(par))

    def test_czy_rozwiazanie_dominanty_jest_poprawne_1(self):
        dominanta = Akord(Dzwiek(3, "g"),
                          Dzwiek(3, "h"),
                          Dzwiek(4, "d"),
                          Dzwiek(4, "g"),
                          WartosciNut.CWIERCNUTA)
        tonika = Akord(Dzwiek(3, "c"),
                       Dzwiek(4, "c"),
                       Dzwiek(4, "e"),
                       Dzwiek(4, "g"),
                       WartosciNut.CWIERCNUTA)
        self.assertTrue(spr_w_4.czy_rozwiazanie_dominanty_jest_poprawne(dominanta, tonika, Tonacja.C_DUR))

    def test_czy_rozwiazanie_dominanty_jest_poprawne_2(self):
        dominanta = Akord(Dzwiek(3, "g"),
                          Dzwiek(3, "h"),
                          Dzwiek(4, "d"),
                          Dzwiek(4, "g"),
                          WartosciNut.CWIERCNUTA)
        tonika = Akord(Dzwiek(3, "c"),
                       Dzwiek(4, "g"),
                       Dzwiek(4, "e"),
                       Dzwiek(4, "c"),
                       WartosciNut.CWIERCNUTA)
        self.assertFalse(spr_w_4.czy_rozwiazanie_dominanty_jest_poprawne(dominanta, tonika, Tonacja.C_DUR))

    def test_czy_rozwiazanie_dominanty_jest_poprawne_3(self):
        dominanta = Akord(Dzwiek(3, "g"),
                          Dzwiek(3, "h"),
                          Dzwiek(4, "d"),
                          Dzwiek(4, "g"),
                          WartosciNut.CWIERCNUTA)
        tonika = Akord(Dzwiek(3, "c"),
                       Dzwiek(4, "c"),
                       Dzwiek(4, "eb"),
                       Dzwiek(4, "g"),
                       WartosciNut.CWIERCNUTA)
        self.assertTrue(spr_w_4.czy_rozwiazanie_dominanty_jest_poprawne(dominanta, tonika, Tonacja.C_MOLL))

    def test_czy_rozwiazanie_dominanty_jest_poprawne_4(self):
        dominanta = Akord(Dzwiek(3, "g"),
                          Dzwiek(3, "h"),
                          Dzwiek(4, "d"),
                          Dzwiek(4, "g"),
                          WartosciNut.CWIERCNUTA)
        tonika = Akord(Dzwiek(3, "c"),
                       Dzwiek(4, "g"),
                       Dzwiek(4, "eb"),
                       Dzwiek(4, "c"),
                       WartosciNut.CWIERCNUTA)
        self.assertFalse(spr_w_4.czy_rozwiazanie_dominanty_jest_poprawne(dominanta, tonika, Tonacja.C_MOLL))

    def test_czy_rozwiazanie_d7_jest_poprawne_1(self):
        dominanta = Akord(Dzwiek(3, "g"),
                          Dzwiek(3, "h"),
                          Dzwiek(4, "d"),
                          Dzwiek(4, "f"),
                          WartosciNut.CWIERCNUTA)
        tonika = Akord(Dzwiek(3, "c"),
                       Dzwiek(4, "c"),
                       Dzwiek(4, "g"),
                       Dzwiek(4, "e"),
                       WartosciNut.CWIERCNUTA)
        self.assertTrue(spr_w_4.czy_rozwiazanie_d7_jest_poprawne(dominanta, tonika, Tonacja.C_DUR))

    def test_czy_rozwiazanie_d7_jest_poprawne_2(self):
        dominanta = Akord(Dzwiek(3, "g"),
                          Dzwiek(3, "h"),
                          Dzwiek(4, "d"),
                          Dzwiek(4, "f"),
                          WartosciNut.CWIERCNUTA)
        tonika = Akord(Dzwiek(3, "c"),
                       Dzwiek(4, "g"),
                       Dzwiek(4, "e"),
                       Dzwiek(4, "c"),
                       WartosciNut.CWIERCNUTA)
        self.assertFalse(spr_w_4.czy_rozwiazanie_dominanty_jest_poprawne(dominanta, tonika, Tonacja.C_DUR))

    def test_czy_rozwiazanie_d7_jest_poprawne_3(self):
        dominanta = Akord(Dzwiek(3, "g"),
                          Dzwiek(3, "h"),
                          Dzwiek(4, "d"),
                          Dzwiek(4, "f"),
                          WartosciNut.CWIERCNUTA)
        tonika = Akord(Dzwiek(3, "c"),
                       Dzwiek(4, "c"),
                       Dzwiek(4, "g"),
                       Dzwiek(4, "eb"),
                       WartosciNut.CWIERCNUTA)
        self.assertTrue(spr_w_4.czy_rozwiazanie_d7_jest_poprawne(dominanta, tonika, Tonacja.C_MOLL))

    def test_czy_rozwiazanie_d7_jest_poprawne_4(self):
        dominanta = Akord(Dzwiek(3, "g"),
                          Dzwiek(3, "h"),
                          Dzwiek(4, "d"),
                          Dzwiek(4, "f"),
                          WartosciNut.CWIERCNUTA)
        tonika = Akord(Dzwiek(3, "c"),
                       Dzwiek(4, "g"),
                       Dzwiek(4, "eb"),
                       Dzwiek(4, "c"),
                       WartosciNut.CWIERCNUTA)
        self.assertFalse(spr_w_4.czy_rozwiazanie_dominanty_jest_poprawne(dominanta, tonika, Tonacja.C_MOLL))


if __name__ == '__main__':
    unittest.main()

import unittest
from partytura import Partytura
from akord import Akord
from enumerations.enum_mozliwe_interwaly import MozliweInterwaly
from enumerations.enum_wartosci_nut import WartosciNut
from enumerations.enum_metrum import Metrum
from dzwiek import Dzwiek
import blad
from tonacja import Tonacja
import sprawdzarka_warstwa_4 as spr_w_4


class TestWarstwy4Sprawdzarki(unittest.TestCase):


    def test_sygn_i_glosy_z_polaczeniem_kwintami_rownoleglymi_1(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 4)
        tonika = Akord(Dzwiek(4, "c"),
                       Dzwiek(4, "e"),
                       Dzwiek(4, "g"),
                       Dzwiek(4, "c"),
                       WartosciNut.CWIERCNUTA)
        par.dodaj_akord(tonika)
        par.dodaj_akord(tonika)
        par.zakoncz_takt()
        self.assertEqual([(0, 1, "ST,TB,")], spr_w_4.sygn_i_glosy_z_polaczeniem_kwintami_rownoleglymi(par))

    def test_sygn_i_glosy_z_polaczeniem_oktawami_rownoleglymi_1(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 4)
        tonika = Akord(Dzwiek(4, "c"),
                       Dzwiek(4, "e"),
                       Dzwiek(4, "g"),
                       Dzwiek(5, "c"),
                       WartosciNut.CWIERCNUTA)
        par.dodaj_akord(tonika)
        par.dodaj_akord(tonika)
        par.zakoncz_takt()
        self.assertEqual([(0, 1, "SB,")], spr_w_4.sygn_i_glosy_z_polaczeniem_oktawami_rownoleglymi(par))

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
        self.assertEqual([(0, 1), (0, 3)], spr_w_4.sygn_gdzie_ruch_glosow_w_tym_samym_kierunku(par))

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
        self.assertEqual([(0, 1, "SATB")], spr_w_4.sygn_i_glosy_gdzie_ruch_glosu_o_interwal_zwiekszony(par))

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
        self.assertEqual([(0, 1, "SATB")], spr_w_4.sygn_i_glosy_gdzie_ruch_o_zbyt_duzy_interwal(par))


if __name__ == '__main__':
    unittest.main()

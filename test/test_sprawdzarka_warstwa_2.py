import unittest
from partytura import Partytura
from tonacja import Tonacja
from dzwiek import Dzwiek
from enumerations.enum_metrum import Metrum
from akord import Akord
from enumerations.enum_wartosci_nut import WartosciNut
import sprawdzarka_warstwa_2 as sprawdzarka


class TestWarstwy2Sprawdzarki(unittest.TestCase):
    def test_sygn_i_glosy_akordow_gdzie_glosy_poza_skalami_1(self):
        par = Partytura(Tonacja.F_DUR, Metrum.TRZY_CZWARTE, 2)
        d_s = Dzwiek(4, 'c')
        d_a = Dzwiek(3, 'h')
        d_t = Dzwiek(3, 'h')
        d_b = Dzwiek(2, 'h')
        akord_a = Akord(d_s, d_a, d_t, d_b, WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        self.assertEqual([], sprawdzarka.sygn_i_glosy_akordow_gdzie_glosy_poza_skalami(par))

    def test_sygn_i_glosy_akordow_gdzie_glosy_poza_skalami_2(self):
        par = Partytura(Tonacja.F_DUR, Metrum.TRZY_CZWARTE, 2)
        d_s = Dzwiek(6, 'c')
        d_a = Dzwiek(3, 'h')
        d_t = Dzwiek(3, 'h')
        d_b = Dzwiek(2, 'h')
        akord_a = Akord(d_s, d_a, d_t, d_b, WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        self.assertEqual([(0, 0, "S")], sprawdzarka.sygn_i_glosy_akordow_gdzie_glosy_poza_skalami(par))

    def test_sygn_akordow_nietworzacych_funkcji_1(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 2)
        akord_a = Akord(Dzwiek(4, "c"),
                        Dzwiek(4, "e"),
                        Dzwiek(4, "g"),
                        Dzwiek(4, "c"),
                        WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        akord_b = Akord(Dzwiek(4, "c"),
                        Dzwiek(5, "d"),
                        Dzwiek(5, "f"),
                        Dzwiek(5, "g"),
                        WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_b)
        self.assertEqual([(0, 1)], sprawdzarka.sygn_akordow_nietworzacych_funkcji(par))

    def test_sygn_akordow_nietworzacych_funkcji_2(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 2)
        akord_a = Akord(Dzwiek(4, "c"),
                        Dzwiek(4, "e"),
                        Dzwiek(4, "g"),
                        Dzwiek(4, "c"),
                        WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        par.zakoncz_takt()
        akord_b = Akord(Dzwiek(4, "c"),
                        Dzwiek(5, "d"),
                        Dzwiek(5, "f"),
                        Dzwiek(5, "g"),
                        WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_b)
        self.assertEqual([(1, 0)], sprawdzarka.sygn_akordow_nietworzacych_funkcji(par))

    def test_sygn_i_glosy_gdzie_przekroczone_odleglosci_1(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 2)
        akord_a = Akord(Dzwiek(4, "c"),
                        Dzwiek(4, "e"),
                        Dzwiek(4, "g"),
                        Dzwiek(4, "c"),
                        WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        par.zakoncz_takt()
        akord_b = Akord(Dzwiek(4, "c"),
                        Dzwiek(5, "d"),
                        Dzwiek(5, "f"),
                        Dzwiek(5, "g"),
                        WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_b)
        self.assertEqual([(2, 0, "SA (1, SEKUNDA_WIELKA), ")],
                         sprawdzarka.sygn_i_glosy_gdzie_przekroczone_odleglosci(par))


if __name__ == '__main__':
    unittest.main()

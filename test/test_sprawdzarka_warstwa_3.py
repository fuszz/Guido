import unittest

import sprawdzarka_warstwa_3
from dzwiek import Dzwiek
from akord import Akord
from enumerations.enum_metrum import Metrum
from enumerations.enum_wartosci_nut import WartosciNut
from partytura import Partytura
import sprawdzarka_warstwa_3 as spr_w_3
from tonacja import Tonacja


class TestWarstwy3Sprawdzarki(unittest.TestCase):
    def test_czy_pierwsza_i_ostatnia_tonika_1(self):
        d_a = Dzwiek(3, 'c')
        d_b = Dzwiek(4, 'e')
        d_c = Dzwiek(3, 'g')
        d_d = Dzwiek(4, 'c')
        akord_a = Akord(d_a, d_b, d_c, d_d, WartosciNut.CWIERCNUTA)
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 1)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.zakoncz_takt()
        self.assertEqual(True, spr_w_3.czy_pierwsza_i_ostatnia_tonika(par))

    def test_czy_pierwsza_i_ostatnia_tonika_2(self):
        d_a = Dzwiek(3, 'c')
        d_b = Dzwiek(4, 'e')
        d_c = Dzwiek(3, 'g')
        d_d = Dzwiek(4, 'c')
        akord_a = Akord(d_a, d_b, d_c, d_d, WartosciNut.CWIERCNUTA)
        par = Partytura(Tonacja.F_DUR, Metrum.TRZY_CZWARTE, 1)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.zakoncz_takt()
        self.assertEqual(False, spr_w_3.czy_pierwsza_i_ostatnia_tonika(par))

    def test_czy_ostateczne_rozwiazanie_nie_jest_w_drugim_przewrocie_1(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 4)
        akd = Akord(Dzwiek(4, "c"),
                    Dzwiek(4, "e"),
                    Dzwiek(4, "g"),
                    Dzwiek(4, "c"),
                    WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akd)
        par.zakoncz_takt()
        self.assertEqual(True, spr_w_3.czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(par))

    def test_czy_ostateczne_rozwiazanie_nie_jest_w_drugim_przewrocie_2(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 4)
        akd = Akord(Dzwiek(4, "c"),
                    Dzwiek(4, "e"),
                    Dzwiek(4, "g"),
                    Dzwiek(4, "g"),
                    WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akd)
        par.zakoncz_takt()
        self.assertEqual(False, spr_w_3.czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(par))

    def test_sygn_subdominant_po_dominancie_1(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 2)
        tonika = Akord(Dzwiek(4, "c"),
                       Dzwiek(4, "e"),
                       Dzwiek(4, "g"),
                       Dzwiek(4, "c"),
                       WartosciNut.CWIERCNUTA)
        subdominanta = Akord(Dzwiek(5, "f"),
                             Dzwiek(5, "a"),
                             Dzwiek(5, "c"),
                             Dzwiek(5, "c"),
                             WartosciNut.CWIERCNUTA)
        dominanta = Akord(Dzwiek(1, "g"),
                          Dzwiek(1, "h"),
                          Dzwiek(1, "d"),
                          Dzwiek(1, "g"),
                          WartosciNut.CWIERCNUTA)
        par.dodaj_akord(tonika)
        par.dodaj_akord(subdominanta)
        par.dodaj_akord(dominanta)
        par.zakoncz_takt()
        par.dodaj_akord(tonika)
        par.dodaj_akord(dominanta)
        par.dodaj_akord(tonika)
        par.zakoncz_takt()
        self.assertEqual([], spr_w_3.sygn_subdominant_po_dominancie(par))
        par.dodaj_akord(dominanta)
        par.dodaj_akord(subdominanta)
        par.dodaj_akord(dominanta)
        par.zakoncz_takt()
        self.assertEqual([(2, 1)], spr_w_3.sygn_subdominant_po_dominancie(par))

    def test_nr_taktu_gdzie_drugi_przewrot_na_raz_1(self):
        bez = Akord(Dzwiek(4, "c"),
                    Dzwiek(4, "e"),
                    Dzwiek(4, "g"),
                    Dzwiek(4, "c"),
                    WartosciNut.CWIERCNUTA)
        pierwszy = Akord(Dzwiek(5, "a"),
                         Dzwiek(5, "f"),
                         Dzwiek(5, "c"),
                         Dzwiek(5, "f"),
                         WartosciNut.CWIERCNUTA)
        drugi = Akord(Dzwiek(1, "g"),
                      Dzwiek(1, "h"),
                      Dzwiek(1, "g"),
                      Dzwiek(1, "d"),
                      WartosciNut.CWIERCNUTA)
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 2)
        par.dodaj_akord(bez)
        par.dodaj_akord(pierwszy)
        par.zakoncz_takt()
        par.dodaj_akord(drugi)
        par.zakoncz_takt()
        par.dodaj_akord(pierwszy)
        par.dodaj_akord(bez)
        par.zakoncz_takt()
        self.assertEqual([1], spr_w_3.nr_taktu_gdzie_drugi_przewrot_na_raz(par))

    def test_nr_taktu_z_przetrzymana_przez_kreske_taktowa_funkcja(self):
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 2)
        par.dodaj_akord(Akord(Dzwiek(4, "c"),
                              Dzwiek(4, "e"),
                              Dzwiek(4, "g"),
                              Dzwiek(4, "c"),
                              WartosciNut.CWIERCNUTA))
        par.zakoncz_takt()
        par.dodaj_akord(Akord(Dzwiek(4, "c"),
                              Dzwiek(4, "e"),
                              Dzwiek(4, "g"),
                              Dzwiek(4, "c"),
                              WartosciNut.CWIERCNUTA))
        par.zakoncz_takt()
        self.assertEqual([1], sprawdzarka_warstwa_3.nr_taktu_z_przetrzymana_przez_kreske_taktowa_funkcja(par))


if __name__ == '__main__':
    unittest.main()

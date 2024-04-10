import unittest
import sprawdzarka_warstwa_1 as spr_w_1
from dzwiek import Dzwiek
from akord import Akord
from tonacja import Tonacja
from enumerations.enum_wartosci_nut import WartosciNut
from enumerations.enum_metrum import Metrum
from partytura import Partytura


class TestyWarstwy1Sprawdzarki(unittest.TestCase):

    def test_czy_liczba_taktow_jest_poprawna_1(self):
        par = Partytura(Tonacja.F_DUR, Metrum.TRZY_CZWARTE, 1)
        self.assertEqual(False, spr_w_1.czy_liczba_taktow_jest_poprawna(par))

    def test_nr_taktow_z_nieodpowiednimi_dlugosciami_1(self):
        par = Partytura(Tonacja.F_DUR, Metrum.TRZY_CZWARTE, 2)
        d_a = Dzwiek(3, 'c')
        d_b = Dzwiek(4, 'e')
        d_c = Dzwiek(3, 'g')
        d_d = Dzwiek(4, 'c')
        akord_a = Akord(d_a, d_b, d_c, d_d, WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.zakoncz_takt()
        par.zakoncz_takt()
        self.assertEqual([1], spr_w_1.nr_taktow_z_nieodpowiednimi_dlugosciami(par))

    def test_nr_taktow_z_nieodpowiednimi_dlugosciami_2(self):
        par = Partytura(Tonacja.F_DUR, Metrum.TRZY_CZWARTE, 2)
        d_a = Dzwiek(3, 'c')
        d_b = Dzwiek(4, 'e')
        d_c = Dzwiek(3, 'g')
        d_d = Dzwiek(4, 'c')
        akord_a = Akord(d_a, d_b, d_c, d_d, WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.zakoncz_takt()
        self.assertEqual([0], spr_w_1.nr_taktow_z_nieodpowiednimi_dlugosciami(par))

    def test_czy_liczba_taktow_jest_poprawna_2(self):
        par = Partytura(Tonacja.F_DUR, Metrum.TRZY_CZWARTE, 1)
        par.zakoncz_takt()
        self.assertEqual(True, spr_w_1.czy_liczba_taktow_jest_poprawna(par))

    def test_czy_w_akordzie_sa_dzwieki_obce_1(self):
        d_a = Dzwiek(3, 'c')
        d_b = Dzwiek(4, 'd')
        d_c = Dzwiek(3, 'c')
        d_d = Dzwiek(4, 'd')
        akord_a = Akord(d_a, d_b, d_c, d_d, WartosciNut.POLNUTA)
        self.assertEqual(False, spr_w_1.czy_w_akordzie_sa_dzwieki_obce(akord_a, Tonacja.C_DUR))

    def test_czy_w_akordzie_sa_dzwieki_obce_2(self):
        d_a = Dzwiek(3, 'c#')
        d_b = Dzwiek(4, 'd')
        d_c = Dzwiek(3, 'c')
        d_d = Dzwiek(4, 'd')
        akord_a = Akord(d_a, d_b, d_c, d_d, WartosciNut.POLNUTA)
        self.assertEqual(True, spr_w_1.czy_w_akordzie_sa_dzwieki_obce(akord_a, Tonacja.C_DUR))

    def test_sygn_akordow_z_dzwiekami_obcymi_1(self):
        d_a = Dzwiek(3, 'c')
        d_b = Dzwiek(4, 'd')
        d_c = Dzwiek(3, 'c')
        d_d = Dzwiek(4, 'd')
        akord_a = Akord(d_a, d_b, d_c, d_d, WartosciNut.POLNUTA)
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 1)
        par.dodaj_akord(akord_a)
        self.assertEqual([], spr_w_1.sygn_akordow_z_dzwiekami_obcymi(par))

    def test_sygn_akordow_z_dzwiekami_obcymi_2(self):
        d_a = Dzwiek(3, 'c#')
        d_b = Dzwiek(4, 'd')
        d_c = Dzwiek(3, 'c')
        d_d = Dzwiek(4, 'd')
        akord_a = Akord(d_a, d_b, d_c, d_d, WartosciNut.POLNUTA)
        par = Partytura(Tonacja.C_DUR, Metrum.TRZY_CZWARTE, 1)
        par.dodaj_akord(akord_a)
        self.assertEqual([(0, 0)], spr_w_1.sygn_akordow_z_dzwiekami_obcymi(par))


if __name__ == '__main__':
    unittest.main()

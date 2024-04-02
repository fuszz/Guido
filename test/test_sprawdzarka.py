import unittest
import partytura
import akord
from enumerations import enum_interwal, enum_wartosci_nut, enum_metrum
import dzwiek
import blad
import sprawdzarka
import tonacja


class TestSprawdzarka(unittest.TestCase):
    def test_podaj_interwal_test1(self):
        dzwiek_a = dzwiek.Dzwiek(2, 'c')
        dzwiek_b = dzwiek.Dzwiek(2, 'd')
        self.assertEqual((0, enum_interwal.Interwal.SEKUNDA_WIELKA),
                         sprawdzarka.podaj_interwal(dzwiek_a, dzwiek_b, tonacja.Tonacja.C_DUR))

    def test_podaj_interwal_test2(self):
        dzwiek_a = dzwiek.Dzwiek(2, 'c')
        dzwiek_b = dzwiek.Dzwiek(2, 'd')
        self.assertEqual((0, enum_interwal.Interwal.SEKUNDA_WIELKA),
                         sprawdzarka.podaj_interwal(dzwiek_a, dzwiek_b, tonacja.Tonacja.A_MOLL))

    def test_podaj_interwal_test3(self):
        dzwiek_a = dzwiek.Dzwiek(2, 'c#')
        dzwiek_b = dzwiek.Dzwiek(2, 'd')
        with self.assertRaises(blad.BladDzwiekPozaTonacja):
            sprawdzarka.podaj_interwal(dzwiek_a, dzwiek_b, tonacja.Tonacja.A_MOLL)

    def test_podaj_interwal_test4(self):
        dzwiek_a = dzwiek.Dzwiek(3, 'c')
        dzwiek_b = dzwiek.Dzwiek(4, 'd')
        self.assertEqual((1, enum_interwal.Interwal.SEKUNDA_WIELKA),
                         sprawdzarka.podaj_interwal(dzwiek_a, dzwiek_b, tonacja.Tonacja.A_MOLL))

    def test_czy_w_akordzie_sa_dzwieki_obce(self):
        d_a = dzwiek.Dzwiek(3, 'c')
        d_b = dzwiek.Dzwiek(4, 'd')
        d_c = dzwiek.Dzwiek(3, 'c')
        d_d = dzwiek.Dzwiek(4, 'd')
        akord_a = akord.Akord(d_a, d_b, d_c, d_d, enum_wartosci_nut.WartosciNut.POLNUTA)
        self.assertEqual(False, sprawdzarka.czy_w_akordzie_sa_dzwieki_obce(akord_a, tonacja.Tonacja.C_DUR))

    def test_czy_w_akordzie_sa_dzwieki_obce2(self):
        d_a = dzwiek.Dzwiek(3, 'c#')
        d_b = dzwiek.Dzwiek(4, 'd')
        d_c = dzwiek.Dzwiek(3, 'c')
        d_d = dzwiek.Dzwiek(4, 'd')
        akord_a = akord.Akord(d_a, d_b, d_c, d_d, enum_wartosci_nut.WartosciNut.POLNUTA)
        self.assertEqual(True, sprawdzarka.czy_w_akordzie_sa_dzwieki_obce(akord_a, tonacja.Tonacja.C_DUR))

    def test_czy_w_partyturze_sa_dzwieki_obce_1(self):
        d_a = dzwiek.Dzwiek(3, 'c')
        d_b = dzwiek.Dzwiek(4, 'd')
        d_c = dzwiek.Dzwiek(3, 'c')
        d_d = dzwiek.Dzwiek(4, 'd')
        akord_a = akord.Akord(d_a, d_b, d_c, d_d, enum_wartosci_nut.WartosciNut.POLNUTA)
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 1)
        par.dodaj_akord(akord_a)
        self.assertEqual(False, sprawdzarka.czy_w_partyturze_sa_dzwieki_obce(par))

    def test_czy_w_partyturze_sa_dzwieki_obce_2(self):
        d_a = dzwiek.Dzwiek(3, 'c#')
        d_b = dzwiek.Dzwiek(4, 'd')
        d_c = dzwiek.Dzwiek(3, 'c')
        d_d = dzwiek.Dzwiek(4, 'd')
        akord_a = akord.Akord(d_a, d_b, d_c, d_d, enum_wartosci_nut.WartosciNut.POLNUTA)
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 1)
        par.dodaj_akord(akord_a)
        self.assertEqual(True, sprawdzarka.czy_w_partyturze_sa_dzwieki_obce(par))

    def test_czy_pierwsza_i_ostatnia_tonika_1(self):
        d_a = dzwiek.Dzwiek(3, 'c')
        d_b = dzwiek.Dzwiek(4, 'e')
        d_c = dzwiek.Dzwiek(3, 'g')
        d_d = dzwiek.Dzwiek(4, 'c')
        akord_a = akord.Akord(d_a, d_b, d_c, d_d, enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 1)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.zakoncz_takt()
        self.assertEqual(True, sprawdzarka.czy_pierwsza_i_ostatnia_tonika(par))

    def test_czy_pierwsza_i_ostatnia_tonika_2(self):
        d_a = dzwiek.Dzwiek(3, 'c')
        d_b = dzwiek.Dzwiek(4, 'e')
        d_c = dzwiek.Dzwiek(3, 'g')
        d_d = dzwiek.Dzwiek(4, 'c')
        akord_a = akord.Akord(d_a, d_b, d_c, d_d, enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par = partytura.Partytura(tonacja.Tonacja.F_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 1)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.zakoncz_takt()
        self.assertEqual(False, sprawdzarka.czy_pierwsza_i_ostatnia_tonika(par))

if __name__ == '__main__':
    unittest.main()

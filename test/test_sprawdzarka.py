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
        self.assertEqual([], sprawdzarka.czy_w_partyturze_sa_dzwieki_obce(par))

    def test_czy_w_partyturze_sa_dzwieki_obce_2(self):
        d_a = dzwiek.Dzwiek(3, 'c#')
        d_b = dzwiek.Dzwiek(4, 'd')
        d_c = dzwiek.Dzwiek(3, 'c')
        d_d = dzwiek.Dzwiek(4, 'd')
        akord_a = akord.Akord(d_a, d_b, d_c, d_d, enum_wartosci_nut.WartosciNut.POLNUTA)
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 1)
        par.dodaj_akord(akord_a)
        self.assertEqual([(0, 0)], sprawdzarka.czy_w_partyturze_sa_dzwieki_obce(par))

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

    def test_czy_takty_maja_poprawne_dlugosci_1(self):
        par = partytura.Partytura(tonacja.Tonacja.F_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 2)
        d_a = dzwiek.Dzwiek(3, 'c')
        d_b = dzwiek.Dzwiek(4, 'e')
        d_c = dzwiek.Dzwiek(3, 'g')
        d_d = dzwiek.Dzwiek(4, 'c')
        akord_a = akord.Akord(d_a, d_b, d_c, d_d, enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.zakoncz_takt()
        par.zakoncz_takt()
        self.assertEqual([1], sprawdzarka.czy_takty_maja_odpowiednie_dlugosci(par))

    def test_czy_takty_maja_poprawne_dlugosci_2(self):
        par = partytura.Partytura(tonacja.Tonacja.F_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 2)
        d_a = dzwiek.Dzwiek(3, 'c')
        d_b = dzwiek.Dzwiek(4, 'e')
        d_c = dzwiek.Dzwiek(3, 'g')
        d_d = dzwiek.Dzwiek(4, 'c')
        akord_a = akord.Akord(d_a, d_b, d_c, d_d, enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.dodaj_akord(akord_a)
        par.zakoncz_takt()
        self.assertEqual([0], sprawdzarka.czy_takty_maja_odpowiednie_dlugosci(par))

    def test_czy_liczba_taktow_jest_poprawna(self):
        par = partytura.Partytura(tonacja.Tonacja.F_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 1)
        self.assertEqual(False, sprawdzarka.czy_liczba_taktow_jest_poprawna(par))

    def test_czy_liczba_taktow_jest_poprawna_1(self):
        par = partytura.Partytura(tonacja.Tonacja.F_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 1)
        par.zakoncz_takt()
        self.assertEqual(True, sprawdzarka.czy_liczba_taktow_jest_poprawna(par))

    def test_czy_wystepuja_skrzyzowania_glosow_1(self):
        par = partytura.Partytura(tonacja.Tonacja.F_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 2)
        d_s = dzwiek.Dzwiek(3, 'c')
        d_a = dzwiek.Dzwiek(4, 'e')
        d_t = dzwiek.Dzwiek(5, 'g')
        d_b = dzwiek.Dzwiek(4, 'c')
        akord_a = akord.Akord(d_s, d_a, d_t, d_b, enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        self.assertEqual([(0, 0)], sprawdzarka.czy_glosy_nie_sa_skrzyzowane(par))

    def test_czy_wystepuja_skrzyzowania_glosow_2(self):
        par = partytura.Partytura(tonacja.Tonacja.F_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 2)
        d_s = dzwiek.Dzwiek(3, 'c')
        d_a = dzwiek.Dzwiek(4, 'e')
        d_t = dzwiek.Dzwiek(5, 'g')
        d_b = dzwiek.Dzwiek(4, 'c')
        akord_a = akord.Akord(d_s, d_a, d_t, d_b, enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.zakoncz_takt()
        par.dodaj_akord(akord_a)
        self.assertEqual([(1, 0)], sprawdzarka.czy_glosy_nie_sa_skrzyzowane(par))

    def test_czy_wystepuja_skrzyzowania_glosow_3(self):
        par = partytura.Partytura(tonacja.Tonacja.F_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 2)
        d_s = dzwiek.Dzwiek(5, 'c')
        d_a = dzwiek.Dzwiek(4, 'e')
        d_t = dzwiek.Dzwiek(3, 'g')
        d_b = dzwiek.Dzwiek(2, 'c')
        akord_a = akord.Akord(d_s, d_a, d_t, d_b, enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        self.assertEqual([], sprawdzarka.czy_glosy_nie_sa_skrzyzowane(par))

    def test_czy_glosy_w_swoich_skalach(self):
        par = partytura.Partytura(tonacja.Tonacja.F_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 2)
        d_s = dzwiek.Dzwiek(4, 'c')
        d_a = dzwiek.Dzwiek(3, 'h')
        d_t = dzwiek.Dzwiek(3, 'h')
        d_b = dzwiek.Dzwiek(2, 'h')
        akord_a = akord.Akord(d_s, d_a, d_t, d_b, enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        self.assertEqual([], sprawdzarka.czy_glosy_w_swoich_skalach(par))

    def test_czy_glosy_w_swoich_skalach_2(self):
        par = partytura.Partytura(tonacja.Tonacja.F_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 2)
        d_s = dzwiek.Dzwiek(6, 'c')
        d_a = dzwiek.Dzwiek(3, 'h')
        d_t = dzwiek.Dzwiek(3, 'h')
        d_b = dzwiek.Dzwiek(2, 'h')
        akord_a = akord.Akord(d_s, d_a, d_t, d_b, enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        self.assertEqual([(0, 0, "sopran ")], sprawdzarka.czy_glosy_w_swoich_skalach(par))

    def test_czy_dzwieki_tworza_sensowne_funkcje_w_tonacji_1(self):
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 2)
        akord_a = akord.Akord(dzwiek.Dzwiek(4, "c"),
                              dzwiek.Dzwiek(4, "e"),
                              dzwiek.Dzwiek(4, "g"),
                              dzwiek.Dzwiek(4, "c"),
                              enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        akord_b = akord.Akord(dzwiek.Dzwiek(4, "c"),
                              dzwiek.Dzwiek(5, "d"),
                              dzwiek.Dzwiek(5, "f"),
                              dzwiek.Dzwiek(5, "g"),
                              enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_b)
        self.assertEqual([(0, 1)], sprawdzarka.czy_dzwieki_tworza_sensowne_funkcje_w_tonacji(par))

    def test_czy_dzwieki_tworza_sensowne_funkcje_w_tonacji_2(self):
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 2)
        akord_a = akord.Akord(dzwiek.Dzwiek(4, "c"),
                              dzwiek.Dzwiek(4, "e"),
                              dzwiek.Dzwiek(4, "g"),
                              dzwiek.Dzwiek(4, "c"),
                              enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        par.zakoncz_takt()
        akord_b = akord.Akord(dzwiek.Dzwiek(4, "c"),
                              dzwiek.Dzwiek(5, "d"),
                              dzwiek.Dzwiek(5, "f"),
                              dzwiek.Dzwiek(5, "g"),
                              enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_b)
        self.assertEqual([(1, 0)], sprawdzarka.czy_dzwieki_tworza_sensowne_funkcje_w_tonacji(par))

    def test_czy_odleglosci_glosow_nieprzekroczone_1(self):
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 2)
        akord_a = akord.Akord(dzwiek.Dzwiek(4, "c"),
                              dzwiek.Dzwiek(4, "e"),
                              dzwiek.Dzwiek(4, "g"),
                              dzwiek.Dzwiek(4, "c"),
                              enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_a)
        par.zakoncz_takt()
        akord_b = akord.Akord(dzwiek.Dzwiek(4, "c"),
                              dzwiek.Dzwiek(5, "d"),
                              dzwiek.Dzwiek(5, "f"),
                              dzwiek.Dzwiek(5, "g"),
                              enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akord_b)
        self.assertEqual([(2, 0, "SA(1, <Interwal.SEKUNDA_WIELKA: (3, \'2\')>)")],
                         sprawdzarka.czy_odleglosci_glosow_nie_sa_przekroczone(par))

    def test_czy_po_dominancie_nie_ma_subdominanty(self):
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 2)
        tonika = akord.Akord(dzwiek.Dzwiek(4, "c"),
                             dzwiek.Dzwiek(4, "e"),
                             dzwiek.Dzwiek(4, "g"),
                             dzwiek.Dzwiek(4, "c"),
                             enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        subdominanta = akord.Akord(dzwiek.Dzwiek(5, "f"),
                                   dzwiek.Dzwiek(5, "a"),
                                   dzwiek.Dzwiek(5, "c"),
                                   dzwiek.Dzwiek(5, "c"),
                                   enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        dominanta = akord.Akord(dzwiek.Dzwiek(1, "g"),
                                dzwiek.Dzwiek(1, "h"),
                                dzwiek.Dzwiek(1, "d"),
                                dzwiek.Dzwiek(1, "g"),
                                enum_wartosci_nut.WartosciNut.CWIERCNUTA)

        par.dodaj_akord(tonika)
        par.dodaj_akord(subdominanta)
        par.dodaj_akord(dominanta)
        par.zakoncz_takt()
        par.dodaj_akord(tonika)
        par.dodaj_akord(dominanta)
        par.dodaj_akord(tonika)
        par.zakoncz_takt()

        self.assertEqual([], sprawdzarka.czy_po_dominancie_nie_ma_subdominanty(par))

        par.dodaj_akord(dominanta)
        par.dodaj_akord(subdominanta)
        par.dodaj_akord(dominanta)
        par.zakoncz_takt()
        self.assertEqual([(2, 1)], sprawdzarka.czy_po_dominancie_nie_ma_subdominanty(par))

    def test_czy_na_raz_nie_ma_drugiego_przewrotu_1(self):
        bez = akord.Akord(dzwiek.Dzwiek(4, "c"),
                          dzwiek.Dzwiek(4, "e"),
                          dzwiek.Dzwiek(4, "g"),
                          dzwiek.Dzwiek(4, "c"),
                          enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        pierwszy = akord.Akord(dzwiek.Dzwiek(5, "a"),
                               dzwiek.Dzwiek(5, "f"),
                               dzwiek.Dzwiek(5, "c"),
                               dzwiek.Dzwiek(5, "f"),
                               enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        drugi = akord.Akord(dzwiek.Dzwiek(1, "g"),
                            dzwiek.Dzwiek(1, "h"),
                            dzwiek.Dzwiek(1, "g"),
                            dzwiek.Dzwiek(1, "d"),
                            enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 2)
        par.dodaj_akord(bez)
        par.dodaj_akord(pierwszy)

        par.zakoncz_takt()
        par.dodaj_akord(drugi)

        par.zakoncz_takt()
        par.dodaj_akord(pierwszy)
        par.dodaj_akord(bez)

        par.zakoncz_takt()
        self.assertEqual([1], sprawdzarka.czy_na_raz_nie_ma_drugiego_przewrotu(par))

    def test_czy_funkcja_nie_przetrzymana_przez_kreske_taktowa(self):
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 4)
        tonika = akord.Akord(dzwiek.Dzwiek(4, "c"),
                             dzwiek.Dzwiek(4, "e"),
                             dzwiek.Dzwiek(4, "g"),
                             dzwiek.Dzwiek(4, "c"),
                             enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        subdominanta = akord.Akord(dzwiek.Dzwiek(5, "f"),
                                   dzwiek.Dzwiek(5, "a"),
                                   dzwiek.Dzwiek(5, "c"),
                                   dzwiek.Dzwiek(5, "c"),
                                   enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        dominanta = akord.Akord(dzwiek.Dzwiek(1, "g"),
                                dzwiek.Dzwiek(1, "h"),
                                dzwiek.Dzwiek(1, "d"),
                                dzwiek.Dzwiek(1, "g"),
                                enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(tonika)
        par.dodaj_akord(subdominanta)
        par.dodaj_akord(dominanta)
        par.zakoncz_takt()
        par.dodaj_akord(dominanta)
        par.dodaj_akord(tonika)
        par.zakoncz_takt()
        par.dodaj_akord(tonika)
        par.zakoncz_takt()
        self.assertEqual([1, 2], sprawdzarka.czy_funkcja_nie_przetrzymana_przez_kreske_taktowa(par))

    def test_czy_ostateczne_rozwiazanie_nie_jest_w_drugim_przewrocie(self):
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 4)
        akd = akord.Akord(dzwiek.Dzwiek(4, "c"),
                          dzwiek.Dzwiek(4, "e"),
                          dzwiek.Dzwiek(4, "g"),
                          dzwiek.Dzwiek(4, "c"),
                          enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akd)
        par.zakoncz_takt()
        self.assertEqual(True, sprawdzarka.czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(par))

    def test_czy_ostateczne_rozwiazanie_nie_jest_w_drugim_przewrocie_2(self):
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 4)
        akd = akord.Akord(dzwiek.Dzwiek(4, "c"),
                          dzwiek.Dzwiek(4, "e"),
                          dzwiek.Dzwiek(4, "g"),
                          dzwiek.Dzwiek(4, "g"),
                          enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(akd)
        par.zakoncz_takt()
        self.assertEqual(False, sprawdzarka.czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(par))

    def test_czy_sa_kwinty_rownolegle(self):
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 4)
        tonika = akord.Akord(dzwiek.Dzwiek(4, "c"),
                             dzwiek.Dzwiek(4, "e"),
                             dzwiek.Dzwiek(4, "g"),
                             dzwiek.Dzwiek(4, "c"),
                             enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(tonika)
        par.dodaj_akord(tonika)
        par.zakoncz_takt()
        self.assertEqual([(0, 1, "ST,TB,")], sprawdzarka.czy_sa_kwinty_rownolegle(par))

    def test_czy_sa_oktawy_rownolegle(self):
        par = partytura.Partytura(tonacja.Tonacja.C_DUR, enum_metrum.Metrum.TRZY_CZWARTE, 4)
        tonika = akord.Akord(dzwiek.Dzwiek(4, "c"),
                             dzwiek.Dzwiek(4, "e"),
                             dzwiek.Dzwiek(4, "g"),
                             dzwiek.Dzwiek(5, "c"),
                             enum_wartosci_nut.WartosciNut.CWIERCNUTA)
        par.dodaj_akord(tonika)
        par.dodaj_akord(tonika)
        par.zakoncz_takt()
        self.assertEqual([(0, 1, "SB,")], sprawdzarka.czy_sa_oktawy_rownolegle(par))


if __name__ == '__main__':
    unittest.main()

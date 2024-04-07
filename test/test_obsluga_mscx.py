import unittest

import akord
import dzwiek
import enumerations.enum_metrum
import enumerations.enum_wartosci_nut
import obsluga_mscx
import obsluga_mscx as mscx
import partytura
import tonacja


class MyTestCase(unittest.TestCase):
    def test_poprawnosci_wczytanej_tonacji(self):
        p1 = mscx.wczytaj_z_pliku_mscx('../przyklady/mscx/partytura_0.mscx')
        self.assertEqual(tonacja.Tonacja.C_DUR, p1.podaj_tonacje())

    def test_poprawnosci_wczytanego_metrum(self):
        p1 = mscx.wczytaj_z_pliku_mscx('../przyklady/mscx/partytura_0.mscx')
        self.assertEqual(enumerations.enum_metrum.Metrum.CZTERY_CZWARTE, p1.podaj_metrum())

    def test_poprawnosci_wczytanej_liczby_taktow(self):
        p1 = mscx.wczytaj_z_pliku_mscx('../przyklady/mscx/partytura_0.mscx')
        self.assertEqual(4, p1.podaj_zadeklarowana_liczbe_taktow())

    def test_poprawnosci_wczytywania_akordow(self):
        p1 = partytura.Partytura(tonacja.Tonacja.C_DUR, enumerations.enum_metrum.Metrum.CZTERY_CZWARTE, 2)
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(5, "c"),
                                   dzwiek.Dzwiek(4, "e"),
                                   dzwiek.Dzwiek(3, "g"),
                                   dzwiek.Dzwiek(3, "c"),
                                   enumerations.enum_wartosci_nut.WartosciNut.POLNUTA))
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(5, "c"),
                                   dzwiek.Dzwiek(4, "a"),
                                   dzwiek.Dzwiek(3, "f"),
                                   dzwiek.Dzwiek(2, "f"),
                                   enumerations.enum_wartosci_nut.WartosciNut.CWIERCNUTA))
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(4, "h"),
                                   dzwiek.Dzwiek(4, "d"),
                                   dzwiek.Dzwiek(3, "g"),
                                   dzwiek.Dzwiek(2, "g"),
                                   enumerations.enum_wartosci_nut.WartosciNut.CWIERCNUTA))
        p1.zakoncz_takt()
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(5, "c"),
                                   dzwiek.Dzwiek(4, "e"),
                                   dzwiek.Dzwiek(3, "g"),
                                   dzwiek.Dzwiek(3, "c"),
                                   enumerations.enum_wartosci_nut.WartosciNut.CALA_NUTA))
        p2 = obsluga_mscx.wczytaj_z_pliku_mscx('../przyklady/mscx/partytura_a.mscx')
        self.assertEqual(p1, p2)

    def test_poprawnosci_wczytywania_akordow_2(self):
        p1 = partytura.Partytura(tonacja.Tonacja.A_DUR, enumerations.enum_metrum.Metrum.TRZY_CZWARTE, 3)
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(5, "c#"),
                                   dzwiek.Dzwiek(4, "e"),
                                   dzwiek.Dzwiek(3, "g#"),
                                   dzwiek.Dzwiek(3, "c#"),
                                   enumerations.enum_wartosci_nut.WartosciNut.POLNUTA))
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(5, "c#"),
                                   dzwiek.Dzwiek(4, "a"),
                                   dzwiek.Dzwiek(3, "f#"),
                                   dzwiek.Dzwiek(2, "f#"),
                                   enumerations.enum_wartosci_nut.WartosciNut.CWIERCNUTA))
        p1.zakoncz_takt()
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(4, "h"),
                                   dzwiek.Dzwiek(4, "d"),
                                   dzwiek.Dzwiek(3, "g#"),
                                   dzwiek.Dzwiek(2, "g#"),
                                   enumerations.enum_wartosci_nut.WartosciNut.CWIERCNUTA))
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(5, "c#"),
                                   dzwiek.Dzwiek(4, "e"),
                                   dzwiek.Dzwiek(3, "g#"),
                                   dzwiek.Dzwiek(3, "c#"),
                                   enumerations.enum_wartosci_nut.WartosciNut.POLNUTA))
        p1.zakoncz_takt()
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(5, "c#"),
                                   dzwiek.Dzwiek(4, "e"),
                                   dzwiek.Dzwiek(3, "g#"),
                                   dzwiek.Dzwiek(3, "c#"),
                                   enumerations.enum_wartosci_nut.WartosciNut.POLNUTA))
        p2 = obsluga_mscx.wczytaj_z_pliku_mscx('../przyklady/mscx/partytura_1.mscx')

    def test_poprawnosci_wczytywania_akordow_3(self):
        p1 = partytura.Partytura(tonacja.Tonacja.DES_DUR, enumerations.enum_metrum.Metrum.TRZY_CZWARTE, 3)
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(5, "c#"),
                                   dzwiek.Dzwiek(4, "e"),
                                   dzwiek.Dzwiek(3, "g#"),
                                   dzwiek.Dzwiek(3, "c"),
                                   enumerations.enum_wartosci_nut.WartosciNut.POLNUTA))
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(5, "db"),
                                   dzwiek.Dzwiek(4, "ab"),
                                   dzwiek.Dzwiek(3, "f"),
                                   dzwiek.Dzwiek(2, "f"),
                                   enumerations.enum_wartosci_nut.WartosciNut.CWIERCNUTA))
        p1.zakoncz_takt()
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(4, "h"),
                                   dzwiek.Dzwiek(4, "d"),
                                   dzwiek.Dzwiek(3, "g"),
                                   dzwiek.Dzwiek(2, "g"),
                                   enumerations.enum_wartosci_nut.WartosciNut.CWIERCNUTA))
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(5, "c"),
                                   dzwiek.Dzwiek(4, "e"),
                                   dzwiek.Dzwiek(3, "g"),
                                   dzwiek.Dzwiek(3, "c#"),
                                   enumerations.enum_wartosci_nut.WartosciNut.POLNUTA))
        p1.zakoncz_takt()
        p1.dodaj_akord(akord.Akord(dzwiek.Dzwiek(5, "c"),
                                   dzwiek.Dzwiek(4, "e"),
                                   dzwiek.Dzwiek(3, "g"),
                                   dzwiek.Dzwiek(3, "c#"),
                                   enumerations.enum_wartosci_nut.WartosciNut.POLNUTA))
        p2 = obsluga_mscx.wczytaj_z_pliku_mscx('../przyklady/mscx/partytura_3.mscx')
        self.assertEqual(p1, p2)

if __name__ == '__main__':
    unittest.main()

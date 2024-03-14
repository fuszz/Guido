import unittest
import obsluga_plikow
import sprawdzarka

# Trzeba dziubać

class TestySprawdzarki(unittest.TestCase):
    def test_badanie_objetosci_taktow_w_partyturze_1(self):
        nowa_partytura = obsluga_plikow.wczytaj_z_pliku("../przyklady/partytura_1.txt")
        self.assertEqual(sprawdzarka.badanie_objetosci_taktow_w_partyturze(nowa_partytura), [])

    def test_badanie_objetosci_taktow_w_partyturze_2(self):
        nowa_partytura = obsluga_plikow.wczytaj_z_pliku("../przyklady/partytura_2.txt")
        print(sprawdzarka.badanie_objetosci_taktow_w_partyturze(nowa_partytura))
        self.assertEqual(sprawdzarka.badanie_objetosci_taktow_w_partyturze(nowa_partytura), [])

    def test_badanie_objetosci_taktow_w_partyturze_3(self):
        nowa_partytura = obsluga_plikow.wczytaj_z_pliku("../przyklady/partytura_1.txt")
        self.assertEqual(sprawdzarka.badanie_objetosci_taktow_w_partyturze(nowa_partytura), [])

    def test_badanie_wystepowania_dzwiekow_obcych(self):
        nowa_partytura = obsluga_plikow.wczytaj_z_pliku("../przyklady/partytura_1.txt")
        self.assertEqual(sprawdzarka.badanie_wystepowania_dzwiekow_obcych(nowa_partytura), [])


if __name__ == '__main__':
    unittest.main()

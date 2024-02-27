import unittest
import obsluga_plikow
import sprawdzarka

class TestySprawdzarki(unittest.TestCase):
    def test_badanie_objetosci_taktow_w_partyturze_1(self):
        nowa_partytura = obsluga_plikow.odczytuj_plik("../przyklady/partytura_1.txt")
        self.assertEqual(sprawdzarka.badanie_objetosci_taktow_w_partyturze(nowa_partytura), [])  # add assertion here

    def test_badanie_wystepowania_dzwiekow_obcych(self):
        nowa_partytura = obsluga_plikow.odczytuj_plik("../przyklady/partytura_1.txt")
        self.assertEqual(sprawdzarka.badanie_wystepowania_dzwiekow_obcych(nowa_partytura), [])


if __name__ == '__main__':
    unittest.main()

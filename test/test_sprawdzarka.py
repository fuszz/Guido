import unittest
import obsluga_plikow
import sprawdzarka

class TestySprawdzarki(unittest.TestCase):
    def test_badanie_objetosci_taktow_w_partyturze(self):
        nowa_partytura = obsluga_plikow.odczytuj_plik("../przyklady/partytura_1.txt")
        self.assertEqual(sprawdzarka.badanie_objetosci_taktow_w_partyturze(nowa_partytura), [])  # add assertion here


if __name__ == '__main__':
    unittest.main()

import obsluga_plikow
import sprawdzarka
import dzwiek
#db = dzwiek.Dzwiek(3, 'c')
#dt = dzwiek.Dzwiek(3, 'g')
#da = dzwiek.Dzwiek(4, 'e')
#ds = dzwiek.Dzwiek(5, 'c')
#a_test = akord.Akord(ds, da, dt, db, 1.0)
#print(sprawdzarka.Sprawdzarka.czy_poprawne_dwojenia(a_test, tonacja.Tonacja('C')))


#nowa_partytura = obsluga_plikow.odczytuj_plik("przyklady/partytura_1.txt")

#nowy_dzwiek = dzwiek.Dzwiek(1, 'c')
#nowy_dzwiek.podaj_nazwe_dzwieku(

import akord
from enumerations import enum_wartosci_nut
d1 = dzwiek.Dzwiek(1, 'c')
a1 = akord.Akord(d1, d1, d1, d1, enum_wartosci_nut.WartosciNut(5))
print(a1.podaj_dlugosc())
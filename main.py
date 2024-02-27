import obsluga_plikow
import sprawdzarka

#db = dzwiek.Dzwiek(3, 'c')
#dt = dzwiek.Dzwiek(3, 'g')
#da = dzwiek.Dzwiek(4, 'e')
#ds = dzwiek.Dzwiek(5, 'c')
#a_test = akord.Akord(ds, da, dt, db, 1.0)
#print(sprawdzarka.Sprawdzarka.czy_poprawne_dwojenia(a_test, tonacja.Tonacja('C')))


nowa_partytura = obsluga_plikow.odczytuj_plik("partytura_1.txt")
print(sprawdzarka.Sprawdzarka.czy_takty_maja_poprawna_dlugosc(nowa_partytura))

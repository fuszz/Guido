import obsluga_plikow

moja_partytura = obsluga_plikow.ObslugaPLikow.odczytuj_plik("partytura_1.txt")
print(moja_partytura.podaj_liste_akordow())
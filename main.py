import obsluga_plikow
import partytura
import tonacja
import akord
import dzwiek
import sprawdzarka

db = dzwiek.Dzwiek(3, 'c')
dt = dzwiek.Dzwiek(3, 'g')
da = dzwiek.Dzwiek(4, 'e')
ds = dzwiek.Dzwiek(5, 'c')
a_test = akord.Akord(ds, da, dt, db, 1.0)
print(sprawdzarka.Sprawdzarka.czy_poprawne_dwojenia(a_test, tonacja.Tonacja('C')))
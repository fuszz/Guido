import obsluga_mscx
import tkinter as tk
import obsluga_txt
import sprawdzarka_warstwa_4 as spr
import partytura
import sprawdzarka_warstwa_1
import wyswietlanie_sprawdzarki_w_1
import wyswietlanie_sprawdzarki_w_2
import wyswietlanie_sprawdzarki_w_3
import wyswietlanie_sprawdzarki_w_4
SCIEZKA_DO_PLIKU_1 = "przyklady/mscx/Przyklad_2.2.mscx"

p = obsluga_mscx.wczytaj_z_pliku_mscx(SCIEZKA_DO_PLIKU_1)

print(wyswietlanie_sprawdzarki_w_1.sprawdz_warstwe_1(p))
print(wyswietlanie_sprawdzarki_w_2.sprawdz_warstwe_2(p))
print(wyswietlanie_sprawdzarki_w_3.sprawdz_warstwe_3(p))
print(wyswietlanie_sprawdzarki_w_4.sprawdz_warstwe_4(p))

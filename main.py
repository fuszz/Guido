import obsluga_mscx
import obsluga_txt
import sprawdzarka_warstwa_4 as spr
import partytura
import sprawdzarka_warstwa_1
import wyswietlanie_sprawdzarki_w_4

SCIEZKA_DO_PLIKU = ('przyklady/txt/partytura_6.txt')

p = obsluga_txt.wczytaj_z_pliku_txt(SCIEZKA_DO_PLIKU)

wyswietlanie_sprawdzarki_w_4.sprawdz_warstwe_4(p)

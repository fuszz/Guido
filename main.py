import obsluga_mscx
import obsluga_txt
import sprawdzarka_warstwa_4 as spr
import partytura
import sprawdzarka_warstwa_1
import sprawdzarka_warstwa_3

SCIEZKA_DO_PLIKU = ('przyklady/txt/partytura_6.txt')

p = obsluga_txt.wczytaj_z_pliku_txt(SCIEZKA_DO_PLIKU)

sprawdzarka_warstwa_3.sprawdz_warstwe_3(p)

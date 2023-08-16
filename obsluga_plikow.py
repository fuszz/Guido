import akord
import dzwiek
import partytura
import tonacja


class ObslugaPLikow:

    @staticmethod
    def odczytuj_plik(sciezka_do_pliku: str) -> partytura.Partytura:

        licznik: int = 0

        with open(sciezka_do_pliku, "r") as dane:
            for linia in dane:
                linia.replace(" ", "")
                # Nagłówek nowotworzonej partytury
                if linia:
                    # Kiedy licznik jest mniejszy od 3, zbieram parametry tworzonej partytury
                    if licznik < 3:
                        licznik += 1
                        parametr, wartosc = linia.split(":")

                        if parametr == "metrum":
                            nowe_metrum: str = wartosc.replace(" ", "")
                        elif parametr == "tonacja":
                            nazwa_tonacji: str = wartosc.replace(" ", "")
                        elif parametr == "takty":
                            nowa_liczba_taktow: int = int(wartosc)

                        if licznik == 3: #Tworzenie partytury
                            licznik += 1
                            nowa_tonacja = tonacja.Tonacja(nazwa_tonacji.strip())
                            nowa_partytura = partytura.Partytura(nowa_tonacja, nowe_metrum.strip(), nowa_liczba_taktow)

                    else:
                        linia = linia.strip()
                        if linia == "T":
                            nowa_partytura.zakoncz_takt()
                        else:

                            dzwieki = linia.split(",")
                            d_s, d_a, d_t, d_b, wartosc = dzwieki

                            d_s = d_s.strip()
                            d_a = d_a.strip()
                            d_t = d_t.strip()
                            d_b = d_b.strip()

                            wartosc = float(wartosc)
                            dzwiek_sopranu = dzwiek.Dzwiek(int(d_s[-1]), d_s[:-1])
                            dzwiek_altu = dzwiek.Dzwiek(int(d_a[-1]), d_a[:-1])
                            dzwiek_tenoru = dzwiek.Dzwiek(int(d_t[-1]), d_t[:-1])
                            dzwiek_basu = dzwiek.Dzwiek(int(d_b[-1]), d_b[:-1])
                            nowy_akord = akord.Akord(dzwiek_sopranu, dzwiek_altu, dzwiek_tenoru, dzwiek_basu, wartosc)
                            nowa_partytura.dodaj_akord(nowy_akord)
        return nowa_partytura

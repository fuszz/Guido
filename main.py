import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import obsluga_txt
import obsluga_mscx
import sprawdzanie
import os

WYBRANY_PLIK = ""
WYBRANY_TYP_PLIKU = ""

okno = tk.Tk()
okno.title("Guido v1.0")
okno.geometry('710x500')
okno.resizable(False, False)

font = ("Helvetica", 9)
okno.option_add("*Font", font)

wyniki = tk.Text(okno, height=31, width=59)

KOLORY_ANSI = ["\033[91m", "\033[92m", "\033[93m", "\033[0m"]


def wyswietl_wybrany_plik() -> None:
    global WYBRANY_PLIK
    podany_plik.config(state="normal")
    podany_plik.delete('1.0', 'end')
    podany_plik.insert(tk.END, WYBRANY_PLIK)
    podany_plik.config(state="disabled")


def wybierz_plik_txt() -> None:
    global WYBRANY_PLIK
    global WYBRANY_TYP_PLIKU
    sciezka_txt = filedialog.askopenfilename(filetypes=[('Text file', '*.txt')])
    WYBRANY_PLIK = sciezka_txt
    WYBRANY_TYP_PLIKU = "TXT"
    wyswietl_wybrany_plik()


def wyswietl_wynik(tekst) -> None:
    wyniki.tag_config("[91m", foreground="red")
    wyniki.tag_config("[92m", foreground="green")
    wyniki.tag_config("[93m", foreground="orange")
    wyniki.tag_config("[0m", foreground="black")
    wyniki.config(state="normal")
    wyniki.delete('1.0', 'end')

    for slowo in tekst.split("\033"):
        kolor = slowo.split("m")[0] + "m"
        wyniki.insert(tk.END, slowo[4:], kolor)
    wyniki.config(state="disabled")


def wybierz_plik_mscx() -> None:
    global WYBRANY_PLIK
    global WYBRANY_TYP_PLIKU
    sciezka_mscx = filedialog.askopenfilename(filetypes=[('Musescore uncompressed file', '*.mscx')])
    WYBRANY_PLIK = sciezka_mscx
    WYBRANY_TYP_PLIKU = "MSCX"
    wyswietl_wybrany_plik()


def wyswietl_popup(tekst: str) -> None:
    messagebox.showinfo("Guido v1.0", tekst)


def sprawdzaj_wybrany_plik() -> None:
    global WYBRANY_PLIK
    global WYBRANY_TYP_PLIKU

    if WYBRANY_PLIK == "":
        wyswietl_popup("Nie podano pliku")
        return
    elif not os.path.exists(WYBRANY_PLIK):
        wyswietl_popup("Podany plik nie istnieje.")
        return
    if WYBRANY_TYP_PLIKU == "TXT":
        try:
            badany_tekst = obsluga_txt.wczytaj_z_pliku_txt(WYBRANY_PLIK)
        except Exception as ext:
            wyswietl_popup(str(ext))
            return
    else:
        try:
            badany_tekst = obsluga_mscx.wczytaj_z_pliku_mscx(WYBRANY_PLIK)
        except Exception as ext:
            wyswietl_popup(str(ext))
            return
    wyswietl_wynik(sprawdzanie.sprawdzaj(badany_tekst))


podaj_plik_txt = tk.Button(okno, text="Plik .txt", command=wybierz_plik_txt, width=33, height=7)
podaj_plik_mscz = tk.Button(okno, text="Plik .mscx", command=wybierz_plik_mscx, width=33, height=7)

sprawdzaj = tk.Button(okno, text="Sprawdzaj", command=sprawdzaj_wybrany_plik,
                      width=33, height=7)

podany_plik = tk.Text(okno, height=2, width=33, wrap="word")
podany_plik.insert(tk.END, "Podaj plik:")
etykieta_pliku = tk.Label(okno, text="Podany plik:")

wyniki.insert(tk.END, "To jest przykładowy tekst w widgecie tekst.\nMa sprawdzić, czy widget działa poprawnie")

wyniki.place(x=10, y=10)
podaj_plik_txt.place(x=450, y=230)
podaj_plik_mscz.place(x=450, y=100)
sprawdzaj.place(x=450, y=360)
podany_plik.place(x=450, y=40)
etykieta_pliku.place(x=450, y=8)

try:
    okno.mainloop()
except Exception as e:
    wyswietl_popup(str(e))

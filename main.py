import tkinter as tk
from tkinter import filedialog

WYBRANY_PLIK = ""
WYBRANY_TYP_PLIKU = ""

okno = tk.Tk()
okno.title("Guido v1.0")
okno.geometry('710x500')
okno.resizable(False, False)

font = ("Helvetica", 9)
okno.option_add("*Font", font)

wyniki = tk.Text(okno, height=31, width=59)


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


def wybierz_plik_mscx() -> None:
    global WYBRANY_PLIK
    global WYBRANY_TYP_PLIKU
    sciezka_mscx = filedialog.askopenfilename(filetypes=[('Musescore uncompressed file', '*.mscx')])
    WYBRANY_PLIK = sciezka_mscx
    WYBRANY_TYP_PLIKU = "MSCX"
    wyswietl_wybrany_plik()


podaj_plik_txt = tk.Button(okno, text="Plik .txt", command=wybierz_plik_txt, width=33, height=7)
podaj_plik_mscz = tk.Button(okno, text="Plik .mscz", command=wybierz_plik_mscx, width=33, height=7)

sprawdzaj = tk.Button(okno, text="Sprawdzaj", command=lambda: wyniki.insert(tk.END, "Uruchomiono sprawdzanie\n"),
                      width=33, height=7)

podany_plik = tk.Text(okno, height=2, width=33)
podany_plik.insert(tk.END, "Podaj plik:")
etykieta_pliku = tk.Label(okno, text="Podany plik:")

wyniki.insert(tk.END, "To jest przykładowy tekst w widgecie tekst.\nMa sprawdzić, czy widget działa poprawnie")

wyniki.place(x=10, y=10)
podaj_plik_txt.place(x=450, y=230)
podaj_plik_mscz.place(x=450, y=100)
sprawdzaj.place(x=450, y=360)
podany_plik.place(x=450, y=40)
etykieta_pliku.place(x=450, y=8)

okno.mainloop()

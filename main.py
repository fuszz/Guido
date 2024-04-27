import tkinter as tk

import enumerations.enum_metrum
import tonacja
from partytura import Partytura
import wyniki_warstwa_1 as w1

okno = tk.Tk()
okno.title("Guido v1.0")
okno.geometry('710x500')
okno.resizable(False, False)

font = ("Helvetica", 9)
okno.option_add("*Font", font)

wyniki = tk.Text(okno, height=31, width=59, state="normal")
podaj_plik_txt = tk.Button(okno, text="Plik .txt", command=lambda: wyniki.insert(tk.END, "Podaj plik .txt\n"), width=33, height=7)
podaj_plik_mscz = tk.Button(okno, text="Plik .mscz", command=lambda: wyniki.insert(tk.END, "Podaj plik .mscz\n"), width=33, height=7)
sprawdzaj = tk.Button(okno, text="Sprawdzaj", command=lambda: wyniki.insert(tk.END, "Uruchomiono sprawdzanie\n"), width=33, height=7)
podany_plik = tk.Text(okno, height=2, width=33)
etykieta_pliku = tk.Label(okno, text="Podany plik:")
wyniki.insert(tk.END, "To jest przykładowy tekst w widgecie tekst.\nMa sprawdzić, czy widget działa poprawnie")

wyniki.place(x=10, y=10)
podaj_plik_txt.place(x=450, y=230)
podaj_plik_mscz.place(x=450, y=100)
sprawdzaj.place(x=450, y=360)
podany_plik.place(x=450, y=40)
etykieta_pliku.place(x=450, y=8)


okno.mainloop()

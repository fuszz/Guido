import tkinter as tk

def insert_formatted_text():
    # Wstawienie sformatowanego tekstu
    text.insert(tk.END, "Ala ma kota i psa, a pies ma Alę.", ("green", "red"))

# Tworzenie głównego okna
root = tk.Tk()
root.title("Wyświetlanie sformatowanego tekstu")

# Tworzenie widżetu tk.Text
text = tk.Text(root, height=10, width=40)
text.pack(pady=20)

# Definicja kolorów dla tagów
text.tag_config("green", foreground="green")
text.tag_config("red", foreground="red")

# Przycisk do wstawiania sformatowanego tekstu
insert_button = tk.Button(root, text="Wstaw sformatowany tekst", command=insert_formatted_text)
insert_button.pack()

root.mainloop()

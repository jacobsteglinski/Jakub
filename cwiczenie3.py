class Samochod:
    def __init__(self, marka, model, liczba_drzwi, rok_produkcji):
        self.marka = marka
        self.model = model
        self.liczba_drzwi = liczba_drzwi
        self.rok_produkcji = rok_produkcji

    def wypisz_dane(self):
        print("Marka:", self.marka)
        print("Model:", self.model)
        print("Liczba drzwi:", self.liczba_drzwi)
        print("Rok produkcji:", self.rok_produkcji)


class Maluch(Samochod):
    marka = "Samochodex"
    model = "maly"
    liczba_drzwi = 3

    def __init__(self, rok_produkcji):
        self.rok_produkcji = rok_produkcji


# Test klasy Samochod
auto = Samochod("Autopol", "rodzinny", 5, 2010)
print("--- Samochod ---")
auto.wypisz_dane()

# Test klasy Maluch
maluch = Maluch(1978)
print("\n--- Maluch ---")
maluch.wypisz_dane()

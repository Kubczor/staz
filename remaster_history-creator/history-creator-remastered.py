import random
import csv


def wczytaj_slowa_z_csv(plik_csv):
    with open(plik_csv, newline='') as csvfile:
        slowa = [row[0] for row in csv.reader(csvfile)]
    return slowa

def generuj_historyjke(slowo_klucz, przymiotniki, czasowniki, rzeczowniki, przyimki, dlugosc=150):
    historia = ""
    ilosc_slow = 0

    # Zainicjowanie flagi informującej, czy słowo kluczowe zostało już użyte
    slowo_klucz_uzyte = False

    while ilosc_slow < dlugosc:
        # Wybór losowego słowa z każdej kategorii
        slowa_kategorii = {
            'przymiotniki': random.choice(przymiotniki),
            'przyslowki': random.choice(przyslowki),
            'czasowniki': random.choice(czasowniki),
            'dopelniacze': random.choice(dopelniacze),
            'rzeczowniki': random.choice(rzeczowniki),
            'przyimki': random.choice(przyimki),
            'slowo_klucz': slowo_klucz if not slowo_klucz_uzyte else random.choice(przymiotniki)
        }

        # Utworzenie fragmentu historyjki
        fragment = f"{slowa_kategorii['przymiotniki']} {slowa_kategorii['czasowniki']} {slowa_kategorii['rzeczowniki']} {slowa_kategorii['dopelniacze']} {slowa_kategorii['przyslowki']} {slowa_kategorii['przyimki']} {slowa_kategorii['slowo_klucz']}."

        # Sprawdzenie, czy dodanie fragmentu nie przekroczy długości 150 słów
        if ilosc_slow + len(fragment.split()) <= dlugosc:
            historia += fragment + " "
            ilosc_slow += len(fragment.split())
            # Oznaczenie słowa kluczowego jako użyte
            if slowa_kategorii['slowo_klucz'] == slowo_klucz:
                slowo_klucz_uzyte = True
        else:
            break

    return historia.strip()

# Wczytanie słów z plików CSV
przymiotniki = wczytaj_slowa_z_csv('adjectives.csv')
czasowniki = wczytaj_slowa_z_csv('verbs.csv')
rzeczowniki = wczytaj_slowa_z_csv('nouns.csv')
przyimki = wczytaj_slowa_z_csv('prepositions.csv')
przyslowki = wczytaj_slowa_z_csv('adverb.csv')
dopelniacze = wczytaj_slowa_z_csv('genitive.csv')

# Pobranie słowa kluczowego od użytkownika
slowo_klucz = input("Wprowadź słowo kluczowe: ")

# Generowanie historyjki na podstawie słowa kluczowego
historyjka = generuj_historyjke(slowo_klucz, przymiotniki, czasowniki, rzeczowniki, przyimki, dlugosc=150)

# Wyświetlenie wygenerowanej historyjki
# print("\nWygenerowana historyjka:")
# print(historyjka)

import os
from google.cloud import translate_v2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"history-creator_key.json"

translate_client = translate_v2.Client()

text = historyjka
target = "pl"

translation = translate_client.translate(text, target_language=target)

translated_text = translation['translatedText']
print(f"{translated_text}")

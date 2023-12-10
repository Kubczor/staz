import random
import csv


def wczytaj_slowa_z_csv(plik_csv):
    with open(plik_csv, newline='') as csvfile:
        slowa = [row[0] for row in csv.reader(csvfile)]
    return slowa


import random

import random

def generuj_historyjke(slowo_klucz, przymiotniki, przyslowki, czasowniki, dopelniacze, rzeczowniki, przyimki, dlugosc=150, max_rekurencja=10):
    historia = ""
    ilosc_slow = 0

    # Zainicjowanie flagi informującej, czy słowo kluczowe zostało już użyte
    slowo_klucz_uzyte = False
    rekurencja = 0

    while ilosc_slow < dlugosc:
        # Wybór losowej kolejności części zdania
        kolejnosc_czesci_zdania = ['przymiotniki', 'przyslowki', 'czasowniki', 'dopelniacze', 'rzeczowniki', 'przyimki']
        random.shuffle(kolejnosc_czesci_zdania)

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

        # Utworzenie fragmentu historyjki w losowej kolejności
        fragment = " ".join([f"{slowa_kategorii[kategoria]}" for kategoria in kolejnosc_czesci_zdania])

        # Sprawdzenie, czy dodanie fragmentu nie przekroczy długości 150 słów
        if ilosc_slow + len(fragment.split()) <= dlugosc:
            historia += fragment + " "
            ilosc_slow += len(fragment.split())
            # Oznaczenie słowa kluczowego jako użyte
            if slowa_kategorii['slowo_klucz'] == slowo_klucz:
                slowo_klucz_uzyte = True
        else:
            break

        # Sprawdzenie, czy słowo kluczowe jest w historii
        if slowo_klucz in historia:
            break

        rekurencja += 1
        if rekurencja >= max_rekurencja:
            break

    # Dodanie kropki na końcu całej historii
    historia = historia.strip() + "."

    return historia.strip()

# Przykład użycia
slowo_klucz = "dom"
przymiotniki = ["piękny", "duży", "czerwony"]
przyslowki = ["szybko", "ostro", "śmiało"]
czasowniki = ["biegnie", "skacze", "pływa"]
dopelniacze = ["najpiękniejszy", "największy", "najnowszy"]
rzeczowniki = ["kot", "samochód", "kwiat"]
przyimki = ["przy", "na", "pod"]

historyjka = generuj_historyjke(slowo_klucz, przymiotniki, przyslowki, czasowniki, dopelniacze, rzeczowniki, przyimki, dlugosc=150, max_rekurencja=10)
print(historyjka)


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
historyjka = generuj_historyjke(slowo_klucz, przymiotniki, przyslowki, czasowniki, dopelniacze, rzeczowniki, przyimki, dlugosc=150)

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

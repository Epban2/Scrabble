# RICCARDO LA ROCCA 4C INF
# Gioco Scrabble
import random


# Ritorna una lista di 8 lettere casuali
def estrai_lettere():
    sacchetto = []
    i = 0
    while i < 8:
        lettera = random.choice(list(lettere.keys()))  # prendo la chiave casuale
        if lettere[lettera]["quantità"] > 0:  # solamente se il valore non è 0
            sacchetto.append(lettera)
            lettere[lettera]["quantità"] -= 1  # rimuovo 1 alla quantita'
            i += 1
        else:
            i -= 1
    return sacchetto


# ritorna il punteggio della parola
def calcola_punteggio(parola):
    punteggio = 0
    for lettera in parola:
        punteggio += lettere[lettera]["punteggio"]
    return punteggio


# main
lettere = {
    'a': {'quantità': 14, 'punteggio': 1},
    'b': {'quantità': 3, 'punteggio': 5},
    'c': {'quantità': 6, 'punteggio': 2},
    'd': {'quantità': 3, 'punteggio': 5},
    'e': {'quantità': 11, 'punteggio': 1},
    'f': {'quantità': 3, 'punteggio': 5},
    'g': {'quantità': 2, 'punteggio': 8},
    'h': {'quantità': 2, 'punteggio': 8},
    'i': {'quantità': 12, 'punteggio': 1},
    'l': {'quantità': 5, 'punteggio': 3},
    'm': {'quantità': 5, 'punteggio': 3},
    'n': {'quantità': 5, 'punteggio': 3},
    'o': {'quantità': 5, 'punteggio': 1},
    'p': {'quantità': 3, 'punteggio': 5},
    'q': {'quantità': 1, 'punteggio': 10},
    'r': {'quantità': 6, 'punteggio': 2},
    's': {'quantità': 6, 'punteggio': 2},
    't': {'quantità': 6, 'punteggio': 2},
    'u': {'quantità': 5, 'punteggio': 3},
    'v': {'quantità': 3, 'punteggio': 5},
    'z': {'quantità': 2, 'punteggio': 8}
}

sacchetto = estrai_lettere()

sacchettoStr = ', '.join(sacchetto)  # stringhe con le lettere randomiche per stampare
print(f"Le tue lettere sono: {sacchettoStr.upper()}")
sacchettoStr = ''.join(sacchetto)  # tolte le virgole per controllare dopo
parola = input("Inserire parola dal sacchetto: ").lower()  # input maiuscolo

i = 0
myfile = open("file.txt", "r")
with myfile as file:
    for riga in myfile:
        if parola.strip() == riga.strip():
            punteggio = calcola_punteggio(parola)
            print(f'Punteggio parola "{parola}"= {punteggio}')
            i = 1
if i == 0:
    print("La tua parola non esiste")

# RICCARDO LA ROCCA 4C INF
# Gioco Scrabble
import random

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


# Ritorna una lista di 8 lettere casuali
def estrai_lettere():
    sacchetto = []
    i = 0
    for i in range(8):
        lettera = random.choice(list(lettere.keys()))  # prendo la chiave casuale
        if lettere[lettera]["quantità"] > 0:  # solamente se il valore non è 0
            sacchetto.append(lettera)
            lettere[lettera]["quantità"] -= 1  # tolgo una lettera dalla quantita'
        else:
            i -= 1
    return sacchetto


# controlla che la parola contenga solo caratteri presenti nel sacchetto
def controllaValida(parola):
    parolaValida = True  # per i controlli

    for char in parola:
        if char not in sacchetto and parolaValida:  # lettera non nel sacchetto
            parolaValida = False  # flag impostato su false
        elif char in sacchetto:
            sacchetto.remove(char)  # sacchetto = ['a','b']. parola= aab --> ritorna false (non valido)
    return parolaValida  # boolean


# controlla se la parola è presente nel dizionario
def controllaInDizionario(parola):
    f = open("file.txt", "r")
    inDizionario = False
    with f as file:  # chiude automaticamente il file
        for riga in f:
            if parola.strip() == riga.strip():  # strip() toglie spazi a inizio e fine della stringa
                inDizionario = True
    return inDizionario


# ritorna il punteggio della parola
def calcola_punteggio(parola):
    punteggio = 0
    for lettera in parola:
        punteggio += lettere[lettera]["punteggio"]
    return punteggio


# main
totale = 0

lenLista = 0
for valore in lettere.values():  # values() ritorna il risultato della chiave "quantita"
    lenLista += valore['quantità']

while lenLista > 0:
    sacchetto = estrai_lettere()

    sacchettoStr = ', '.join(sacchetto).upper()  # stringhe con le lettere random
    print(f"Le tue lettere sono: {sacchettoStr}")
    parola = input("Inserire parola dal sacchetto: ").lower()  # input minuscolo

    if controllaValida(parola):
        if controllaInDizionario(parola):
            punti = calcola_punteggio(parola)
            totale += punti
            print(f"Il punteggio per: '{parola}' = {punti}")
        else:
            print("La parola non e' nel dizionario")
    else:
        print("La parola contiene caratteri non validi!")

    for valore in lettere.values():
        lenLista += valore['quantità']
    print("\n")

print(f"Punteggio totalizzato: {totale}")

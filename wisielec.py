
from hangman_body import HANGMAN_BODY
from slowwa import *
import random
import string

def losuj():
    ''' Funkcja losuje jedno słowo spośród listy dostępnych słów i zwraca to słowo '''
    slowo = random.choice(words) # zmienna lokalna
    return slowo


# def litera_zgadnij(slowo, myslniki):
#     litera = input('Podaj literę:')
#     if litera in slowo:
#        for indeks, literka in enumerate(slowo):
#         if litera == literka:
#             print(indeks)
#             myslniki[indeks].replace('_', litera)
#             print(myslniki)


def wyswietlanie_wisielca(liczba_wisielca):
    print(HANGMAN_BODY[liczba_wisielca])
    print(liczba_wisielca)

def litera_zgadnij(slowo, myslniki_lista, litera):
    result = False
    if litera in slowo:
        for indeks, literka in enumerate(slowo):
            if litera == literka:
                myslniki_lista[indeks] = litera
                result = True
                print(result)
    return result
    


def main():
    alfabet = string.ascii_uppercase
    print(alfabet)
    print(HANGMAN_BODY[0])
    slowo = losuj()
    liczba_myslnikow = len(slowo)
    print('Słowo:')
    myslniki = '_' * liczba_myslnikow
    myslniki_lista = list(myslniki)
    print(''.join(myslniki_lista))
    liczba_wisielca = 0
    dlugos_hangman_body = len(HANGMAN_BODY)
    przegrana = False
    while '_' in myslniki_lista:
        print(alfabet)
        litera = input('Podaj literę: ')
        if litera.upper() not in alfabet:
            print('Litera została już użyta')
        else:
            alfabet = alfabet.replace(litera, ' ')
            if litera_zgadnij(slowo, myslniki_lista, litera) == False:
                liczba_wisielca += 1

            print(''.join(myslniki_lista))
            wyswietlanie_wisielca(liczba_wisielca)

        if dlugos_hangman_body - 1 == liczba_wisielca:
            przegrana = True
            break 
    
    if przegrana:
        print('GAME OVER. Przegrałeś')
    else:
        print('GAME OVER. Wygrałeś')
    
        
 
    

main()
# -*- coding: utf-8 -*-


#       main z moja sciezka, chcesz swoj? ZRÓB SE!

import os

os.chdir(r"C:\Users\grzon\Documents\Python\Wizuala\Wizu")

import pobieranko, przetwarzanko, wizualizowanko, chmurkowanko2

def od_zera_do_bohatera_nie_rob_plox():
    pobieranko.pobierz_od_zera()
    przetwarzanko.sumuj_lata("Dane")
    przetwarzanko.analizka_lat("Dane")
    return
def srednia_wszystkich():
    wejscie = wczytywanko("Lata\\wszyscy.txt")
    lata = [int(i) for i in wejscie.keys() if ( int(i) > 1960 and int(i) < 2020 )]
    ilosc_utworow = [int(wejscie[str(i)]) for i in lata]
	all_srednia = sum(ilosc_utworow)/(len(lata)*20)
    return all_srednia

def wykresy_po_latach():
    plik = open( "katalog_linkow.txt" ,'r')
    artysci = [ x[ 0 : -1 ] for x in plik.readlines() ]
    artysci.append("wszyscy")
    plik.close()

    for art in artysci:
        wizualizowanko.wykresuj_lata(przetwarzanko.wczytywanko("Lata\\"+art+".txt"), art)
        wizualizowanko.wykresuj_lata_ograniczone(przetwarzanko.wczytywanko("Lata\\"+art+".txt"), art, srednia_wszystkich)
    return



def chmury_dla_wszystkich_nie_rob_plox():
    chmurkowanko2.chmury_4_all("Dane")
    return

przetwarzanko.czytaj_10(przetwarzanko.wczytywanko("Dane.txt"))
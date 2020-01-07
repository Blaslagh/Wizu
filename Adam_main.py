# -*- coding: utf-8 -*-


#       main z moja sciezka, chcesz swoj? ZRÓB SE!

import os

os.chdir("C:\\Users\\Adam\\Source\\Repos\\Blaslagh\\Wizu")

import pobieranko, przetwarzanko, wizualizowanko, chmurkowanko2

def od_zera_do_bohatera_nie_rob_plox():
    pobieranko.pobierz_od_zera()
    przetwarzanko.sumuj_lata("Dane")
    przetwarzanko.analizka_lat("Dane")
    return

def wykresy_po_latach():
    plik = open( "katalog_linkow.txt" ,'r')
    artysci = [ x[ 0 : -1 ] for x in plik.readlines() ]
    artysci.append("wszyscy")
    plik.close()

    for art in artysci:
        wizualizowanko.wykresuj_lata(przetwarzanko.wczytywanko("Lata\\"+art+".txt"), art)
        wizualizowanko.wykresuj_lata_ograniczone(przetwarzanko.wczytywanko("Lata\\"+art+".txt"), art)
    return

def chmury_dla_wszystkich_nie_rob_plox():
    chmurkowanko2.chmury_4_all("Dane","Chmury3", 3)
    chmurkowanko2.chmury_4_all("Dane","Chmury4", 4)
    return

chmury_dla_wszystkich_nie_rob_plox()



przetwarzanko.czytaj_x(przetwarzanko.wczytywanko("Dane.txt"), 10)

przetwarzanko.skomplikowalnosc(przetwarzanko.wczytywanko("Dane\\lady_pank\\2.txt"))
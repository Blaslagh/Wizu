# -*- coding: utf-8 -*-


#       main z moja sciezka, chcesz swoj? ZRÓB SE!

import os

os.chdir("C:\\Users\\Adam\\Source\\Repos\\Blaslagh\\Wizu")

import pobieranko, przetwarzanko, wizualizowanko


####pobieranko.pobierz_od_zera()

###przetwarzanko.sumuj_lata("Dane")

###przetwarzanko.analizka_lat("Dane")



plik = open( "katalog_linkow.txt" ,'r')
artysci = [ x[ 0 : -1 ] for x in plik.readlines() ]
artysci.append("wszyscy")
plik.close()

for art in artysci:
    wizualizowanko.wykresuj_lata(przetwarzanko.wczytywanko("Lata\\"+art+".txt"), art)
    wizualizowanko.wykresuj_lata_ograniczone(przetwarzanko.wczytywanko("Lata\\"+art+".txt"), art)
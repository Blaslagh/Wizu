# -*- coding: utf-8 -*-


#       main z moja sciezka, chcesz swoj? ZRÓB SE!

import os

os.chdir("C:\\Users\\Adam\\Source\\Repos\\Blaslagh\\Wizu")

import pobieranko, przetwarzanko, wizualizowanko, chmurkowanko

def od_zera_do_bohatera_nie_rob_plox():
	pobieranko.pobierz_od_zera()
	przetwarzanko.sumuj_lata("Dane")
	przetwarzanko.analizka_lat("Dane")
	return

def srednia_wszystkich():
	wejscie = przetwarzanko.wczytywanko("Lata\\wszyscy.txt")
	lata = [int(i) for i in wejscie.keys() if ( int(i) > 1960 and int(i) < 2020 )]
	ilosc_utworow = [int(wejscie[str(i)]) for i in lata]
	all_srednia = sum(ilosc_utworow)/(len(lata)*19)
	return all_srednia

def wykresy_po_latach():

	plik = open( "katalog_linkow.txt" ,'r')
	artysci = [ x[ 0 : -1 ] for x in plik.readlines() ]
	artysci.append("wszyscy")
	plik.close()

	for art in artysci:
		wizualizowanko.wykresuj_lata(przetwarzanko.wczytywanko("Lata\\"+art+".txt"), art)
		wizualizowanko.wykresuj_lata_ograniczone(przetwarzanko.wczytywanko("Lata\\"+art+".txt"), art, srednia_wszystkich())
	return

def chmury_dla_wszystkich_nie_rob_plox():
	chmurkowanko.chmury_4_all("Dane","Chmury3", 3)
	chmurkowanko.chmury_4_all("Dane","Chmury4", 4)
	return


przetwarzanko.czytanko_dla_art()
przetwarzanko.zapisz_czytanie()


wizualizowanko.wykresuj_skomplikowanie_srednia("Dane")
wizualizowanko.wykresuj_skomplikowanie_suma("Dane")
wizualizowanko.wykresuj_skomplikowanie_po_latach("Dane")


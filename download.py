#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, os


#Tworzymy katalog linków do piosenek

plik = open("katalog_linkow.txt","r")
try:
	z_pliku = plik.read()
finally:
	plik.close()

def pobierz_linki( katalog_atrystow = z_pliku.split() ):
    try:
        tab_link=[]
        for artysta in katalog_atrystow:
            try:
                for nr in range( 1, 20 ):
                    strona_artysty = "https://www.tekstowo.pl/piosenki_artysty," + str( artysta ) + ",alfabetycznie,strona," + str( nr ) + ".html"
                    for i in requests.get( strona_artysty ).text.split( '"' ):
                        if ('piosenka,' + str( artysta ) + ',' in i ): 
                            if i[0] == '/':
                                if "https://www.tekstowo.pl" + i in tab_link:
                                    continue
                                tab_link.append( [ artysta, "https://www.tekstowo.pl" + i] )
                            else:
                                if "https://www.tekstowo.pl/" + i in tab_link:
                                    continue
                                tab_link.append( [ artysta, "https://www.tekstowo.pl/" + i] )
                print( "Linki do " + artysta + " zostały pobrane" )
            except:
                print( "Błąd pobierania linków ", artysta )
        return( tab_link )
    except:
        print( "Tragiczny błąd pobierania linków")
    return

def pobierz_tekst(artysta, link):
    try:
        temp=requests.get(link)
        temp.encoding="utf-8"
        rok="NW"
        for i in temp.text.split("</div>"):
            if ('Rok powstania:' in i):
                for j in i.split("</tr>"):
                    if ('Rok powstania:' in j):
                        try:
                            rok=''.join(k for k in j if k.isdigit())[0:4]
                        except:
                            print("Brak roku")
                        break
                break
            if ( 'class="song-text"' in i ): 
                wlasciwy_kontener = i
        print( '.', end = '' )
        return artysta, rok, wlasciwy_kontener.replace("<br />","").replace(")","").replace("(","").replace("?","").replace(",","").replace(".","").replace("!","").lower().split()[4:-15]
    except:
        print( "#", end = '' )
    return

def zlicz_slowa(tekst,lista_slow):
    for slowo in tekst:
        if len( slowo ) < 3:
            continue
        if slowo in lista_slow:
            lista_slow[slowo] += 1
        else:
            lista_slow[slowo] = 1
    return lista_slow

def pobierz_od_zera(a=0,b=-1):
    for tekst in [ pobierz_tekst( link[0], link[1] ) for link in pobierz_linki()[a:b] ]:
        try:
            if not os.path.exists("Dane\\"+str(tekst[0])+"\\"+str(tekst[1])):
                os.makedirs("Dane\\"+str(tekst[0])+"\\"+str(tekst[1]))
            plik = open("Dane\\"+str(tekst[0])+"\\"+str(tekst[1])+"\\"+tekst[2][0]+".txt","w")
            try:
                plik.writelines([ slowo + ' ' for slowo in tekst[2]])
                print( "s", end = '' ) 
            except:
                print( "F", end = '' )
            finally:
                plik.close()
        except:
            print(tekst)
    return


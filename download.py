#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, os


#Tworzymy katalog linków do piosenek

plik = open("C:\\Users\\Adam\\Source\\Repos\\Blaslagh\\Wizu\\katalog_linkow.txt","r")
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
            if ('class="song-text"' in i): 
                wlasciwy_kontener=i
        print('.',end='')
        return artysta, rok, wlasciwy_kontener.replace("<br />","").replace(")","").replace("(","").replace("?","").replace(",","").replace(".","").replace("!","").lower().split()[4:-15]
    except:
        print("\nBłąd pobierania tekstu " + link)
    return

def zlicz_slowa(tekst,lista_slow):
    for slowo in tekst:
        if len(slowo)<3:
            continue
        if slowo in lista_slow:
            lista_slow[slowo] += 1
        else:
            lista_slow[slowo] = 1
    return lista_slow



lista_tekstow = [ pobierz_tekst( i[0], i[1] ) for i in pobierz_linki()[0:100] ]


zbior_slow = {}
i=0
for tekst in lista_tekstow:
    try:
        newpath = "C:\\Users\\Adam\\Source\\Repos\\Blaslagh\\Wizu\\Dane\\"+str(tekst[0])+"\\"+str(tekst[1])
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        plik = open("C:\\Users\\Adam\\Source\\Repos\\Blaslagh\\Wizu\\Dane\\"+str(tekst[0])+"\\"+str(tekst[1])+"\\"+str(i)+".txt","w")
        try:
            plik.write([ slowo + ' ' for slowo in tekst[2]])
        except:
            print("Problem z zapisaniem")
        finally:
            plik.close()

        i+=1
        zbior_slow = zlicz_slowa( tekst[2], zbior_slow )
    except:
        print(tekst)
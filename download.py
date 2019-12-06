#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


#Tworzymy katalog linków do piosenek

plik = open("C:\\Users\\Adam\\Source\\Repos\\Blaslagh\\Wizu\\katalog_linkow.txt","r")
try:
	z_pliku = plik.read()
finally:
	plik.close()


def pobierz_linki(katalog_atrystow=z_pliku.split()):
    try:
        tab_link=[]
        for artysta in katalog_atrystow:
            for nr in range(1,20):
                strona_artysty="https://www.tekstowo.pl/piosenki_artysty,"+str(artysta)+",alfabetycznie,strona,"+str(nr)+".html"
                for i in requests.get(strona_artysty).text.split('"'):
                    if ('piosenka,'+str(artysta)+',' in i): 
                        if i[0]=='/':
                            if "https://www.tekstowo.pl"+i in tab_link:
                                continue
                            tab_link.append("https://www.tekstowo.pl"+i)
                        else:
                            if "https://www.tekstowo.pl/"+i in tab_link:
                                continue
                            tab_link.append("https://www.tekstowo.pl/"+i)
        return(tab_link)
    except:
        print("B³¹d pobierania linków")
    return

def pobierz_tekst(link):
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
        return (rok, wlasciwy_kontener.replace("<br />","").replace(")","").replace("(","").replace("?","").replace(",","").replace(".","").replace("!","").lower().split()[4:-15])
    except:
        print("B³¹d pobierania tekstu "+link)
    return

tab_link=pobierz_linki()

for i in tab_link[0:100]:
    pobierz_tekst(i)
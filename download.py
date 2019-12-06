#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


lista_slow={}

#Tworzymy katalog linków do piosenek

def pobierz_linki(katalog_atrystow):
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
    except:
        print("B³¹d pobierania linków")


#Ka¿dy tekst z piosenek pobieramy i przetwarzamy

for link in tab_link:
    temp=requests.get(link)
    temp.encoding="utf-8"
    for i in temp.text.split("</div>"):
        if ('class="song-text"' in i): 
            wlasciwy_kontener=i
            break

    tekst=wlasciwy_kontener.replace("<br />","").replace(")","").replace("(","").replace("?","").replace(",","").replace(".","").replace("!","").lower().split()[4:-15]
    for slowo in tekst:
        if slowo in lista:
            lista[slowo] += wlasciwy_kontener.count(slowo)
        else:
            lista[slowo] = wlasciwy_kontener.count(slowo)


#Zamieniamy nasz¹ listê na tablicê

tablicka=[]
for i in range(max(lista.values())):
    for j in lista:
        if lista[j]==i:
            tablicka.append([j,i])
print(tablicka[-20:-1])       
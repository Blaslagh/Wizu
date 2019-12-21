# -*- coding: utf-8 -*-

import requests, os



def pobierz_linki():
    tab_link=[]
    try:
        plik = open("pobrane_linki.txt","r")
        try:
            tab_link = [ i.split() for i in plik.read().split('\n') ]
            print("Wczytano plik linków")
        except:
            print("Błąd wczytania")
        finally:       
            plik.close()

    except:
        plik = open("katalog_linkow.txt","r")
        try:
        	z_pliku = plik.read()
        finally:
        	plik.close()
        tab_link=[]
        katalog_atrystow = z_pliku.split()
        
        for artysta in katalog_atrystow:
            try:
                for nr in range( 1, 20 ):
                    strona_artysty = "https://www.tekstowo.pl/piosenki_artysty," + str( artysta ) + ",alfabetycznie,strona," + str( nr ) + ".html"
                    for i in requests.get( strona_artysty ).text.split( '"' ):
                        if ('piosenka,' + str( artysta ) + ',' in i ): 
                            if i[0] == '/':
                                if "https://www.tekstowo.pl" + i in [tab_link[x][1] for x in range(len(tab_link)-1)]:
                                    continue
                                tab_link.append( [ artysta, "https://www.tekstowo.pl" + i] )
                            else:
                                if "https://www.tekstowo.pl/" + i in [tab_link[x][1] for x in range(len(tab_link)-1)]:
                                    continue
                                tab_link.append( [ artysta, "https://www.tekstowo.pl/" + i] )
                print( "Linki do " + artysta + " zostały pobrane" )
            except:
                print( "Błąd pobierania linków ", artysta )
                
        plik = open("pobrane_linki.txt","w")
        try:
        	z_pliku = plik.writelines( [ i[0] + ' ' + i[1] + '\n' for i in tab_link ] )
        finally:
        	plik.close()
    return( tab_link )

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
                            rok=''.join(k for k in j if k.isdigit())[-4:]
                            if len(rok)<4:
                                rok="NW"
                        except:
                            print("Brak roku")
                        break
                break
            if ( 'class="song-text"' in i ): 
                wlasciwy_kontener = i
        print( '.', end = '' )
        return artysta, rok, wlasciwy_kontener.replace("<br />","").replace(':',"").replace('`',"").replace('\'',"").replace(';',"").replace('"',"").replace("-","").replace(")","").replace("*","").replace("(","").replace("?","").replace(",","").replace(".","").replace("!","").replace('[',"").replace(']',"").lower().split()[4:-15]
    except:
        print( "\n#", end = '' )
    return

def pobierz_od_zera(a=0,b=-1,podfolder="Dane"):
    if not input(os.getcwd()+"\\"+podfolder+"\n\nJesteś pewien że podany katalog jest właściwy? T/N\n").lower().startswith("t"):
        return
    for link in pobierz_linki()[a:b]:
        tekst = pobierz_tekst( link[0], link[1] )
        if (tekst == None or tekst == "None" or tekst[2] == None or tekst[2] == "None"):
            print("Brak tekstu!")
            continue
        try:
            if not os.path.exists(podfolder+"\\"+str(tekst[0])+"\\"+str(tekst[1])):
                os.makedirs(podfolder+"\\"+str(tekst[0])+"\\"+str(tekst[1]))
            plik = open(podfolder+"\\"+str(tekst[0])+"\\"+str(tekst[1])+"\\"+tekst[2][0]+".txt","w")
            try:
                plik.writelines([ slowo + ' ' for slowo in tekst[2]])
                print( "s", end = '' ) 
            except:
                print( "\n\nF\n",tekst,"\n\n", end = '' )
                
            finally:
                plik.close()
        except:
            print(tekst)
    print("\n\nWszystko pobrane mordeczko!\n\n\a\a\a")
    return

def pobierz_od_zera_v2(a=0,b=-1,podfolder="Dane"):
    if not input(os.getcwd()+"\\"+podfolder+"\n\nJesteś pewien że podany katalog jest właściwy? T/N\n").lower().startswith("t"):
        return
    i = 1
    for link in pobierz_linki()[a:b]:
        tekst = pobierz_tekst( link[0], link[1] )
        if (tekst == None or tekst == "None" or tekst[2] == None or tekst[2] == "None"):
            print("Brak tekstu!")
            continue
        try:
            if not os.path.exists(podfolder+"\\"+str(tekst[0])+"\\"+str(tekst[1])):
                os.makedirs(podfolder+"\\"+str(tekst[0])+"\\"+str(tekst[1]))
            plik = open(podfolder+"\\"+str(tekst[0])+"\\"+str(tekst[1])+"\\"+i+".txt","w")
            try:
                plik.writelines([ slowo + ' ' for slowo in tekst[2]])
                print( "s", end = '' ) 
            except:
                print( "\n\nF\n",tekst,"\n\n", end = '' )
                
            finally:
                plik.close()
        except:
            print(tekst)
        i += 1
    print("\n\nWszystko pobrane mordeczko!\n\n\a\a\a")
    return
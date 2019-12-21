#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def zlicz_slowa(tekst,lista_slow):
    if len(tekst.split('\n')) == 1:
        for slowo in tekst.split(' '):
            if len( slowo ) < 3:
                continue
            if slowo in lista_slow:
                lista_slow[slowo] += 1
            else:
                lista_slow[slowo] = 1
    else:
        for wejscie in tekst.split('\n'):
            wejscie = wejscie.split(' ')
            if len(wejscie) == 2:
                slowo = wejscie[0] 
                ilosc = int(wejscie[1])
                if slowo in lista_slow:
                    lista_slow[slowo] += ilosc
                else:
                    lista_slow[slowo] = ilosc
    return lista_slow

def sumuj_lata(sciezka):
    if not os.path.exists(sciezka):
        print("Ni ma")
        return
    lista_kat = [x for x in os.listdir(sciezka) if os.path.isdir(sciezka+'\\'+x)]
    for katalog in lista_kat:
        sumuj_lata(sciezka + '\\' + katalog)

    lista_slow = {}
    lista_plikow = [x for x in os.listdir(sciezka) if not os.path.isdir(sciezka+'\\'+x)]
    for plik in lista_plikow:
        czytaj = open(sciezka+'\\' + plik, 'r')
        try:
            lista_slow = zlicz_slowa( czytaj.read(), lista_slow)
        finally:
            czytaj.close()
    zapis = open(sciezka+'.txt','w')
    try:
        zapis.writelines([ str(slowo) + ' ' + str(lista_slow[slowo]) + '\n' for slowo in lista_slow.keys()])
        print( ".", end = '' ) 
    except:
        print( "\ndupa\n\n", end = '' )
                
    finally:
        zapis.close()


    return

sumuj_lata("C:\\Users\\Adam\\Source\\Repos\\Blaslagh\\Wizu\\Dane")
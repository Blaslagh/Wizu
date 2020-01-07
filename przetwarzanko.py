# -*- coding: utf-8 -*-

import os
import win32com.client as wincl
from gtts import gTTS



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

def sumuj_lata(sciezka='Dane'):
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
	except:
		print( "\ndupa\n\n", end = '' )
				
	finally:
		zapis.close()


	return

def analizka_lat(sciezka):
	if not os.path.exists(sciezka):
		print("Ni ma")
		return
	lista_kat = [x for x in os.listdir(sciezka) if os.path.isdir(sciezka+'\\'+x)]
	lata={}
	for artysta in lista_kat:
		lista_kat2 = [x for x in os.listdir(sciezka+'\\'+artysta) if os.path.isdir(sciezka+'\\'+artysta+'\\'+x)]
		atrysta_lata={}
		for rok in lista_kat2:
			try:
				if int(rok) in lata.keys():
					lata[int(rok)] += len(os.listdir(sciezka+'\\'+artysta+'\\'+rok))
				else:
					lata[int(rok)] = len(os.listdir(sciezka+'\\'+artysta+'\\'+rok))
				if int(rok) in atrysta_lata.keys():
					atrysta_lata[int(rok)] += len(os.listdir(sciezka+'\\'+artysta+'\\'+rok))
				else:
					atrysta_lata[int(rok)] = len(os.listdir(sciezka+'\\'+artysta+'\\'+rok))
			except:
				continue
		if not os.path.exists("Lata"):
			os.makedirs("Lata")
		zapis = open("Lata\\"+artysta+'.txt','w')
		try:
			zapis.writelines([ str(rok) + ' ' + str(atrysta_lata[rok]) + '\n' for rok in sorted(atrysta_lata.keys())])
			print( "o", end = '' )
		except:
			print( "N", end = '' )
		finally:
			zapis.close()
	zapis = open("Lata\\"+'wszyscy.txt','w')
	try:
		zapis.writelines([ str(rok) + ' ' + str(lata[rok]) + '\n' for rok in sorted(lata.keys())])
		print( "o", end = '' )
	except:
		print( "N", end = '' )
	finally:
		zapis.close()
	return

def wczytywanko(sciezka):
	if not os.path.exists(sciezka):
		print("Ni ma")
		return False
	elif os.path.isdir(sciezka):
		print("nie plik")
		return
	else:
		plik = open( sciezka ,'r')
		slownik={}
		for x in plik.readlines():
			slownik[x.split()[0]] = x.split()[1]
		plik.close()
		return slownik

def skomplikowalnosc(slownik_tekst):
	rozne = len( slownik_tekst.keys() )
	ilosc = sum( [ int(x) for x in slownik_tekst.values() ] )
	return (rozne/ilosc)

def czytaj_x( slownik, x=10 ):
	zbior = list( {k: v for k, v in sorted( slownik.items(), key=lambda item: int(item[1]), reverse=True)}.keys() )[0:x]
	wincl.Dispatch("SAPI.SpVoice").Speak("Walić w dupala windowsa i microsoft")
	wincl.Dispatch("SAPI.SpVoice").Speak(zbior)
	return

def czytanko_dla_art(sciezka_in='Dane', sciezka_out='Czytanie', ilosc=10):
	if not os.path.exists(sciezka_in):
		print("Ni ma")
		return
	lata={}
	if not os.path.exists(sciezka_out):
		os.makedirs(sciezka_out)
	for artysta in [x for x in os.listdir(sciezka_in) if not os.path.isdir(sciezka_in+'\\'+x)]:
		try:
			zapisz_czytanie(wczytywanko(sciezka_in+'\\'+artysta),sciezka_out+'\\'+artysta[0:-4], ilosc)
			print( "o", end = '' )
		except:
			print( "N", end = '' )
	return

def zapisz_czytanie( slownik, sciezka_out='czytanie', x=1000 ):
	zbior = ''.join(list( {k: v for k, v in sorted( slownik.items(), key=lambda item: int(item[1]), reverse=True)}.keys() )[0:x])
	tts = gTTS(text=zbior, lang='pl', slow=True)
	tts.save(sciezka_out+".mp3")
	return


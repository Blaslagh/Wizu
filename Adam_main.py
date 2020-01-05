# -*- coding: utf-8 -*-


#       main z moja sciezka, chcesz swoj? ZRÓB SE!

import os

os.chdir("C:\\Users\\Adam\\Source\\Repos\\Blaslagh\\Wizu")

import pobieranko, przetwarzanko

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
			print( "juppi\n\n", end = '' )
		except:
			print( "\ndupa\n\n", end = '' )
		finally:
			zapis.close()
	zapis = open("Lata\\"+'wszyscy.txt','w')
	try:
		zapis.writelines([ str(rok) + ' ' + str(lata[rok]) + '\n' for rok in sorted(lata.keys())])
		print( "juppi\n\n", end = '' )
	except:
		print( "\ndupa\n\n", end = '' )
	finally:
		zapis.close()
	return

analizka_lat("Dane")
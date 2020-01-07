# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import przetwarzanko, os

def wykresuj_lata(wejscie, artysta):
	plt.clf()
	if wejscie == False:
		print("dupcia: "+artysta)
		return
	with plt.style.context('seaborn-darkgrid'):
		plt.plot([int(x) for x in wejscie.keys()],  [int(wejscie[x]) for x in wejscie.keys()],'ro' )
		plt.grid(True)
		plt.xlim(min([int(x) for x in wejscie.keys()])-1, max([int(x) for x in wejscie.keys()])+1)
		plt.xlabel(r"Rok")
		plt.ylabel(r"Ilość wydanych utworów")
		plt.title(artysta)
		plt.savefig("Lata\\wykresy\\"+artysta+".jpg")
	return

def wykresuj_lata_ograniczone(wejscie, artysta, srednia_wszyscy):
	plt.clf()
	if wejscie == False:
		print("dupcia "+artysta)
		return
	x = [int(i) for i in wejscie.keys() if ( int(i) > 1960 and int(i) < 2020 )]
	y = [int(wejscie[str(i)]) for i in x]
	y_srednia = sum(y)/len(x)
	all_srednia = srednia_wszyscy
	with plt.style.context('seaborn-darkgrid'):
		plt.plot( x, y, 'ro' )
		plt.axhline(y_srednia, linestyle='--')
		plt.axhline(all_srednia, linestyle='--', color='dimgrey')
		plt.grid(True)
		plt.xlim(min(x)-2, 2020)
		plt.xlabel(r"Rok")
		plt.ylabel(r"Ilość wydanych utworów")
		plt.title(artysta)
		plt.savefig("Lata\\wykresy\\"+artysta+"_o.jpg")
	return

def wykresuj_skomplikowanie_suma(wejscie):
	if wejscie == False:
		print("dupcia "+artysta)
		return
	x={}
	for artysta in [x for x in os.listdir(wejscie) if not os.path.isdir(wejscie+'\\'+x)]:
		try:
			x[artysta[0:-4]]=przetwarzanko.skomplikowalnosc(przetwarzanko.wczytywanko(wejscie+'\\'+artysta))
			print( "o", end = '' )
		except:
			print( "N", end = '' )
	iksy = list(x.keys())
	wysokosci = [ x[i] for i in iksy ]
	plt.clf()
	with plt.style.context('seaborn-darkgrid'):
		plt.bar( iksy, wysokosci )
		plt.axhline(przetwarzanko.skomplikowalnosc(przetwarzanko.wczytywanko(wejscie+'.txt')), linestyle='--', color='dimgrey')
		plt.grid(True)
		plt.xticks(rotation='vertical')
		plt.ylabel(r"Sumaryczna skomplikowalność tekstu")
		plt.margins(0.1)
		plt.subplots_adjust(bottom=0.4)
		plt.savefig("Skomplikowanie.jpg")
	return

def wykresuj_skomplikowanie_srednia(wejscie):
	if wejscie == False:
		print("dupcia ")
		return
	x={}
	for artysta in [x for x in os.listdir(wejscie) if os.path.isdir(wejscie+'\\'+x)]:
		cos=[]
		for rok in [x for x in os.listdir(wejscie+'\\'+artysta) if not os.path.isdir(wejscie+'\\'+artysta+'\\'+x)]:
			try:
				wartosc = przetwarzanko.skomplikowalnosc( przetwarzanko.wczytywanko( wejscie+'\\'+artysta+'\\' + rok ) )
				cos.append(wartosc)
			except:
				print("Błąd przetwarzania: "+wejscie+'\\'+artysta+'\\' + rok )
		x[artysta[0:-4]] = sum(cos)/len(cos)
			

	iksy = list(x.keys())
	wysokosci = [ x[i] for i in iksy ]
	plt.clf()
	with plt.style.context('seaborn-darkgrid'):
		plt.bar( iksy, wysokosci)
		plt.axhline(sum(wysokosci)/len(wysokosci), linestyle='--', color='dimgrey')
		plt.grid(True)
		plt.xticks(rotation='vertical')
		plt.ylabel(r"Średnia skomplikowalność tekstu")
		plt.margins(0.1)
		plt.subplots_adjust(bottom=0.4)
		plt.savefig("Skomplikowanie_srednia.jpg")
	return

def wykresuj_skomplikowanie_po_latach(wejscie):
	if wejscie == False:
		print("dupcia ")
		return
	x={}
	for artysta in [x for x in os.listdir(wejscie) if os.path.isdir(wejscie+'\\'+x)]:

		for rok in [x for x in os.listdir(wejscie+'\\'+artysta) if not os.path.isdir(wejscie+'\\'+artysta+'\\'+x)]:
			try:
				wartosc = przetwarzanko.skomplikowalnosc( przetwarzanko.wczytywanko( wejscie+'\\'+artysta+'\\' + rok ) )
				if int(rok[0:-4]) in list(x.keys()):
					x[int(rok[0:-4])].append(float(wartosc))
				else:
					x[int(rok[0:-4])] = [float(wartosc)]
			except:
				if rok[0:-4]=='NW':
					continue
				print("Błąd przetwarzania: "+wejscie+'\\'+artysta+'\\' + rok )
	iksy = sorted([i for i in x.keys() if i<2020 and i>1950])
	wysokosci = [ sum(x[i])/len(x[i]) for i in iksy ]
	plt.clf()
	with plt.style.context('seaborn-darkgrid'):
		plt.axhline(sum(wysokosci)/len(wysokosci), linestyle='--', color='dimgrey')
		plt.plot( iksy, wysokosci)
		plt.grid(True)
		plt.xticks(rotation='vertical')
		plt.ylabel(r"Średnia skomplikowalność tekstu")
		plt.margins(0.1)
		plt.subplots_adjust(bottom=0.4)
		plt.savefig("Skomplikowanie_w_latach.jpg")
	return
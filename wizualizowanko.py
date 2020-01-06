# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def wykresuj_lata(wejscie, artysta):
	if wejscie == False:
		print("dupcia: "+artysta)
		return
	plt.plot([int(x) for x in wejscie.keys()],  [int(wejscie[x]) for x in wejscie.keys()],'o' )
	plt.grid(True)
	plt.xlim(min([int(x) for x in wejscie.keys()])-1, max([int(x) for x in wejscie.keys()])+1)
	plt.xlabel(r"Rok")
	plt.ylabel(r"Ilość wydanych utworów")
	plt.title(artysta)
	plt.savefig("Lata\\wykresy\\"+artysta+".jpg")

def wykresuj_lata_ograniczone(wejscie, artysta):
	if wejscie == False:
		print("dupcia "+artysta)
		return
	plt.plot([int(x) for x in wejscie.keys()],  [int(wejscie[x]) for x in wejscie.keys()],'o' )
	plt.grid(True)
	plt.xlim(1960, 2020)
	plt.xlabel(r"Rok")
	plt.ylabel(r"Ilość wydanych utworów")
	plt.title(artysta)
	plt.savefig("Lata\\wykresy\\"+artysta+"_o.jpg")
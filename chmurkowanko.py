import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import przetwarzanko



def chmuruj_slownik(wejscie_slownik=przetwarzanko.wczytywanko("Dane.txt"), sciezka='chmura.jpg'):

	slownik_do_chmury = {}

	for i in wejscie_slownik.keys():
		slownik_do_chmury[ str(i) ] = float( wejscie_slownik[i] )

	wordcloud = WordCloud().generate_from_frequencies(slownik_do_chmury)

	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.savefig(sciezka)
	return

def chmuruj_slownik_ponad_x(wejscie_slownik=przetwarzanko.wczytywanko("Dane.txt"), sciezka='chmura.jpg', x = 3):

	slownik_do_chmury = {}

	for i in wejscie_slownik.keys():
		if len(str(i)) >= x:
			slownik_do_chmury[ str(i) ] = float( wejscie_slownik[i] )

	wordcloud = WordCloud().generate_from_frequencies(slownik_do_chmury)

	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.savefig(sciezka)
	return

def chmury_4_all(sciezka_in, sciezka_out, ilosc):
	if not os.path.exists(sciezka_in):
		print("Ni ma")
		return
	lata={}
	if not os.path.exists(sciezka_out):
		os.makedirs(sciezka_out)
	for artysta in [x for x in os.listdir(sciezka_in) if os.path.isdir(sciezka_in+'\\'+x)]:
		atrysta_lata={}
		if not os.path.exists(sciezka_out+'\\'+artysta):
			os.makedirs(sciezka_out+'\\'+artysta)

		for rok in [x for x in os.listdir(sciezka_in+'\\'+artysta) if os.path.isdir(sciezka_in+'\\'+artysta+'\\'+x)]:
			try:
				chmuruj_slownik_ponad_x(przetwarzanko.wczytywanko(sciezka_in+'\\'+artysta+'\\'+rok+'.txt'),sciezka_out+'\\'+artysta+'\\'+rok+'.jpg', ilosc)
				print( "o", end = '' )
			except:
				print( "N", end = '' )
		print( "\n", end = '' )
	for artysta in [x for x in os.listdir(sciezka_in) if not os.path.isdir(sciezka_in+'\\'+x)]:
		try:
			chmuruj_slownik_ponad_x(przetwarzanko.wczytywanko(sciezka_in+'\\'+artysta+'.txt'),sciezka_out+'\\'+artysta+'.jpg', ilosc)
			print( "o", end = '' )
		except:
			print( "N", end = '' )
	return


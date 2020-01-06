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

def chmury_4_all(sciezka):
	if not os.path.exists(sciezka):
		print("Ni ma")
		return
	lata={}
	if not os.path.exists("Chmury"):
		os.makedirs("Chmury")
	for artysta in [x for x in os.listdir(sciezka) if os.path.isdir(sciezka+'\\'+x)]:
		atrysta_lata={}
		if not os.path.exists("Chmury\\"+artysta):
			os.makedirs("Chmury\\"+artysta)

		for rok in [x for x in os.listdir(sciezka+'\\'+artysta) if os.path.isdir(sciezka+'\\'+artysta+'\\'+x)]:
			try:
				chmuruj_slownik(przetwarzanko.wczytywanko(sciezka+'\\'+artysta+'\\'+rok+'.txt'),"Chmury\\"+artysta+'\\'+rok+'.jpg')
				print( "o", end = '' )
			except:
				print( "N", end = '' )
	return


def chmuruj_slownik_ponad_4(wejscie_slownik=przetwarzanko.wczytywanko("Dane.txt"), sciezka='chmura.jpg'):

	slownik_do_chmury = {}

	for i in wejscie_slownik.keys():
		if len(str(i)) > 3:
			slownik_do_chmury[ str(i) ] = float( wejscie_slownik[i] )

	wordcloud = WordCloud().generate_from_frequencies(slownik_do_chmury)

	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.savefig(sciezka)
	return
import os
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import przetwarzanko
from PIL import Image, ImageFilter, ImageEnhance


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

	wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate_from_frequencies(slownik_do_chmury)
	wordcloud.to_file(sciezka)

	return

def chmury_4_all(sciezka_in="Dane.txt", sciezka_out="Def", ilosc=3):
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
			chmuruj_slownik_ponad_x(przetwarzanko.wczytywanko(sciezka_in+'\\'+artysta),sciezka_out+'\\'+artysta[0:-4]+'.jpg', ilosc)
			print( "o", end = '' )
		except:
			print( "N", end = '' )
	return

def chmury_z_grafik(wejscie_slownik, art, x=3):
	slownik_do_chmury = {}
	for i in wejscie_slownik.keys():
		if len(str(i)) >= x:
			slownik_do_chmury[ str(i) ] = float( wejscie_slownik[i] )
	zdjecie=Image.open('Chmury\\Grafiki_do_chmur\\'+art+'.jpg')
	mask = np.array(zdjecie)
	
	
	chmurka = WordCloud( background_color="white", mode="RGB", mask=mask, max_font_size=70, max_words=3000, width=1500, height=1500, contour_width=0).generate_from_frequencies(slownik_do_chmury)
	image_colors = ImageColorGenerator(mask)
	chmurka.recolor(color_func=image_colors)
	chmurka.to_file('Chmury\\Grafochmurki\\'+art+'.jpg')
	slowa=Image.open('Chmury\\Grafochmurki\\'+art+'.jpg')
	slowa = slowa.resize(zdjecie.size)
	zdjecie = zdjecie.filter(ImageFilter.BLUR)
	zdjecie = ImageEnhance.Color(zdjecie)
	zdjecie = zdjecie.enhance(0.5)
	polaczone = Image.blend(slowa,zdjecie,0.15)

	polaczone.save('Chmury\\Grafochmurki\\'+art+'_z_tlem.jpg')

def chmury_4_art(sciezka_in="Dane", sciezka_out="Chmury", ilosc=3):
	if not os.path.exists(sciezka_in):
		print("Ni ma")
		return
	for artysta in [x for x in os.listdir(sciezka_in) if not os.path.isdir(sciezka_in+'\\'+x)]:
		try:
			chmuruj_slownik_ponad_x(przetwarzanko.wczytywanko(sciezka_in+'\\'+artysta),sciezka_out+'\\'+artysta[0:-4]+'.jpg', ilosc)
			print( "o", end = '' )
		except:
			print( "N", end = '' )
	return
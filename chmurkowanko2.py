import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud



def chmuruj_slownik(wejscie_slownik):

    slownik_do_chmury = {}

    for i in wejscie_slownik.keys():
        slownik_do_chmury[ str(i) ] = float( wejscie_slownik[i] )

    wordcloud = WordCloud().generate_from_frequencies(slownik_do_chmury)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

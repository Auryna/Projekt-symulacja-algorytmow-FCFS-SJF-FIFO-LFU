#ten skrypt jest odpowiedzialny za działania symulacji zastepowania stron
import strona
import FIFO
import LFU
def main():#glowna funkcja
    f = open('wyniki_zastepowania_stron.txt', 'w')
    strony=[]
    ilosc=25
    for i in range(ilosc):
        strony.append(strona.strona(i))
    rozmiar=5
    f.write(f"dla ilosci stron {ilosc}i rozmiarze{rozmiar}\n")
    f.write(f"ilosc bledow dla algorytmu fifo:{FIFO.fifo(strony,rozmiar)},dla LFU: {LFU.lfu(strony,rozmiar)}\n")
    strony = []
    ilosc = 75
    for i in range(ilosc):
        strony.append(strona.strona(i))
    rozmiar = 5
    f.write(f"dla ilosci stron {ilosc}i rozmiarze{rozmiar}\n")
    f.write(f"ilosc bledow dla algorytmu fifo:{FIFO.fifo(strony, rozmiar)},dla LFU: {LFU.lfu(strony, rozmiar)}\n")
    strony = []
    ilosc = 125
    for i in range(ilosc):
        strony.append(strona.strona(i))
    rozmiar = 5
    f.write(f"dla ilosci stron {ilosc}i rozmiarze{rozmiar}\n")
    f.write(f"ilosc bledow dla algorytmu fifo:{FIFO.fifo(strony, rozmiar)},dla LFU: {LFU.lfu(strony, rozmiar)}\n")
    ilosc = 25
    for i in range(ilosc):
        strony.append(strona.strona(i))
    rozmiar = 10
    f.write(f"dla ilosci stron {ilosc}i rozmiarze{rozmiar}\n")
    f.write(f"ilosc bledow dla algorytmu fifo:{FIFO.fifo(strony, rozmiar)},dla LFU: {LFU.lfu(strony, rozmiar)}\n")
    strony = []
    ilosc = 75
    for i in range(ilosc):
        strony.append(strona.strona(i))
    rozmiar = 10
    f.write(f"dla ilosci stron {ilosc}i rozmiarze{rozmiar}\n")
    f.write(f"ilosc bledow dla algorytmu fifo:{FIFO.fifo(strony, rozmiar)},dla LFU: {LFU.lfu(strony, rozmiar)}\n")
    strony = []
    ilosc = 125
    for i in range(ilosc):
        strony.append(strona.strona(i))
    rozmiar = 10
    f.write(f"dla ilosci stron {ilosc}i rozmiarze{rozmiar}\n")
    f.write(f"ilosc bledow dla algorytmu fifo:{FIFO.fifo(strony, rozmiar)},dla LFU: {LFU.lfu(strony, rozmiar)}\n")
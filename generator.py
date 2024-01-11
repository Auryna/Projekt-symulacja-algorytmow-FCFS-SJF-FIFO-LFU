import proces
import numpy as np
def generuj_procesy(ilosc, sr_czas_przybycia, czas_trwania,odchylenie_standardowe_przybycia,odchylenie_standardowe_wykonania,):#ilosc procesow
    procesy=[]
    for pid in range(ilosc):
        czas_przybycia=max(1,int(np.random.normal(sr_czas_przybycia, odchylenie_standardowe_przybycia)))
        czas_wykonania=max(0,int(np.random.normal(czas_trwania, odchylenie_standardowe_wykonania)))
        procesy.append(proces.proces(pid,czas_przybycia,czas_wykonania))
    return procesy
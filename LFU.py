def lfu(strony, rozmiar_ramki):
    ramka=[]
    bledy=0
    for strona in strony:
        strona.uzycia+=1
        if strona not in strony:
            bledy+=1
            if len(ramka)<rozmiar_ramki:
                ramka.append(strona)
            else:
                ramka.sort(key=lambda x: x.uzycia)
                ramka.pop(0)
                ramka.append(strona)
    return bledy
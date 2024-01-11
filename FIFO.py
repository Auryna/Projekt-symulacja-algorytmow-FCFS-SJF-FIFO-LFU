def fifo(strony,rozmiar_ramki):
    ramka=[]
    bledy=0
    for strona in strony:
        if strona not in ramka:
            bledy+=1
            if len(ramka)<rozmiar_ramki:
                ramka.append(strona)
            else:
                ramka.pop(0)
                ramka.append(strona)
    return bledy
def fcfs(procesy):
    procesy.sort(key=lambda x: x.czas_przybycia)
    czas_aktualny=0
    for proces in procesy:
        if czas_aktualny<proces.czas_przybycia:
            czas_aktualny=proces.czas_przybycia
        proces.czas_oczekiwania=czas_aktualny=proces.czas_przybycia
        proces.czas_ukonczenia=czas_aktualny+proces.czas_wykonania
        czas_aktualny+=proces.czas_ukonczenia
    return czas_aktualny

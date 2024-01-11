#ten skrypt jest odpowiedzialny za działania symulacji planowania czasu procesora
import generator
import FCFS
import SJF

def main():#glowna funcja
    f=open('wyniki_planowania_czasu_procesora.txt','w')
    temp1=0#zmienna do pomocy
    temp2=0#zmienna do pomocy
    procesy1=generator.generuj_procesy(25,50,5,50,0)
    procesy2=generator.generuj_procesy(75,50,5,50,0)
    procesy3=generator.generuj_procesy(125, 50, 5, 50, 0)
    f.write("25 procesow o czasasch nadejscia od 0 do 100 oraz czasie rownym wykonania 0\n")
    FCFS.fcfs(procesy1)
    for proces in procesy1:
        temp1 += proces.czas_oczekiwania
    SJF.sjf(procesy1)
    for proces in procesy1:
        temp2 += proces.czas_oczekiwania
    f.write(f"sredni czas wykonania dla FCFS:{temp1 / 25},a dlaSJF{temp2 / 25}\n")
    f.write("50 procesow o czasasch nadejscia od 0 do 100 oraz czasie rownym wykonania 0\n")
    temp1=0
    temp2=0
    FCFS.fcfs(procesy2)
    for proces in procesy2:
        temp1 += proces.czas_oczekiwania
    SJF.sjf(procesy2)
    for proces in procesy2:
        temp2 += proces.czas_oczekiwania
    f.write(f"sredni czas wykonania dla FCFS:{temp1 / 50},a dlaSJF{temp2 / 50}\n")
    f.write("125 procesow o czasasch nadejscia od 0 do 100 oraz czasie rownym wykonania 0\n")
    temp1 = 0
    temp2 = 0
    FCFS.fcfs(procesy3)
    for proces in procesy3:
        temp1+=proces.czas_oczekiwania
    SJF.sjf(procesy3)
    for proces in procesy3:
        temp2 += proces.czas_oczekiwania
    f.write(f"sredni czas wykonania dla FCFS:{temp1/125},a dlaSJF{temp2/125}\n")
    procesy1 = generator.generuj_procesy(25, 0, 5, 0, 5)
    procesy2 = generator.generuj_procesy(75, 0, 5, 0, 5)
    procesy3 = generator.generuj_procesy(125, 0, 5, 0, 5)
    f.write("25 procesow o czasasch nadejscia 0 oraz czasie wykonnia od 1 do 10\n")
    FCFS.fcfs(procesy1)
    for proces in procesy1:
        temp1 += proces.czas_oczekiwania
    SJF.sjf(procesy1)
    for proces in procesy1:
        temp2 += proces.czas_oczekiwania
    f.write(f"sredni czas wykonania dla FCFS:{temp1 / 25},a dlaSJF{temp2 / 25}\n")
    f.write("50 procesow o czasasch nadejscia 0 oraz czasie wykonnia od 1 do 10\n")
    temp1 = 0
    temp2 = 0
    FCFS.fcfs(procesy2)
    for proces in procesy2:
        temp1 += proces.czas_oczekiwania
    SJF.sjf(procesy2)
    for proces in procesy2:
        temp2 += proces.czas_oczekiwania
    f.write(f"sredni czas wykonania dla FCFS:{temp1 / 50},a dlaSJF{temp2 / 50}\n")
    f.write("125 procesow o czasasch nadejscia 0 oraz czasie wykonnia od 1 do 10\n")
    temp1 = 0
    temp2 = 0
    FCFS.fcfs(procesy3)
    for proces in procesy3:
        temp1 += proces.czas_oczekiwania
    SJF.sjf(procesy3)
    for proces in procesy3:
        temp2 += proces.czas_oczekiwania
    f.write(f"sredni 1czas wykonania dla FCFS:{temp1 / 125},a dlaSJF{temp2 / 125}\n")
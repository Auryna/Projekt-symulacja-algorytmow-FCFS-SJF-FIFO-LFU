import planowanie_czasu_procesora
import zastepowanie_stron

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')
dziala=1 #zmienna do zapetlania programu
while dziala==1:
    wybor=input("Wyberz opcje symulacji:\n1. planowanie czasu procesora\n2. zastepowanie stron.\n3. Koniec.\nWpisz wybor: ")
    if wybor=="1":
        planowanie_czasu_procesora.main()
        dziala = 0
    elif wybor=="2":
        zastepowanie_stron.main()
        dziala = 0
    elif wybor=="3":
        print("koniec pracy")
        dziala=0
    else:
        print("wybierz istniejąca opcje")

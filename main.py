# -*- coding: utf-8 -*-
import time

print("Witam w programie sprawdzającym, czy wyraz jest palindromem!!!")
time.sleep(1.5)

T = False
kopia = ""

while T == False:
    wyraz_in = str(input("\nProszę o podanie wyrazu do sprawdzenia: "))
    wyraz_out = wyraz_in.lower().replace(" ", "")

    for zmienna in range(len(wyraz_out)):
        kopia = kopia + wyraz_out[len(wyraz_out) - 1:len(wyraz_out)]
        wyraz_out = wyraz_out[:len(wyraz_out) - 1]

    print("\nOdpowiedź, to...", end=" ")
    time.sleep(2)

    if wyraz_in.lower().replace(" ", "") == kopia:
        print("wyraz \"{}\" jest palindromem!! :D".format(wyraz_in))
    else:
        print("wyraz \"{}\" nie jest palindromem :(".format(wyraz_in))
    time.sleep(1)

    while T == False:
        wybor = str(input("\nCzy chcesz zakończyć działanie programu? - ")).upper()
        time.sleep(0.5)
        if wybor == ("T" or "TAK"):
            T = True
        elif wybor == ("N" or "NIE"):
            T = False
            break
        else:
            print("\n!!!!!! Odpowiedź nie została poprawnie wprowadzona !!!!!!")
            time.sleep(1)
            print(
                "\nNapisz \"T\" lub \"TAK\", aby wyjść z programu\nNapisz \"N\" lub \"NIE\", aby sprawdzić kolejny wyraz do sprawdzenia")
            time.sleep(2)

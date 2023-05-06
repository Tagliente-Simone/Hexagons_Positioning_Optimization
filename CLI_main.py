from folder_1.CalculateDimension import Calculate as cd
from folder_2.CalculateDimension import compute as cd2
import sys
from termcolor import colored

def checkfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    

def hexagon_test(dest):
    max_found = 0;
    best_compo = "0-0"

    if float(dest) >= 30 and float(dest)  <= 40:
        compo_list = ["5-6-7-8-7-6-5", "6-7-8-9-8-7-6"]
    elif float(dest)  > 40 and float(dest)  <= 50:
        compo_list = ["6-7-8-9-8-7-6", "5-6-7-8-7-6-5", "4-5-6-5-4"]
    elif float(dest)  > 50 and float(dest)  <= 70:
        compo_list = ["4-5-6-5-4", "4-5-6-7-6-5-4", "3-4-5-4-3"]
    elif float(dest)  > 70:
        compo_list = ["3-4-3", "3-4-5-4-3"]

    for i in range(0, len(compo_list)):
        rows_array = [float(i) for i in compo_list[i].split('-')]
        if(len(rows_array) % 2 == 1):
            n_rows = len(rows_array)
            radius = float(dest)
            radius = radius / 20
            #Call the function to calculate the dimension of the hexagon
            total = cd(radius, n_rows, rows_array, 9999)
            total_tubes_1 = sum([int(i) for i in compo_list[i].split('-')]) * total
            if total_tubes_1 > max_found:
                max_found = total_tubes_1
                best_compo = compo_list[i]

    print("     -> Forma esagonale: " + str(best_compo))
    return max_found

def rectangle_test(dest):

    rows = [(4, 5), (6, 7)]

    max_number = 0
    best_config = (0, 0)

    for row in rows:
        
        total_tubes = cd2(float(dest)/20, row[0], row[1], row[1])
        if total_tubes > max_number:
            max_number = total_tubes
            best_config = row
            
    print("     -> Forma rettangolare: " + str(best_config))
    return max_number





quit = True
while True:
        print(colored("-----------------NUOVA SESSIONE-------------------------------------------------------------------", "green"))
        print("Inserisci il diametro del tubo in millimetri (digita 'help' per la lista dei comandi): ")
        diameter = input().lower()
        if diameter == "quit":
            sys.exit()
        elif diameter == "help":
            print(colored("------------------------------------LISTA DEI COMANDI", "green"))
            print(colored("     -> 'help': mostra la lista dei comandi", "yellow"))
            print(colored("     -> 'quit': esce dal programma", "yellow"))
            print(colored("     -> 'conversion': converte il diametro da millimetri a pollici", "yellow"))
        elif diameter == "conversion":
            print("Inserisci il diametro del tubo in pollici: ")
            diameter_inches = input()
            if checkfloat(diameter_inches):
                diameter_mm = float(diameter_inches) * 25.4
                print(colored(f"Il diametro del tubo in millimetri è {diameter_mm}", "yellow"))
            else:
                print(colored("Inserisci un valore numerico valido", "red"))
        elif checkfloat(diameter) and float(diameter) >= 30 and float(diameter) <= 90:
            print(colored("------------------------------------COMPOSIZIONI CONSIGLIATE", "green"))
            total_hexagon = hexagon_test(diameter)
            total_rectangle = rectangle_test(diameter)
            print(colored("------------------------------------NUMERO TOTALE DI TUBI", "green"))
            print(colored(f"     -> Forma esagonale: {total_hexagon}", "yellow"))
            print(colored(f"     -> Forma rettangolare: {total_rectangle}", "yellow"))
        else:
            print(colored("Inserisci un comando valido o un diametro valido compreso tra 30mm e 90mm, o digita 'quit' per uscire", "red"))










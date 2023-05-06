from folder_1.CalculateDimension import Calculate as cd
from folder_2.CalculateDimension import compute as cd2
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
from termcolor import colored

def checkfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
class App:


    

    def hexagon_test(self, dest, console_log):
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

        log_msg = f"Composizioni consigliate per il tubo di diametro {dest}mm:\n"
        log_msg += f"- Forma esagonale: {best_compo}\n"
        console_log.config(state="normal")
        console_log.insert(tk.END, log_msg)
        console_log.config(state="disabled")

        return max_found

    def rectangle_test(self, dest, console_log):

        rows = [(4, 5), (6, 7)]

        max_number = 0
        best_config = (0, 0)

        for row in rows:
            
            total_tubes = cd2(float(dest)/20, row[0], row[1], row[1])
            if total_tubes > max_number:
                max_number = total_tubes
                best_config = row
        log_msg = f"Composizioni consigliate per il tubo di diametro {dest}mm:\n"
        log_msg += f"- Forma rettangolare: {best_config}\n"
        console_log.config(state="normal")
        console_log.insert(tk.END, log_msg)
        console_log.config(state="disabled")   
        return max_number

    def __init__(self, master):
        self.master = master
        master.title("Tubi")

        # Create input label and entry
        self.label = tk.Label(master, text="Inserisci il diametro del tubo in millimetri:")
        self.label.pack()

        self.diameter_entry = tk.Entry(master)
        self.diameter_entry.pack()

        # Create button to calculate tube compositions
        self.calculate_button = tk.Button(master, text="Calcola composizioni", command=self.calculate_compositions)
        self.calculate_button.pack()

        # Create button to convert diameter to inches
        self.convert_button = tk.Button(master, text="Conversione pollici", command=self.convert_diameter)
        self.convert_button.pack()

        # Create console log
        self.console_log = tk.Text(master)
        self.console_log.config(state="disabled")
        self.console_log.pack()

    def calculate_compositions(self):
        diameter = self.diameter_entry.get()
        if checkfloat(diameter) and float(diameter) >= 30 and float(diameter) <= 90:
            total_hexagon = self.hexagon_test(diameter, self.console_log)
            total_rectangle = self.rectangle_test(diameter, self.console_log)
            log_msg = f"Numero totale di tubi per il tubo di diametro {diameter}mm:\n"
            log_msg += f"- Forma esagonale: {total_hexagon}\n"
            log_msg += f"- Forma rettangolare: {total_rectangle}\n\n"
            self.console_log.config(state="normal")
            self.console_log.insert(tk.END, log_msg)
            self.console_log.config(state="disabled")
        else:
            messagebox.showerror("Errore", "Inserisci un diametro valido compreso tra 30mm e 90mm")

    def convert_diameter(self):
        diameter_inches = simpledialog.askfloat("Conversione pollici", "Inserisci il diametro del tubo in pollici:")
        if diameter_inches is not None:
            diameter_mm = diameter_inches * 25.4
            log_msg = f"Il diametro del tubo in millimetri è {diameter_mm}\n\n"
            self.console_log.config(state="normal")
            self.console_log.insert(tk.END, log_msg)
            self.console_log.config(state="disabled")
        else:
            messagebox.showerror("Errore", "Inserisci un valore numerico valido")

root = tk.Tk()
app = App(root)
root.mainloop()
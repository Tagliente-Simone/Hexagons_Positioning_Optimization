from folder_1.CalculateDimension import calculate_hexagon_dimensions as cd
from folder_2.CalculateDimension import calculate_rectangle_dimensions as cd2
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from PIL import ImageTk, Image
import math
from folder_2.Draw import draw_rectangles as draw_rects
from folder_1.Draw import draw_hexagons as draw_hexs



class App:

    def hexagon_test(self, weight, dest, console_log):
        max_found = 0;
        best_compo = ""

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
                hexagons = cd(radius, n_rows, rows_array, 9999)
                total = len(hexagons)
                single = sum([int(i) for i in compo_list[i].split('-')])
                total_tubes_1 =  single * total
                if single * weight < 25:
                    if total_tubes_1 > max_found:
                        max_found = total_tubes_1
                        best_compo = compo_list[i]
                        best_hex = hexagons
                else:
                    log_msg = f"Composizione {compo_list[i]} scartata per eccesso di peso\n"
                    console_log.config(state="normal")
                    console_log.insert(tk.END, log_msg)
                    console_log.config(state="disabled")
                    return -1


        log_msg = "**********************************************************************\n"
        log_msg += f"Composizioni consigliate per il tubo di diametro {dest} mm:\n"
        log_msg += f"- Forma esagonale: {best_compo} - Peso: {round(sum([int(i) for i in best_compo.split('-')]) * weight, 2)} Kg\n"
        console_log.config(state="normal")
        console_log.insert(tk.END, log_msg)
        console_log.config(state="disabled")
        draw_hexs(best_hex)

        return max_found

    def rectangle_test(self, weight, dest, console_log):

        rows = [(4, 5), (6, 7)]

        max_number = 0
        best_config = (0, 0)

        for row in rows:
            
            rects = cd2(float(dest)/20, row[0], row[1], row[1], weight)
            total_rect = len(rects)
            single_rect = (row[1] * int((row[1] / 2)) + row[0] * (row[1] - int((row[1]) / 2)))
            total_tubes = total_rect * single_rect
            if single_rect * weight < 25:
                if total_tubes > max_number:
                    max_number = total_tubes
                    best_config = row
                    best_rect = rects
            else:
                log_msg = f"Composizione {row} scartata per eccesso di peso\n"
                console_log.config(state="normal")
                console_log.insert(tk.END, log_msg)
                console_log.config(state="disabled")
                return -1

        log_msg = f"- Forma rettangolare: {best_config} - Peso: {round((best_config[1] * int((best_config[1] / 2)) + best_config[0] * (best_config[1] - int((best_config[1]) / 2))) * weight, 2)} Kg\n"
        console_log.config(state="normal")
        console_log.insert(tk.END, log_msg)
        console_log.config(state="disabled")   
        draw_rects(best_rect)
        return max_number
    
    def actual_hexagon_test(self, weight, dest, console_log, actual_compo):
        rows_array = [float(i) for i in actual_compo.split('-')]
        if(len(rows_array) % 2 == 1):
                n_rows = len(rows_array)
                radius = float(dest)
                radius = radius / 20
                #Call the function to calculate the dimension of the hexagon
                hexagons = cd(radius, n_rows, rows_array, 9999)
                total = len(hexagons)
                single = sum([int(i) for i in actual_compo.split('-')])

        log_msg = "######################################################################\n"
        log_msg += f"Composizione attuale per il tubo di diametro {dest} mm:\n"
        log_msg += f"- Forma esagonale: {actual_compo} - Peso: {round(sum([int(i) for i in actual_compo.split('-')]) * weight, 2)} Kg\n"
        log_msg += f"- Numero di tubi: {single * total}\n"
        console_log.config(state="normal")
        console_log.insert(tk.END, log_msg)
        console_log.config(state="disabled")
        return single*total


    def __init__(self, master):
        self.master = master
        master.title("Tubi")

        # Create input label and entry
        self.label = tk.Label(master, text="Inserisci il diametro del tubo in millimetri:")
        self.label.place(x=10, y=0)

        self.diameter_entry = ttk.Combobox(root, 
                                           values=self.read_diameters_from_file(),
                                           state="readonly")
        self.diameter_entry.config(width=50)
        self.diameter_entry.place(x=10, y=45)

        # Create button to calculate tube compositions
        self.calculate_button = tk.Button(master, text="Ottimizza", command=self.calculate_compositions)
        self.calculate_button.place(x=10, y=70)

        # Label Text
        self.label_text = tk.Label(master, text="d_int\td_est\tlunghezza\tpeso_uni")
        self.label_text.place(x=10, y=20)

        # Create console log
        self.console_log = tk.Text(master)
        self.console_log.config(state="disabled")
        self.console_log.config(width=70, height=18)
        self.console_log.place(x=0, y=100)

    def calculate_compositions(self):
        self.console_log.config(state="normal")
        self.console_log.delete('1.0', tk.END)
        self.console_log.config(state="disabled")
        diameters_string = self.diameter_entry.get()
        diameters_float = tuple(diameters_string.split(" "))
        actual_compo = diameters_float[4]
        diameter = float(diameters_float[1])
        weight = float(diameters_float[3])
        total_actual_hexagon = self.actual_hexagon_test(weight, diameter, self.console_log, actual_compo)
        total_hexagon = self.hexagon_test(weight, diameter, self.console_log)
        total_rectangle = self.rectangle_test(weight, diameter, self.console_log)
        log_msg = f"Numero totale di tubi per il tubo di diametro {diameter} mm:\n"
        log_msg += f"- Forma esagonale: {total_hexagon}"
        if total_actual_hexagon <= total_hexagon:
            log_msg += f" - Incremento del {round(((total_hexagon - total_actual_hexagon) / total_actual_hexagon) * 100, 2)}%\n"
        else:
            log_msg += "\n"
        log_msg += f"- Forma rettangolare: {total_rectangle}"
        if total_actual_hexagon <= total_rectangle:
            log_msg += f" - Incremento del {round(((total_rectangle - total_actual_hexagon) / total_actual_hexagon) * 100, 2)}%\n"
        else:
            log_msg += "\n"
        self.console_log.config(state="normal")
        self.console_log.insert(tk.END, log_msg)
        self.console_log.config(state="disabled")
        #self.show_images("folder_1/images/hex.png", "folder_2/images/rect.png")

    def read_diameters_from_file(self):
            
        df = pd.read_csv("composizione_fasci_cleaned.csv")
        df = df.drop_duplicates(subset=['d_int','d_est', 'lunghezza', 'peso_uni'], keep='first')
        df = df.sort_values(by=['d_est'])
        df = df.drop(['gruppo', 'pz_fascio'], axis=1)
        # Replace ',' with '.' in all columns
        df = df.replace(',', '.', regex=True)
        
        diameters = df[["d_int", "d_est", "lunghezza", "peso_uni", "compo_fascio"]].values.tolist()
        return diameters




    
    def checkfloat(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False
        
    def show_images(self, image_path_1, image_path_2, max_size=(960, 900)):
        # Crea la finestra
        image_window = tk.Toplevel()
        
        # Carica le immagini e ridimensionale se necessario
        image_1 = Image.open(image_path_1)
        image_2 = Image.open(image_path_2)
        image_1.thumbnail(max_size, Image.LANCZOS)
        image_2.thumbnail(max_size, Image.LANCZOS)
        photo_1 = ImageTk.PhotoImage(image_1)
        photo_2 = ImageTk.PhotoImage(image_2)
        
        # Crea due widget Label per visualizzare le immagini affiancate
        label_1 = tk.Label(image_window, image=photo_1)
        label_1.grid(row=0, column=0)
        label_2 = tk.Label(image_window, image=photo_2)
        label_2.grid(row=0, column=1)
        
        # Imposta il titolo della finestra
        image_window.title("Immagini affiancate")
        
        # Avvia il loop dell'interfaccia grafica
        image_window.mainloop()
    

root = tk.Tk()
root.geometry("568x400")
root.resizable(False, False)
app = App(root)
root.mainloop()
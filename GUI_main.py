from folder_1.CalculateDimension import calculate_hexagon_dimensions as cd
from folder_2.CalculateDimension import calculate_rectangle_dimensions as cd2
from folder_3.CalculateDimension import calculate_trapeze_dimensions as cd3
from folder_4.CalculateDimension import calculate_asymHex_dimensions as cd4
import tkinter as tk
from tkinter import ttk
import pandas as pd
from PIL import ImageTk, Image
from folder_2.Draw import draw_rectangles as draw_rects
from folder_1.Draw import draw_hexagons as draw_hexs
from folder_3.Draw import draw_trapezes as draw_traps
from folder_4.Draw import draw_asymHex as draw_asymHexs
import csv
import shared_variable as sv





class App:

    def hexagon_test(self, weight, dest, console_log, total_actual_hexagon):
        max_found = 0;
        best_compo = ""

        if float(dest) >= 30 and float(dest)  <= 40:
            compo_list = ["5-6-7-8-7-6-5", "6-7-8-9-8-7-6", "4-5-6-5-4"]
        elif float(dest)  > 40 and float(dest)  <= 50:
            compo_list = ["6-7-8-9-8-7-6", "5-6-7-8-7-6-5", "4-5-6-5-4"]
        elif float(dest)  > 50 and float(dest)  <= 70:
            compo_list = ["3-4-5-4-3", "4-5-6-5-4"]
        elif float(dest)  > 70:
            compo_list = ["3-4-3"]

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
                    log_msg = f"ERRORE: Composizione {compo_list[i]} scartata per eccesso di peso\n"
                    console_log.config(state="normal")
                    console_log.insert(tk.END, log_msg)
                    console_log.config(state="disabled")
                    return -1
                
        log_msg = "**********************************************************************\n"
        log_msg += f"Composizioni consigliate per il tubo di diametro {dest} mm:\n"
        log_msg += f"\n- Forma esagonale: {best_compo} - Peso: {round(sum([int(i) for i in best_compo.split('-')]) * weight, 2)} Kg - Tubi totali: {max_found}\n"
        log_msg += f" -----> Percentuale incremento numero di tubi: {round((max_found - total_actual_hexagon) / total_actual_hexagon * 100, 2)}%\n"
        console_log.config(state="normal")
        console_log.insert(tk.END, log_msg)
        console_log.config(state="disabled")
        self.save_on_csv_hex(best_hex, "")
        draw_hexs(best_hex, False)

        return max_found
    
    def save_on_csv_hex(self, hexagons, actual):
        with open('coordinate_esagoni' + actual + '.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['x', 'y'])

            for hexagon in hexagons:
                writer.writerow([round((hexagon.origin_x - sv.start_originx)*10, 0), round((hexagon.origin_y - sv.start_originy)*10, 0)])

    def rectangle_test(self, weight, dest, console_log, total_actual_hexagon):

        if float(dest) >= 30 and float(dest)  <= 40: 
            rows = [(6, 7)]
        elif float(dest)  > 40 and float(dest)  <= 60:
            rows = [(6, 7), (4, 5)]
        else:
            rows = [(4, 5)]
            
        log_msg = ""
        max_number = 0
        best_rect = []

        for row in rows:
            
            rects = cd2(float(dest)/20, row[0], row[1], row[1], weight)
            total_rect = len(rects)
            single_rect = (row[1] * int((row[1] / 2)) + row[0] * (row[1] - int((row[1]) / 2)))
            total_tubes = total_rect * single_rect
            log_msg += f"\n- Forma rettangolare: {row} - Peso: {round((row[1] * int((row[1] / 2)) + row[0] * (row[1] - int((row[1]) / 2))) * weight, 2)} Kg - Tubi totali: {total_tubes}\n"
            log_msg += f" -----> Percentuale incremento numero di tubi: {round((total_tubes - total_actual_hexagon) / total_actual_hexagon * 100, 2)}%\n"
            if single_rect * weight < 25:
                if total_tubes > max_number:
                    max_number = total_tubes
                    best_rect = rects
            else:
                log_msg += f"ERRORE: Composizione {row} scartata per eccesso di peso\n"
                console_log.config(state="normal")
                console_log.insert(tk.END, log_msg)
                console_log.config(state="disabled")
                continue

        #log_msg = f"- Forma rettangolare: {best_config} - Peso: {round((best_config[1] * int((best_config[1] / 2)) + best_config[0] * (best_config[1] - int((best_config[1]) / 2))) * weight, 2)} Kg - Tubi totali: {max_number}\n"
        console_log.config(state="normal")
        console_log.insert(tk.END, log_msg)
        console_log.config(state="disabled")  
        self.save_on_csv_rect(best_rect)
        draw_rects(best_rect)
        return max_number
    
    def save_on_csv_rect(self, rectangles):
        """
        Save the center coordinates and rotation information of the given rectangles in a CSV file.

        Args:
        rectangles (list): List of Rectangle objects to be saved in a CSV file.
        rotation (str): String specifying if the rectangles have been rotated or not.

        Returns:
        None
        """
        with open('coordinate_rettangoli.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['x', 'y'])

            for rectangle in rectangles:
                writer.writerow([round(rectangle.center_x - sv.start_originx, 2), round(rectangle.center_y - sv.start_originy, 2)])
    
    def actual_hexagon_test(self, weight, dest, console_log, actual_compo):
        
        if actual_compo == "3-4-5-4":
            return 1
        
        
        rows_array = [float(i) for i in actual_compo.split('-')]
        if(len(rows_array) % 2 == 1):
                n_rows = len(rows_array)
                radius = float(dest)
                radius = radius / 20
                #Call the function to calculate the dimension of the hexagon
                hexagons = cd(radius, n_rows, rows_array, 9999)
                total = len(hexagons)
                single = sum([int(i) for i in actual_compo.split('-')])

        log_msg = "**********************************************************************\n"
        log_msg += f"Composizione attuale per il tubo di diametro {dest} mm:\n"
        log_msg += f"\n- Forma esagonale: {actual_compo} - Peso: {round(sum([int(i) for i in actual_compo.split('-')]) * weight, 2)} Kg\n"
        log_msg += f"- Numero di tubi: {single * total}\n"
        console_log.config(state="normal")
        console_log.insert(tk.END, log_msg)
        console_log.config(state="disabled")
        draw_hexs(hexagons, True)
        self.save_on_csv_hex(hexagons, "_attuale")
        return single*total
    
    def trapezoid_test(self, weight, dest, console_log, total_actual_hexagon):
        
        if float(dest) >= 30 and float(dest)  <= 40:
            compos = ["8-7-6-5", "9-8-7-6"]
        elif float(dest)  > 40 and float(dest)  <= 50:
            compos = ["9-8-7-6", "8-7-6-5", "6-5-4"]
        elif float(dest)  > 50 and float(dest)  <= 70:
            compos = ["5-4-3", "6-5-4"]
        elif float(dest)  > 70:
            compos = ["4-3"]
        
        max = 0
        
        
        for compo in compos:
            single = sum([int(i) for i in compo.split('-')])
            trapezes = cd3(float(dest)/20, compo)
            total = single * len(trapezes)
            if total > max:
                max = total
                best_compo = compo
                best_trapezes = trapezes
        
        log_msg = "\n- Forma trapezoidale: " + best_compo + " - Peso: " + str(round(sum([int(i) for i in best_compo.split('-')]) * weight, 2)) + " Kg - Tubi totali: " + str(max) + "\n"
        log_msg += f" -----> Percentuale incremento numero di tubi: {round((max - total_actual_hexagon) / total_actual_hexagon * 100, 2)}%\n"
        console_log.config(state="normal")
        console_log.insert(tk.END, log_msg)
        console_log.config(state="disabled")       
        self.save_on_csv_trapezoid(best_trapezes)
        draw_traps(best_trapezes)
        
    def asym_hexagon_test(self, weight, dest, console_log, total_actual_hexagon):
        
        compos = ["3-4-5-4"]
        
        
        single = sum([int(i) for i in compos[0].split('-')])            
        hexs = cd4(float(dest)/20, compos[0])
        total = single * len(hexs)
        
        log_msg = "\n- Forma esagonale asimmetrica: " + compos[0] + " - Peso: " + str(round(sum([int(i) for i in compos[0].split('-')]) * weight, 2)) + " Kg - Tubi totali: " + str(total) + "\n"
        log_msg += f" -----> Percentuale incremento numero di tubi: {round((total - total_actual_hexagon) / total_actual_hexagon * 100, 2)}%\n"
        console_log.config(state="normal")
        console_log.insert(tk.END, log_msg)
        console_log.config(state="disabled")
        draw_asymHexs(hexs, False)
        self.save_on_csv_hex(hexs, "_asimmetrico")
            
        
        
    def save_on_csv_trapezoid(self, trapezes):
        
        with open('coordinate_trapezi.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['x', 'y'])

            for trapeze in trapezes:
                writer.writerow([round(trapeze.origin_x - sv.start_originx, 2), round(trapeze.origin_y - sv.start_originy, 2)]) 
        
        

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
        self.calculate_button.place(x=10, y=80)

        # Create button to calculate tube compositions
        self.calculate_button = tk.Button(master, text="Mostra Immagini", command=self.show_images_function)
        self.calculate_button.place(x=130, y=80)

        # Create button to calculate tube compositions
        self.calculate_button = tk.Button(master, text="Ricarica Immagini", command=self.reload_images_function)
        self.calculate_button.place(x=280, y=80)

        

        # Label Text
        self.label_text = tk.Label(master, text="d_int\td_est\tlunghezza\tpeso_uni")
        self.label_text.place(x=10, y=20)

        # Create console log
        self.console_log = tk.Text(master)
        self.console_log.config(state="disabled")
        self.console_log.config(width=100, height=20)
        self.console_log.place(x=0, y=130)

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
        self.hexagon_test(weight, diameter, self.console_log, total_actual_hexagon)
        #self.rectangle_test(weight, diameter, self.console_log, total_actual_hexagon)
        self.trapezoid_test(weight, diameter, self.console_log, total_actual_hexagon)
        self.asym_hexagon_test(weight, diameter, self.console_log, total_actual_hexagon)

    def show_images_function(self):
        self.show_images("images/hex.png", "images/asym.png", "images/hex_actual.png", "images/trap.png")

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
        
    def show_images(self, image_path_1, image_path_2, image_path_3, image_path_4, max_size=(480, 400)):
        
            
        # Crea la finestra
        global new_window
        new_window = tk.Toplevel()
        
        # Carica le immagini e ridimensionale se necessario
        image_1 = Image.open(image_path_1)
        image_2 = Image.open(image_path_2)
        image_3 = Image.open(image_path_3)
        image_4 = Image.open(image_path_4)
        image_1.thumbnail(max_size, Image.BILINEAR)
        image_2.thumbnail(max_size, Image.BILINEAR)
        image_3.thumbnail(max_size, Image.BILINEAR)
        image_4.thumbnail(max_size, Image.BILINEAR)
        photo_1 = ImageTk.PhotoImage(image_1)
        photo_2 = ImageTk.PhotoImage(image_2)
        photo_3 = ImageTk.PhotoImage(image_3)
        photo_4 = ImageTk.PhotoImage(image_4)
        
        # Crea due widget Label per visualizzare le immagini affiancate
        label_1 = tk.Label(new_window, image=photo_1)
        label_1.grid(row=1, column=0)
        label_2 = tk.Label(new_window, image=photo_2)
        label_2.grid(row=1, column=1)
        label_3 = tk.Label(new_window, image=photo_3)
        label_3.grid(row=0, column=0)
        label_4 = tk.Label(new_window, image=photo_4)
        label_4.grid(row=0, column=1)
        
        
        # Imposta il titolo della finestra
        new_window.title("Immagini affiancate")
    
        
        # Avvia il loop dell'interfaccia grafica
        new_window.mainloop()

    def reload_images_function(self):
        self.reload_images("images/hex.png", "images/asym.png", "images/hex_actual.png", "images/trap.png")

    def reload_images(self, image_path_1, image_path_2, image_path_3, image_path_4, max_size=(480, 400)):

        # Carica le immagini e ridimensionale se necessario
        image_1 = Image.open(image_path_1)
        image_2 = Image.open(image_path_2)
        image_3 = Image.open(image_path_3)
        image_4 = Image.open(image_path_4)
        image_1.thumbnail(max_size, Image.BILINEAR)
        image_2.thumbnail(max_size, Image.BILINEAR)
        image_3.thumbnail(max_size, Image.BILINEAR)
        image_4.thumbnail(max_size, Image.BILINEAR)
        photo_1 = ImageTk.PhotoImage(image_1)
        photo_2 = ImageTk.PhotoImage(image_2)
        photo_3 = ImageTk.PhotoImage(image_3)
        photo_4 = ImageTk.PhotoImage(image_4)
        
        # Crea due widget Label per visualizzare le immagini affiancate
        label_1 = tk.Label(new_window, image=photo_1)
        label_1.grid(row=1, column=0)
        label_2 = tk.Label(new_window, image=photo_2)
        label_2.grid(row=1, column=1)
        label_3 = tk.Label(new_window, image=photo_3)
        label_3.grid(row=0, column=0)
        label_4 = tk.Label(new_window, image=photo_4)
        label_4.grid(row=0, column=1)

        # Avvia il loop dell'interfaccia grafica
        new_window.mainloop()


    
root = tk.Tk()
root.geometry("680x500")
root.resizable(False, False)
app = App(root)
root.mainloop()
import tkinter as tk
import CalculateDimension as calc
from PIL import ImageTk, Image


dest = ""
compo = ""

compo_list = ["3-4-5-6-5-4-3", 
              "4-5-6-7-6-5-4", 
              "5-6-7-8-7-6-5", 
              "6-7-8-9-8-7-6", 
              "7-8-9-10-9-8-7", 
              "4-5-6-5-4", 
              "3-4-3",
              "4-5-4", 
              "5-6-5", 
              "2-3-2"]

def checkfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def inject_dest():
    if checkfloat(textbox_dest.get()):
        global dest
        dest = textbox_dest.get()
    else:
        print("Errore: inserire un numero")
        textbox_dest.delete(0, tk.END)
        textbox_dest.insert(0, "Errore: inserire un numero")

def checkcompofloat(string, delimiter = "-"):
    parts = string.split(delimiter)
    for part in parts:
        if not part.isdigit():
            return False
    return True

def inject_compo():
    if checkcompofloat(textbox_compo.get()):
        global compo
        compo = textbox_compo.get()
    else:
        print("Errore: inserire una composizione valida")
        textbox_compo.delete(0, tk.END)
        textbox_compo.insert(0, "Errore: inserire una composizione valida")
    
def load_image():
    # Load the image file
    image = Image.open("./images/test.png")
    image = image.resize((480, 400))  # Resize the image to fit in the window
    photo = ImageTk.PhotoImage(image)
    
    # Set the image on the label widget
    label.configure(image=photo)
    label.image = photo  # Keep a reference to the photo to avoid garbage collection

    

def new_windows():
    inject_dest()
    new_window = tk.Toplevel(window)
    new_window.title("Composizione")
    new_window.geometry("300x300")

    max_found = 0;
    best_compo = "4-5-6-7-6-5-4"

    for i in range(0, len(compo_list)):
        rows_array = [float(i) for i in compo_list[i].split('-')]
        if(len(rows_array) % 2 == 1):
            n_rows = len(rows_array)
            radius = float(dest)
            radius = radius / 20
            #Call the function to calculate the dimension of the hexagon
            total = calc.Calculate(radius, n_rows, rows_array, 9999)
            total_tubes_1 = sum([int(i) for i in compo_list[i].split('-')]) * total
            if total_tubes_1 > max_found:
                max_found = total_tubes_1
                best_compo = compo_list[i]
    label_best_compo = tk.Label(new_window, text="Miglior composizione: " + best_compo).place(x=10, y=30)

def startcomputation():
    inject_dest()
    inject_compo()
    if dest == "" or compo == "":
        print("Errore: inserire tutti i dati")
    else:
        rows_array = [float(i) for i in compo.split('-')]
        if(len(rows_array) % 2 == 1):
            n_rows = len(rows_array)
            radius = float(dest)
            radius = radius / 20

            #Call the function to calculate the dimension of the hexagon
            total = calc.Calculate(radius, n_rows, rows_array, 9999)
            label_total.config(text="Total tubes: " + str(sum([int(i) for i in compo.split('-')]) * total))
            load_image()

window = tk.Tk()
window.title("My GUI")

window.geometry("1000x480")
# Create an empty label to hold the image
label = tk.Label(window)
label.place(x=500, y=0)

label_dest = tk.Label(window, text="Diametro esterno:")
textbox_dest = tk.Entry(window)

label_compo = tk.Label(window, text="Composizione:")
textbox_compo = tk.Entry(window)

button_start = tk.Button(window, text="Start", command=startcomputation)
button_test = tk.Button(window, text="Test", command=new_windows)

window.resizable(False, False)

label_total = tk.Label(window, text="Total tubes: ")
label_total.place(x=10, y=210)


label_dest.place(x=10, y=30)
textbox_dest.place(x=10, y=50)

label_compo.place(x=10, y=100)
textbox_compo.place(x=10, y=120)

button_start.place(x=10, y=150)
button_test.place(x=10, y=180)

window.mainloop()
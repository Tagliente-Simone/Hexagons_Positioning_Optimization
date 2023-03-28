import tkinter as tk
import CalculateDimension as calc
from PIL import ImageTk, Image


dest = ""
compo = ""

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
        print(dest)
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
        print(compo)
    else:
        print("Errore: inserire una composizione valida")
        textbox_compo.delete(0, tk.END)
        textbox_compo.insert(0, "Errore: inserire una composizione valida")
    
def load_image():
    # Load the image file
    image = Image.open("./images/test.png")
    image = image.resize((240, 200))  # Resize the image to fit in the window
    photo = ImageTk.PhotoImage(image)
    
    # Set the image on the label widget
    label.configure(image=photo)
    label.image = photo  # Keep a reference to the photo to avoid garbage collection

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
            calc.Calculate(radius, n_rows, rows_array, 9999)
            load_image()

window = tk.Tk()
window.title("My GUI")

window.geometry("800x400")

# Create an empty label to hold the image
label = tk.Label(window)
label.pack()

label_dest = tk.Label(window, text="Diametro esterno:")
textbox_dest = tk.Entry(window)

label_compo = tk.Label(window, text="Composizione:")
textbox_compo = tk.Entry(window)

button_start = tk.Button(window, text="Start", command=startcomputation)


label_dest.place(x=10, y=30)
textbox_dest.place(x=10, y=50)

label_compo.place(x=10, y=100)
textbox_compo.place(x=10, y=120)

button_start.place(x=10, y=200)

window.mainloop()
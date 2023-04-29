import tkinter as tk
from PIL import ImageTk, Image
import CalculateDimension as calc



def checkfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def inject_rows():
    if textbox_rows.get().isdigit():
        global rows
        rows = textbox_rows.get()
    else:
        print("Errore: inserire un numero")
        textbox_rows.delete(0, tk.END)
        textbox_rows.insert(0, "Errore: inserire un numero")

def inject_dest():
    if checkfloat(textbox_dest.get()):
        global dest
        dest = textbox_dest.get()
    else:
        print("Errore: inserire un numero")
        textbox_dest.delete(0, tk.END)
        textbox_dest.insert(0, "Errore: inserire un numero")

def inject_min_max():
    if checkfloat(textbox_min.get()) and checkfloat(textbox_max.get()):
        global min
        min = textbox_min.get()
        global max
        max = textbox_max.get()

def startcomputation():
    inject_dest()
    inject_rows()
    inject_min_max()


    total_tubes = calc.compute(float(dest)/20, float(min), float(max), rows)
    label_total.config(text="Total tubes: " + str(int(total_tubes)))
    load_image()

def load_image():
    # Load the image file
    image = Image.open("./images/test.png")
    image = image.resize((720, 600))  # Resize the image to fit in the window
    photo = ImageTk.PhotoImage(image)
    
    # Set the image on the label widget
    label.configure(image=photo)
    label.image = photo  # Keep a reference to the photo to avoid garbage collection




window = tk.Tk()
window.title("My GUI")

# Create an empty label to hold the image
label = tk.Label(window)
label.place(x=300, y=80)

window.geometry("1000x700")
window.resizable(False, False)

label_dest = tk.Label(window, text="Diametro esterno:")
textbox_dest = tk.Entry(window)

label_rows = tk.Label(window, text="Numero di file (deve essere dispari):")
textbox_rows = tk.Entry(window)

label_min = tk.Label(window, text="min:")
textbox_min = tk.Entry(window)

label_max = tk.Label(window, text="max:")
textbox_max = tk.Entry(window)

label_dest.place(x=10, y=30)
textbox_dest.place(x=10, y=50)

label_rows.place(x=190, y=30)
textbox_rows.place(x=190, y=50)

label_min.place(x=10, y=100)
textbox_min.place(x=10, y=120)

label_max.place(x=10, y=150)
textbox_max.place(x=10, y=170)

label_total = tk.Label(window, text="Total tubes: ")
label_total.place(x=10, y=250)

button_start = tk.Button(window, text="Start", command=startcomputation)

button_start.place(x=10, y=200)


window.mainloop()
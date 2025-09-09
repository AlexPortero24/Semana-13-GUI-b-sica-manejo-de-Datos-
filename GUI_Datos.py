
# La GUI se realizó con las indicaciones de la tarea

import tkinter as tk
from PIL import Image, ImageTk # Librería necesaria para redimensionar imágenes se requiere descargar la libreria Pillow.
print("Pillow funciona correctamente")
from tkinter import messagebox

# crear la ventana principal
ventana=tk.Tk()
ventana.title("Bienvenido a la Aplicación GUI") # titulo descriptivo
ventana.geometry("700x400") # son las dimensiones  de mi ventana
ventana.config(bg="khaki1") # se añade color a la ventana
ventana.iconbitmap("sapo.ico") # se añade una imagen
ventana.resizable(False, False) # Evita que la ventana sea redimensionable

# Imagen del sapo (más grande)
# ==========================
# Abrir la imagen y redimensionarla
imagen_sapo = Image.open("sapo1.png")  # Imagen con tema de Naruto(Anime)
imagen_sapo = imagen_sapo.resize((100, 100))  # Tamaño de la imagen
imagen_sapo_tk = ImageTk.PhotoImage(imagen_sapo)

# Mostrar la imagen en la ventana
label_sapo = tk.Label(ventana, image=imagen_sapo_tk, bg="khaki1")
label_sapo.place(x=10, y=290) # Aqui se cambia la ubicaion de mi imagen sapo1.png
#--------------------------------------------------------------------------------------

# Texto descriptivo arriba(Etiquetas)
# ==========================
label_texto = tk.Label(ventana, text="Ingrese información para la lista:",
                       font=("Arial", 14, "bold"), bg="pale green" , relief="solid") #bg es el color de fondo
label_texto.place(x=150, y=20)

# ==========================
# Campo de texto
# ==========================
entry_dato = tk.Entry(ventana, width=33, font=("Arial", 12) , relief="solid") # font se usa para la fuente y el tamaño del texto
entry_dato.place(x=150, y=60)

# ==========================
# Lista para mostrar datos
# ==========================
listbox_datos = tk.Listbox(ventana, width=50, height=13 , relief="solid") # relief es el borde solido del cuadro de texto
listbox_datos.place(x=150, y=100)

# ==========================
# Funciones de botones
# ==========================
def agregar():
    dato = entry_dato.get().strip() # obtine el texto del entry
    if dato:
        listbox_datos.insert(tk.END, dato)
        entry_dato.delete(0, tk.END) # se borran los datos del entry
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar un dato.") # si esta vacio muestra la advertencia

def limpiar():
    listbox_datos.delete(0, tk.END) # se borranlos datos del Listbox


# ==========================
# Botones, funciona llamando a la funcion agregar y limpiar al hacer clic
# ==========================
btn_agregar = tk.Button(ventana, text="Agregar", width=12, activebackground="cyan2",activeforeground="green", command=agregar)
btn_agregar.place(x=190, y=320) # Ubicación del botón de agregar

btn_limpiar = tk.Button(ventana, text="Limpiar", width=12, activebackground="cyan2", command=limpiar)
btn_limpiar.place(x=320, y=320) # Ubicación del botón de limpiar


# su funcion es mantener la ventana abierta
ventana.mainloop()
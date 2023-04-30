import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

print (" Librerias Leidas")

ventana= tk.Tk()
ventana.title("Interfaz Gráfica")
ventana.geometry("400x500")

#Crear los comandos
def imagen ():
    img=Image.open("C:/Users\claud\OneDrive - Universidad Tecnologica de Jalisco\OneDrive\Documentos\MAESTRIA INTELIGENCIA ARTIFICIAL\MIA PYTHON VSC\GUI\imagenes\Paisajes\descarga.gif")
    new_img=img.resize((300,256))
    render=ImageTk.PhotoImage(new_img)
    #Llamar imagen
    img1=Label(ventana, image=render)
    img1.image=render
    img1.place(x=10,y=30)
def mensaje():
    salir= messagebox.askquestion("Salir", "¿Desea salir de la interfaz?")
    if salir == 'yes':
        ventana.quit()
        ventana.detroy()

#Crear botones
boton=tk.Button(ventana, command=imagen, text="Abrir Imagen", height=2,width=20 )
boton.place(x=100, y=350)

boton1=tk.Button(ventana, command=mensaje, text="Salir", height=2,width=20 )
boton1.place(x=100, y=450)



ventana.mainloop()











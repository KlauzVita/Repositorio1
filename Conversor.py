from tkinter import *
from tkinter import ttk

def calcular(*args):
    #Agregar robustes con try y except, pass
    try:
    #metros.set(pies.get()) # Se borra print(pies.get()) #.get() para que obtenga el valor que tiene la variable de la linea 5
        resultado=float(pies.get())*.3048 #cadena a flotante
        metros.set(resultado)
    except ValueError:
        pass #Bloque de código en blanco


raiz= Tk()
raiz.title("Pies a metros") #Titulo de la raiz

marcoPrincipal= ttk.Frame(raiz, padding="15 15 15 15") #paddin agrega margenes al diseño en pixeles #creado el objeto hay que vincular y vamos a ponerle el widget de quien va depender (raiz)
# Si lo ejecutas se ve igual, porque no le hemos dado una posición.
marcoPrincipal.grid(column=0, row=0)    #metodo grid caracteristicas de posinamiento.
#Si ejecutamos solo abre una ventana pequeña porque no tiene tamaño.
#Agregar campo Entry nos permite agregar una linea de texto

pies=StringVar()
metros=StringVar()
#Entry usa una sola linea como texto de entrada.
txtPies= ttk.Entry(marcoPrincipal, width=7, textvariable=pies, justify="center")#para colocar posición necesitamos .grid, textvariable=pies asignamos
txtPies.grid(column=1, row=0)

#Objetos ánonimos
#Diseño stiky alineación interna de cada elemento, path es un margen
#padx margen en el eje y 
ttk.Label(marcoPrincipal, text="pies").grid(column=2, row=0) #puede estar dentro del argumento pady o sust por for hijo
ttk.Label(marcoPrincipal, text="equivalentes a").grid(column=0, row=1)
ttk.Label(marcoPrincipal, textvariable=metros).grid(column=1, row=1)
ttk.Label(marcoPrincipal, text="metros").grid(column=2, row=1)
ttk.Button(marcoPrincipal, text="Calcular", command=calcular).grid(column=2, row=2) #todos los bottones tinen comand

for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=5, pady=5)
#poner foco, para dar funcionalidad usabilidad
txtPies.focus()

#agregar funcianalidad enter para que de el resultado .bind con comandos de las teclas
raiz.bind("<Return>", calcular)


raiz.mainloop()




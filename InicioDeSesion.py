from tkinter import *
from tkinter import ttk

raiz= Tk()
raiz.title("Inicio de Sesión")

marcoPrincipal=ttk.Frame(raiz, padding="20 20 20 20")
marcoPrincipal.grid(column=0, row=0)

Usuario=StringVar()
Contraseña=StringVar()

txtUsuario= ttk.Entry(marcoPrincipal, textvariable=Usuario, justify="left")
txtUsuario.grid(column=4, row=1)

txtContraseña= ttk.Entry(marcoPrincipal, textvariable=Contraseña)
txtContraseña.grid(column=4, row=2)

ttk.Label(marcoPrincipal, text="Usuario:").grid(column=0, row=1, sticky=E)
ttk.Label(marcoPrincipal, text="Contraseña:").grid(column=0, row=2)

ttk.Button(marcoPrincipal, text="Ingresar").grid(column=4, row=3, sticky=E)

for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=5, pady=5)

txtUsuario.focus()

raiz.bind("<Return>", )

raiz.mainloop()
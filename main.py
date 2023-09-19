import tkinter as tk
import random

#Definir Variables
VarProteina="Pollo Asado"
VarBase="Arroz"
VarCarbohidrato="Papa"
VarExtra=""
VarEnsalada="Lechuga y Tomate"
VarPostre="Chocorramo"
VarJugo="Jugo de lulo"
VarEXTRAAgua="Agua"


# Opciones de almuerzo predefinidas
categorias = {
    "Proteína": VarProteina,
    "Base": VarBase,
    "Carbohidrato": VarCarbohidrato,
    "Extra": VarExtra,
    "Ensalada": VarEnsalada,
    "Postre": VarPostre,
    "Bebida": VarJugo,
    "EXTRAAgua": VarEXTRAAgua
}

# Función para generar un menú de almuerzo
def generar_menu():
    menu = {}
    for categoria, opciones in categorias.items():
        if categoria in seleccion:
            opcion = opciones
            menu[categoria] = opcion
    return menu

# Función para mostrar el menú en la interfaz
def mostrar_menu():
    menu_generado = generar_menu()
    resultado.config(text="Menú Generado:\n")
    for categoria, opcion in menu_generado.items():
        resultado.config(text=resultado.cget("text") + f"{categoria}: {opcion}\n")

# Función para manejar la selección del usuario
def actualizar_seleccion():
    seleccion.clear()
    for categoria, var in categorias_vars.items():
        if var.get() == 1:
            seleccion.add(categoria)

# Configuración de la interfaz gráfica
app = tk.Tk()
app.title("Generador de Menú de Almuerzo")

categorias_vars = {}
seleccion = set()

for categoria in categorias:
    categorias_vars[categoria] = tk.IntVar()
    tk.Checkbutton(app, text=categoria, variable=categorias_vars[categoria], command=actualizar_seleccion).pack()

generar_button = tk.Button(app, text="Generar Menú", command=mostrar_menu)
generar_button.pack()

resultado = tk.Label(app, text="", justify="left")
resultado.pack()

app.mainloop()

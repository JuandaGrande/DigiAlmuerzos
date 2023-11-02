import pandas as pd
import qrcode
import json
import datetime
from PIL import Image

# Paso 1: Leer la base de datos de Excel
def leer_menu(fecha_actual):
    try:
        menu_df = pd.read_excel('menu.xlsx')
        opciones_almuerzo = menu_df[menu_df['Fecha'] == fecha_actual]
        return opciones_almuerzo
    except FileNotFoundError:
        print("El archivo 'menu.xlsx' no se encontró. Asegúrate de que el archivo existe y tiene el formato adecuado.")
        return None

# Paso 2: Permitir al usuario seleccionar alimentos y cantidades
def seleccionar_alimentos(opciones_almuerzo):
    if opciones_almuerzo is None:
        return None
    
    for index, row in opciones_almuerzo.iterrows():
        print(f"Opciones de almuerzo para hoy {row['Fecha']}: ")
        print(f"1. Sopa: {row['Sopa']}")
        print(f"2. Proteico: {row['Proteico']}")
        print(f"3. Cereal: {row['Cereal']}")
        print(f"4. Tubérculo: {row['Tubérculo']}")
        print(f"5. Vegetariano: {row['Vegetariano']}")
    
    alimentos_seleccionados = {}
    
    while True:
        opcion = input("Seleccione un alimento por número (o escriba 'terminar' para finalizar): ").strip().lower()
        if opcion == 'terminar':
            break
        
        if opcion.isdigit():
            opcion_num = int(opcion)
            if opcion_num >= 1 and opcion_num <= 5:
                if opcion_num==1:
                    StringComida=row['Sopa']
                if opcion_num==2:
                    StringComida=row['Proteico']
                if opcion_num==3:
                    StringComida=row['Cereal']
                if opcion_num==4:
                    StringComida=row['Tubérculo']
                if opcion_num==5:
                    StringComida=row['Vegetariano']

                cantidad = (input(f"Ingrese la cantidad de porciones de {StringComida} (Escribe 'ayuda' si no conoces las porciones): "))
                if cantidad == "ayuda":
                    im=Image.open("Porcionamiento.png")
                    im.show()
                    cantidad = (input(f"Ingrese la cantidad de porciones de {StringComida}: "))
                cantidad=int(cantidad)
                columna = opciones_almuerzo.columns[opcion_num]
                if cantidad >5:
                    cantidad=5
                elif cantidad <1:
                    cantidad=1
                alimentos_seleccionados[columna] = cantidad
            else:
                print("Número de opción no válido. Intente nuevamente.")
        else:
            print("Entrada no válida. Intente nuevamente.")
    
    return alimentos_seleccionados

# Paso 3: Generar un código QR con las selecciones del usuario
def generar_qr(selecciones):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    selecciones_json = json.dumps(selecciones)
    
    qr.add_data(selecciones_json)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("codigo_qr.png")

try:
    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now().strftime("%b-%d")

    # Paso 1: Leer el menú para la fecha actual
    opciones_almuerzo = leer_menu(fecha_actual)

    # Paso 2: Permitir al usuario seleccionar alimentos y cantidades
    alimentos_seleccionados = seleccionar_alimentos(opciones_almuerzo)

    if alimentos_seleccionados:
        # Paso 3: Generar un código QR con las selecciones del usuario
        generar_qr(alimentos_seleccionados)

        print("Código QR generado con las selecciones de alimentos.")
        print(f"Alimentos seleccionados: {alimentos_seleccionados}")
    else:
        print("No se pudieron seleccionar alimentos.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
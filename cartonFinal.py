import random

def generar_carton():
    # Crear una matriz de 3 filas y 9 columnas inicializada con None
    carton = [[None for _ in range(9)] for _ in range(3)]
    
    # Generar los números para cada columna dentro de los rangos especificados
    numeros_por_columna = {
        0: list(range(1, 9)),    # Columna 1: números del 1 al 9
        1: list(range(10, 19)),   # Columna 2: números del 10 al 19
        2: list(range(20, 29)),   # Columna 3: números del 20 al 29
        3: list(range(30, 39)),   # Columna 4: números del 30 al 39
        4: list(range(40, 49)),   # Columna 5: números del 40 al 49
        5: list(range(50, 59)),   # Columna 6: números del 50 al 59
        6: list(range(60, 69)),   # Columna 7: números del 60 al 69
        7: list(range(70, 79)),   # Columna 8: números del 70 al 79
        8: list(range(80, 89)),   # Columna 9: números del 80 al 89
    }
    
    # Barajar los números de cada columna para garantizar la aleatoriedad
    for columna in range(9):
        random.shuffle(numeros_por_columna[columna])
    
    # Distribuir los números en el cartón
    for fila in range(3):
        # Seleccionar 5 columnas al azar para poner números en esta fila
        columnas_a_usar = random.sample(range(9), 5)
        for columna in columnas_a_usar:
            # Tomar el primer número disponible de la columna correspondiente
            carton[fila][columna] = numeros_por_columna[columna].pop(0)

    # Reemplazar None por ' ' para representar los espacios en blanco
    for fila in range(3):
        for columna in range(9):
            if carton[fila][columna] is None:
                carton[fila][columna] = ' '
    
    return carton

def imprimir_carton(carton):
    # Imprimir el cartón en un formato legible
    for fila in carton:
        # Convertir cada número a string y ajustarlo a 2 caracteres de ancho
        print(' '.join(str(num).rjust(2, ' ') for num in fila))

# Generar e imprimir por consola un cartón de bingo
#carton = generar_carton()
#imprimir_carton(carton)



from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_carton_pdf(carton, filename):
    c = canvas.Canvas(filename, pagesize=letter)

    # Definir el tamaño y la posición del cartón en la página
    x_offset = 50
    y_offset = 750
    cell_width = 50
    cell_height = 50


    # Dibujar los bordes de las celdas
    c.setStrokeColorRGB(0, 0, 0)  # Color negro
    for fila in range(4):
        y = y_offset - fila * cell_height
        c.line(x_offset, y, x_offset + 9 * cell_width, y)  # Línea horizontal
    for columna in range(10):
        x = x_offset + columna * cell_width
        c.line(x, y_offset, x, y_offset - 3 * cell_height)  # Línea vertical

    # Escribir los números en el cartón
    c.setFont("Helvetica", 12)
    for fila, numeros in enumerate(carton):
        for columna, numero in enumerate(numeros):
            x = x_offset + columna * cell_width + cell_width / 2
            y = y_offset - fila * cell_height - cell_height / 2
            c.drawCentredString(x, y, str(numero))

    c.save()


# Generar un unico carton y guardarlo en un archivo PDF
#carton = generar_carton()
#generar_carton_pdf(carton, "carton_con_bordes.pdf")
#imprimir_carton(carton)


# Generar varios cartones y guardarlos en un archivo PDF
def generar_y_guardar_cartones_pdf(cantidad):
    for i in range(cantidad):
        carton = generar_carton()
        imprimir_carton(carton)
        filename = f"carton_{i + 1}.pdf"
        generar_carton_pdf(carton, filename)
        print(f"Cartón {i + 1} generado y guardado en {filename}")

# Generar e imprimir la cantidad cartones de lotería que quiera el usuario
cantidad_cartones = int(input("Ingrese la cantidad de cartones que desea generar: "))
generar_y_guardar_cartones_pdf(cantidad_cartones)
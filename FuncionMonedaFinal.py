import random

def lanzar_moneda():
    # Función que simula el lanzamiento de una moneda
    return random.choice(['cara', 'cruz'])

def juego_monedas():
    puntos = 0
    contador_cara = 0
    contador_cruz = 0

    while True:
        resultado = lanzar_moneda()
        print(f"Lanzamiento: {resultado}")

        # Restar 1 punto por cada lanzamiento
        puntos -= 1

        # Contar caras y cruces consecutivas
        if resultado == 'cara':
            contador_cara += 1
            contador_cruz = 0
        else:
            contador_cruz += 1
            contador_cara = 0

        # Verificar si hay 3 caras o cruces consecutivas
        if contador_cara == 3 or contador_cruz == 3:
            puntos += 8  # Ganar 8 puntos si se obtienen 3 caras o 3 cruces consecutivas
            break

    # Mensaje final basado en los puntos totales
    if puntos > 0:
        print(f"Juego terminado. Felicitaciones, has ganado con {puntos} puntos.")
    else:
        print(f"Juego terminado. Lo siento, has perdido y tienes {puntos} puntos.")

    return puntos

# Ejecutar el juego
juego_monedas()

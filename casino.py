import random

def girar_rodillo():
    # Función que simula el giro de un rodillo
    valores = ['A', 'B', 'C', 'D','E']
    return random.choice(valores)

def agregar_puntos():
    # Función que permite al jugador agregar más puntos
    while True:
        try:
            puntos_adicionales = int(input("¿Cuántos puntos adicionales quieres agregar? (mínimo 1 punto) "))
            if puntos_adicionales < 1:
                print("Debes ingresar un número mayor o igual a 1.")
            else:
                return puntos_adicionales
        except ValueError:
            print("Por favor, ingresa un número válido.")

def maquina_tragamonedas():
    # Preguntar al jugador cuántos puntos quiere empezar y validar la entrada
    while True:
        try:
            puntos = int(input("¿Cuántos puntos iniciales quieres tener? (mínimo 1 punto) "))
            if puntos < 1:
                print("Debes ingresar un número mayor o igual a 1.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    while True:
        input("Presiona Enter para girar los rodillos...")

        # Girar los nueve rodillos
        rodillos = [girar_rodillo() for _ in range(9)]

        # Imprimir los resultados
        print("---------------------------------")
        for i in range(3):
            print(f"Rodillo {i+1}: {rodillos[i*3]} | {rodillos[i*3+1]} | {rodillos[i*3+2]}")

        # Restar 1 punto por cada tirada
        puntos -= 1


        # Verificar si los valores de las fila 1 son iguales
        if rodillos[0] == rodillos[1] == rodillos[2]:
            if rodillos[1] == 'A':
                puntos += 10
                print("¡Felicidades! Has ganado 10 puntos en la primera fila.")
            elif rodillos[1] == 'B':
                puntos += 7
                print("¡Felicidades! Has ganado 7 puntos en la primera fila.")
            elif rodillos[1] == 'C':
                puntos += 5
                print("¡Felicidades! Has ganado 5 puntos en la primera fila.")
            elif rodillos[1] == 'D':
                puntos += 2
                print("¡Felicidades! Has ganado 2 puntos en la primera fila.")
            elif rodillos[1] == 'E':
                puntos += 0           

        # Verificar si los valores de las fila 2 son iguales
        if rodillos[3] == rodillos[4] == rodillos[5]:
            if rodillos[4] == 'A':
                puntos += 10
                print("¡Felicidades! Has ganado 10 puntos en la segunda fila.")
            elif rodillos[4] == 'B':
                puntos += 7
                print("¡Felicidades! Has ganado 7 puntos en la segunda fila.")
            elif rodillos[4] == 'C':
                puntos += 5
                print("¡Felicidades! Has ganado 5 puntos en la segunda fila.")
            elif rodillos[4] == 'D':
                puntos += 2
                print("¡Felicidades! Has ganado 2 puntos en la segunda fila.")
            elif rodillos[4] == 'E':
                puntos += 0                  

        # Verificar si los valores de las fila 3 son iguales
        if rodillos[6] == rodillos[7] == rodillos[8]:
            if rodillos[7] == 'A':
                puntos += 10
                print("¡Felicidades! Has ganado 10 puntos en la tercera fila.")
            elif rodillos[7] == 'B':
                puntos += 7
                print("¡Felicidades! Has ganado 7 puntos en la tercera fila.")
            elif rodillos[7] == 'C':
                puntos += 5
                print("¡Felicidades! Has ganado 5 puntos en la tercera fila.")
            elif rodillos[7] == 'D':
                puntos += 2
                print("¡Felicidades! Has ganado 2 puntos en la tercera fila.")
            elif rodillos[7] == 'E':
                puntos += 0   

        # Verificar si los valores de los rodillos en la diagonal Izquierda-derecha son iguales
        if rodillos[0] == rodillos[4] == rodillos[8]:
            if rodillos[4] == 'A':
                puntos += 10
                print("¡Felicidades! Has ganado 10 puntos en la diagonal izquierda.")
            elif rodillos[4] == 'B':
                puntos += 7
                print("¡Felicidades! Has ganado 7 puntos en la diagonal izquierda.")
            elif rodillos[4] == 'C':
                puntos += 5
                print("¡Felicidades! Has ganado 5 puntos en la diagonal izquierda.")
            elif rodillos[4] == 'D':
                puntos += 2
                print("¡Felicidades! Has ganado 2 puntos en la diagonal izquierda.")
            elif rodillos[4] == 'E':
                puntos += 0   

        # Verificar si los valores de los rodillos en la diagonal derecha-Izquierda son iguales
        if rodillos[2] == rodillos[4] == rodillos[6]:
            if rodillos[4] == 'A':
                puntos += 10
                print("¡Felicidades! Has ganado 10 puntos en la diagonal derecha.")
            elif rodillos[4] == 'B':
                puntos += 7
                print("¡Felicidades! Has ganado 7 puntos en la diagonal derecha.")
            elif rodillos[4] == 'C':
                puntos += 5
                print("¡Felicidades! Has ganado 5 puntos en la diagonal derecha.")
            elif rodillos[4] == 'D':
                puntos += 2
                print("¡Felicidades! Has ganado 2 puntos en la diagonal derecha.")
            elif rodillos[4] == 'E':
                puntos += 0   

        # Verificar si el jugador tiene puntos suficientes para seguir jugando
        if puntos <= 0:
            print("---------------------------------")
            print("Lo siento, no tienes suficientes puntos para continuar jugando.")
            print("---------------------------------")
            agregar_mas_puntos = input("¿Deseas agregar más puntos para seguir jugando? (s/n): ").lower()
            print("---------------------------------")
            if agregar_mas_puntos == 's':
                puntos += agregar_puntos()
            else:
                break

        # Preguntar al jugador si desea seguir jugando
        print("---------------------------------")
        print(f"Puntos totales: {puntos}")
        continuar = input("¿Deseas seguir jugando? (s/n): ").lower()
        print("---------------------------------")
        if continuar != 's':
            print(f"Puntos totales: {puntos}")
            break

# Ejecutar la máquina tragamonedas
maquina_tragamonedas()

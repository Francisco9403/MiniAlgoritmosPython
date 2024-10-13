# Matriz de distancias
distancias = [
    [0, 3139.54, 2376.064],  # Depósito
    [3095.6649999999995, 0, 2929.8579999999997],   # Casa 1
    [2537.3189999999995, 3068.8469999999998, 0],  # Casa 2
]

def vecino_mas_proximo(distancias):
    num_casas = len(distancias)
    visitado = [False] * num_casas  # Marca todas las casas como no visitadas
    ruta = []
    casa_actual = 0  # Comenzamos en el Depósito (índice 0)
    ruta.append(casa_actual)
    visitado[casa_actual] = True
    distancia_total = 0

    for _ in range(num_casas - 1):
        menor_distancia = float('inf')
        siguiente_casa = None

        # Buscar la casa no visitada más cercana
        for casa in range(num_casas):
            if not visitado[casa] and distancias[casa_actual][casa] < menor_distancia:
                menor_distancia = distancias[casa_actual][casa]
                siguiente_casa = casa

        # Visitamos la casa más cercana
        ruta.append(siguiente_casa)
        visitado[siguiente_casa] = True
        distancia_total += menor_distancia
        casa_actual = siguiente_casa

    # Regresar al Depósito
    distancia_total += distancias[casa_actual][0]
    ruta.append(0)

    return ruta, distancia_total

ruta_optima, distancia_optima = vecino_mas_proximo(distancias)
print(f"Ruta óptima: {ruta_optima}")
print(f"Distancia total: {distancia_optima} cuadras")

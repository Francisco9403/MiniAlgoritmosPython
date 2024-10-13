import osmnx as ox
import networkx as nx

# Pedir al usuario que ingrese la ciudad y el país (ejemplo: 'Junín, Argentina')
lugar = input("Introduce la ciudad y el país (por ejemplo, 'Junín, Argentina'): ")
print("-" * 50) 
# Descargar la red de calles de la ciudad especificada por el usuario
grafo = ox.graph_from_place(lugar, network_type='drive')


# Función para pedir varias direcciones al usuario y almacenarlas en una lista
def obtener_direcciones():
    direcciones = []
    while True:
        # Pedir una dirección al usuario o 'fin' para finalizar
        direccion = input("Introduce una dirección (o escribe 'fin' para terminar): ")
        if direccion.lower() == 'fin':  # Si el usuario escribe 'fin', termina la entrada
            break
        print("-" * 50) 
        direcciones.append(direccion)  # Agregar la dirección a la lista
    return direcciones  # Devolver la lista de direcciones

# Obtener las direcciones proporcionadas por el usuario
direcciones_usuario = obtener_direcciones()

# Convertir las direcciones ingresadas en coordenadas geográficas (geocodificación)
ubicaciones = [ox.geocode(direccion) for direccion in direcciones_usuario]

# Obtener el nodo más cercano a cada ubicación (en la red de calles) usando las coordenadas (longitud, latitud)
nodos_casas = [ox.distance.nearest_nodes(grafo, latlong[1], latlong[0]) for latlong in ubicaciones]

# Calcular la matriz de distancias entre cada par de ubicaciones utilizando el grafo de calles
distancias = []
for i in range(len(nodos_casas)):  # Iterar sobre las ubicaciones (nodos)
    fila = []
    for j in range(len(nodos_casas)):
        if i != j:  # Si no es la misma ubicación, calcular la distancia más corta
            distancia = nx.shortest_path_length(grafo, nodos_casas[i], nodos_casas[j], weight='length')
            fila.append(distancia)
        else:
            fila.append(0)  # Si es la misma ubicación, la distancia es 0
    distancias.append(fila)  # Agregar la fila de distancias a la matriz



# Función para resolver el Problema del Viajante (TSP) usando la heurística del vecino más cercano
def tsp_vecino_mas_cercano(distancias, limite):
    num_nodos = len(distancias)  # Número total de nodos (ubicaciones)
    visitado = [False] * num_nodos  # Lista para marcar las ubicaciones ya visitadas
    recorridos = []  # Lista para almacenar los recorridos por segmentos de "limite" casas
    distancia_total = 0  # Variable para acumular la distancia total recorrida
    inicio = 0  # Comenzar el recorrido desde el nodo 0

    # Mientras haya ubicaciones no visitadas
    while not all(visitado):
        tour = [inicio]  # Iniciar el recorrido desde el nodo inicial
        visitado[inicio] = True  # Marcar el nodo inicial como visitado
        distancia_segmento = 0  # Inicializar la distancia recorrida en este segmento
        contador = 0  # Contador de casas visitadas en el segmento actual

        # Mientras no se haya alcanzado el límite de casas y queden casas por visitar
        while contador < limite and not all(visitado):
            actual = tour[-1]  # La última ubicación visitada en el tour
            siguiente = None
            distancia_minima = float('inf')  # Inicializar con un valor infinito para encontrar el vecino más cercano

            # Buscar el vecino más cercano no visitado
            for i in range(num_nodos):
                if not visitado[i] and distancias[actual][i] < distancia_minima:
                    siguiente = i  # Actualizar el siguiente nodo como el más cercano
                    distancia_minima = distancias[actual][i]

            # Si se encuentra un vecino no visitado
            if siguiente is not None:
                tour.append(siguiente)  # Añadir el vecino más cercano al recorrido
                visitado[siguiente] = True  # Marcarlo como visitado
                distancia_segmento += distancia_minima  # Sumar la distancia recorrida
                contador += 1  # Incrementar el contador de casas visitadas

        # Volver al punto de inicio después de cada segmento
        distancia_segmento += distancias[tour[-1]][inicio]  # Agregar la distancia de regreso al inicio
        tour.append(inicio)  # Agregar el inicio al final del tour

        # Almacenar el recorrido y la distancia del segmento
        recorridos.append((tour, distancia_segmento))
        distancia_total += distancia_segmento  # Sumar la distancia del segmento a la distancia total

    return recorridos, distancia_total  # Devolver los recorridos por segmentos y la distancia total

# Pedir al usuario que ingrese el número máximo de casas (diarios) por recorrido
print("-" * 50)  # Separador
limite_diarios = int(input("Introduce el número máximo de casas por segmento: "))

# Obtener los recorridos por segmentos y la distancia total recorrida
recorridos_segmentados, distancia_total = tsp_vecino_mas_cercano(distancias, limite_diarios)


print("-" * 50)  # Separador
# Mostrar la matriz de distancias entre las ubicaciones
print("\nMatriz de distancias entre ubicaciones:\n")
for fila in distancias:
    print(fila)
print("\n" + "-" * 50)  # Separador


# Mostrar los recorridos segmentados con la distancia de cada segmento
print(f"\nRecorridos por segmentos (máximo de {limite_diarios} casas por segmento):\n")
for idx, (tour, distancia_segmento) in enumerate(recorridos_segmentados):
    print(f"Segmento {idx + 1} (Distancia: {distancia_segmento / 1000:.2f} km):")
    for i in tour:
        print(f"[Casa {i}, ({direcciones_usuario[i]})]")
    print("-" * 50)  # Separador entre segmentos

# Mostrar la distancia total recorrida en kilómetros
print(f"\nDistancia total recorrida: {distancia_total / 1000:.2f} Kilómetros")
print("-" * 50)  # Separador final


# Mostrar el grafo (opcional)
ox.plot_graph(grafo)






r"""
Convertir direcciones (si las tienes) a coordenadas (geocodificación)
ubicaciones = [

    error(502 mentros)  6600 metros(Distancia real)   6098 metros(Estimarcion del programa)  
    ox.geocode("418 Siria, Junin, Buenos Aires"),   #Deposito
    ox.geocode("27 Newbery, Junin, Buenos Aires"), 
    ox.geocode("1500 Belgrano, Junin, Buenos Aires"),

    error(960 metros)  9500 metros (Distancia real)  8540 metros(Estimarcion del programa)  
    ox.geocode("76, Doctor Calp, Eusebio Marcilla, Junín, Partido de Junín, Buenos Aires, B6000, Argentina"),   #Deposito
    ox.geocode("1022, Presidente Quintana, Libertad, Junín, Partido de Junín, Buenos Aires, B6000, Argentina"),
    ox.geocode("77, Dorrego, El Picaflor, Junín, Partido de Junín, Buenos Aires, 6000, Argentina"), 
]
"""

r"""
PS C:\Users\usuario\Desktop> python "Alternativa.py"
Introduce la ciudad y el país (por ejemplo, 'Junín, Argentina'): Junín, Argentina
Introduce una dirección (o escribe 'fin' para terminar): 418 Siria, Junin, Buenos Aires
Introduce una dirección (o escribe 'fin' para terminar): 1500 Belgrano, Junin, Buenos Aires
Introduce una dirección (o escribe 'fin' para terminar): 27 Newbery, Junin, Buenos Aires
Introduce una dirección (o escribe 'fin' para terminar): 1386, Italia, Uocra, Junín, Partido de Junín, Buenos Aires, B6000, Argentina
Introduce una dirección (o escribe 'fin' para terminar): 77, Dorrego, El Picaflor, Junín, Partido de Junín, Buenos Aires, 6000, Argentina
Introduce una dirección (o escribe 'fin' para terminar): fin
--------------------------------------------------

Matriz de distancias entre ubicaciones:

[0, 2202.2509999999993, 1690.5590000000002, 1216.7439999999997, 2314.91]
[2199.132, 0, 2233.627, 987.3159999999999, 3760.936000000001]
[1864.275, 2209.22, 0, 2456.767999999999, 1558.053]
[1216.736, 987.8219999999999, 2489.029, 0, 3531.6459999999997]
[2318.3830000000003, 3737.682, 1909.6050000000002, 3533.986, 0]

--------------------------------------------------
Introduce el número máximo de casas por segmento: 2

Recorridos por segmentos (máximo de 2 casas por segmento):

Segmento 1 (Distancia: 4.40 km):
[Casa 0, (418 Siria, Junin, Buenos Aires)]
[Casa 3, (1386, Italia, Uocra, Junín, Partido de Junín, Buenos Aires, B6000, Argentina)]
[Casa 1, (1500 Belgrano, Junin, Buenos Aires)]
[Casa 0, (418 Siria, Junin, Buenos Aires)]
--------------------------------------------------
Segmento 2 (Distancia: 5.57 km):
[Casa 0, (418 Siria, Junin, Buenos Aires)]
[Casa 2, (27 Newbery, Junin, Buenos Aires)]
[Casa 4, (77, Dorrego, El Picaflor, Junín, Partido de Junín, Buenos Aires, 6000, Argentina)]
[Casa 0, (418 Siria, Junin, Buenos Aires)]
--------------------------------------------------

Distancia total recorrida: 9.97 Kilómetros
--------------------------------------------------
PS C:\Users\usuario\Desktop> 
"""
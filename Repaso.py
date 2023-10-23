class Grafo:
    def __init__(self):
        self.nodos = set()
        self.arcos = {}
    
    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)
        if nodo not in self.arcos:
            self.arcos[nodo] = []

    def agregar_arco(self, origen, destino):
        if origen in self.nodos and destino in self.nodos:
            self.arcos[origen].append(destino)
        else:
            raise ValueError("Los nodos de origen y destino deben estar en el grafo.")
        
        # Crear un grafo para representar archivos y dependencias
grafo = Grafo()

def vecindad_izquierda(grafo, nodo):
    vecinos_izquierdos = []

    for origen, destinos in grafo.arcos.items():
        if nodo in destinos:
            vecinos_izquierdos.append(origen)

    return vecinos_izquierdos
def vecindad_ideal_izquierda(grafo, nodo):
    nodos_presentes = grafo.nodos  # Obtiene todos los nodos presentes en el grafo

    vecinos_ideales_izquierdos = []

    for posible_predecesor in nodos_presentes:
        if posible_predecesor != nodo:
            vecinos_ideales_izquierdos.append(posible_predecesor)

    return vecinos_ideales_izquierdos

def crear_grafo_desde_diccionario(diccionario):
    grafo = Grafo()  # Crea una instancia de la clase Grafo
    # Agrega nodos y arcos al grafo basados en el diccionario
    for archivo, dependencias in diccionario.items():
        grafo.agregar_nodo(archivo)
        for destino in dependencias:
            grafo.agregar_nodo(destino)
            grafo.agregar_arco(archivo, destino)
    return grafo  # Devuelve el grafo creado

def main():
    grafo = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["B"]
}
    mi_grafo = crear_grafo_desde_diccionario(grafo)
    nodo_de_interes = "A"
    vecindad_izq = vecindad_izquierda(mi_grafo, nodo_de_interes)
    vecindad_ideal_izq = vecindad_ideal_izquierda(mi_grafo, nodo_de_interes)
    print(f"Vecindad Izquierda de {nodo_de_interes}: {vecindad_izq}")
    print(f"Vecindad Izquierda  ideal {nodo_de_interes}: {vecindad_ideal_izq}")


main()
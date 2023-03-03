import random
import time

# logica busque "normal"
def búsqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# logica busqueda binaria
def búsqueda_binaria(lista, objetivo, lim_inf=None, lim_sup=None):
    if lim_inf is None:
        lim_inf = 0  # inicio de la lista
    if lim_sup is None:
        lim_sup = len(lista) - 1  # final de la lista

    # lista no ordenada
    if lim_sup < lim_inf:
        return -1

    # con // me da la division truncada 7 / 2 = 3.5 , 7 // 2 = 3
    punto_medio = (lim_inf + lim_sup) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return búsqueda_binaria(lista, objetivo, lim_inf, punto_medio - 1)
    else:
        return búsqueda_binaria(lista, objetivo, punto_medio + 1, lim_sup)


# para que se pueda llamar a esta funcion como primario no desde otro archivo py
if __name__ == '__main__':
    tamaño = 20000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))

    lista_ordenada = sorted(list(conjunto_inicial))

    # mido el tiempo de búsqueda ingenua.
    inicio = time.time()
    for objetivo in lista_ordenada:
        búsqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de búsqueda ingenua: {fin - inicio} segundos.")

    # Mido el tiempo de búsqueda binaria.
    inicio = time.time()
    for objetivo in lista_ordenada:
        búsqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de búsqueda binaria: {fin - inicio} segundos.")

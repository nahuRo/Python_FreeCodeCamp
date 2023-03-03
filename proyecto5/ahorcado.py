from palabras import palabras_array
from diagrama import vidas_diccionario_visual

import random
import string


def traer_palabra(listado):
    palabra = random.choice(listado)
    return palabra.upper()


def ahorcado():
    print("======================")
    print("Bienvenido al juego")
    print("======================")

    palabra = traer_palabra(palabras_array)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    # trae todo el abecedario sin incluir la ñ
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(
            f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)} ")  # uno todos los elementos con ' ', en este caso
        # mostrar el estado actual de la palabra
        palabra_lista = [
            letra if letra in letras_adivinadas else '-' for letra in palabra]
        # se lee: agrega/imprimi la letra si la letra se encuentra en "apalabras_adivinadas" sino agrega/imprimi '-' por cada letra en "palabra"

        # muestro el estado del diagrama
        print(vidas_diccionario_visual[vidas])
        # muestro el estado de la palabra
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        # si resto conjuntos se restan y devuelven la diferencias
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # si la letra esta en la palabra, quito esa letra del conjunto de letras pendientes por adivinar sino le resto una vida al usuario
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(" ")
            else:
                vidas -= 1
                print(f"\nTu letra {letra_usuario} no esta en la palabra")
        # si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Elige otra letra")
        else:
            print("\nEsta letra no es valida")

    # El juego llega a esta linea cuando se adivinaron todas la letras o cuando se quedo sin vidas
    if vidas == 0:
        print(f"Ahorcado! Perdiste. La palabra era {palabra}")
    else:
        print(f"Ganaste! Adivinaste la palabra {palabra}")


ahorcado()

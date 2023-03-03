import random


def adivina_el_numero(x):
    print("======================")
    print("Bienvenido al juego")
    print("======================")
    print("Tu meta es adivinar el numero generado por la computadora")

    numero_random = random.randint(1, x)

    prediccion = 0
    intentos = 0

    while prediccion != numero_random:
        prediccion = int(input(f"Ingresa un valor entre 1 y {x}: "))

        if prediccion > numero_random:
            print("El numero a adivinar es mas chico")
        elif prediccion < numero_random:
            print("El numero a adivinar es mas grande")

        intentos = intentos + 1

    print(f"""
    Felicitaciones adivinaste el número {numero_random}!
    Cantidad de intentos: {intentos}
    """)


adivina_el_numero(10)

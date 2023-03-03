import random


def adivina_el_num_computadora(x):
    print("======================")
    print("Bienvenido al juego")
    print("======================")

    print(f"Pensa un numero entre 1 y {x} que la computadora debe adivinar")

    lim_inf = 1
    lim_sup = x

    intentos = 0

    respuesta = ""

    while respuesta != "c":

        if lim_inf != lim_sup:
            prediccion = random.randint(lim_inf, lim_sup)
        else:
            prediccion = lim_inf

        respuesta = input(f"""
        prediccion de la computadora --> {prediccion}
        - Ingresa a si la respuesta es un numero menor
        - Ingresa b si la respuesta es un numero mayor
        - Ingresa c si la respuesta es correcta
        """).lower()

        if respuesta == "a":
            lim_sup = prediccion - 1
        elif respuesta == "b":
            lim_inf = prediccion + 1

        intentos = intentos + 1

    print(f"""
    La computadora logro adivinar tu numero -> {respuesta}
    en {intentos}
    """)


adivina_el_num_computadora(10)

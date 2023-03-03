import random


def game():
    print("======================")
    print("Bienvenido al juego")
    print("======================")

    computadora = random.choice(["pi", "pa", "ti"])

    player = input("""
    Ingresa:
    pi --> piedra
    pa --> papel
    ti --> tijera
    \n""")

    if player == computadora:
        print(f"Empate! A mbos jugadores eligieron {player}")
    elif (player == "pi" and computadora == "ti") or (player == "pa" and computadora == "pi") or (player == "ti" and computadora == "pa"):
        print(f"""
        *** Gano el jugador ***
        jugador --> {player}
        computadora --> {computadora}
        """)
    else:
        print(f"""
        *** Gano la computadora ***
            jugador --> {player}
            computadora --> {computadora}
        """)


game()

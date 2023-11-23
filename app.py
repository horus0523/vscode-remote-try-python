#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


def jugar_rock_paper_scissors():
    elementos = ["rock", "paper", "scissors"]
    puntuacion_jugador = 0
    puntuacion_oponente = 0

    while True:
        print("Elige una opción: rock, paper o scissors")
        opcion_jugador = input().lower()

        if opcion_jugador not in elementos:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

        opcion_oponente = random.choice(elementos)
        print("El oponente elige:", opcion_oponente)

        if opcion_jugador == opcion_oponente:
            print("Empate!")
        elif (opcion_jugador == "rock" and opcion_oponente == "scissors") or \
             (opcion_jugador == "scissors" and opcion_oponente == "paper") or \
             (opcion_jugador == "paper" and opcion_oponente == "rock"):
            print("¡Ganaste!")
            puntuacion_jugador += 1
        else:
            print("Perdiste.")
            puntuacion_oponente += 1

        print("Puntuación: Jugador", puntuacion_jugador, "- Oponente", puntuacion_oponente)

        print("¿Quieres jugar de nuevo? (s/n)")
        respuesta = input().lower()
        if respuesta != "s":
            break

    print("¡Gracias por jugar!")

jugar_rock_paper_scissors()

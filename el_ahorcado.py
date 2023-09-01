import random

import string

from palabras import palabras



def obtener_palabra_valida(lista_palabras):

    # Seleccionar una palabra al azar de la lista
    # de palabras validas
    palabra = random.choice(palabras)

    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()


def ahorcado():

    print("-" * 50)
    print("¡ Bienvenido(a) al juego del Ahorcado !")
    print("-" * 50)

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7
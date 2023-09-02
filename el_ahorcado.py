import random

import string

from palabras import palabras

from ahorcado_diagramas import vidas_diccionario_visual


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

    while len(letras_por_adivinar) > 0 and vidas > 0:

        # Letras adivinadas
        # " ".join({"A", "B". "C"}) -> "A, B, C"

        print(f"Te quedan {vidas} vidas y has usado estas letras:"
              f"{' '.join(letras_adivinadas)} ")

        # Mostrar el estado actual de la palabra

        palabra_lista = [letra if letra in letras_adivinadas
                         else "-" for letra in palabra] # list comprehension una forma de escribir las lista
                                                        # en una sola linea
        # Mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        # Mostrar las letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        # Si la letra escogida por el usuario est+a en el
        # abecedario y no esta en el conjunto de letras
        # que ya se han ingresado, se añade la letra al conjunto
        # de letras ingresadas. 
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)



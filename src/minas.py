"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

Guia de numeros del tablero:
0 = Sin descubrir
1 = hay una bomba
2 = descubierto
3 = bandera

"""

import random

def pideMina():
    l_mina = []
    mina = input("Ingresa coordenadas (fila, columna):")
    mina = mina.split(",")
    for posicion in mina:
        posicion = int(posicion)-1
        l_mina.append(posicion)
    t_mina = tuple(l_mina)
    return t_mina

def generaMinas(numero_de_minas):
    minas = set()
    for numero_mina in range(numero_de_minas):
        fila = random.randint(0, 7)
        columna = random.randint(0, 7)
        mina = (fila, columna)
        minas.add(mina)
    return minas

def generarTablero():
    tablero = []
    for fila in range(8):
        tablero.append([0, 0, 0, 0 ,0, 0, 0, 0])
    return tablero

def inicializaTablero():
    tablero = generarTablero()
    minas = generaMinas(10)
    for mina in minas:
        tablero[mina[0]][mina[1]] = 1
    return tablero

def compruebaMina(tablero, posicion):
    if tablero[posicion[0]][posicion[1]] == 1:
        return True
    else:
        return False
            
def imprimirTablero(tablero):
    print(end=" ")
    for numero in range(1, len(tablero)+1):
        print(numero, end=" ")
    print("\n")
    for numero in range(1, len(tablero)+1):
        print(numero , end=" ")
        for celda in tablero[numero-1]:
            if celda == 2:
                print(" ", end=" ")
            else:
                print("·", end=" ")
        print("\n")
        
        
def jugar():
    """
    Esta función ejecuta el juego.

    """
    tablero = inicializaTablero()
    imprimirTablero(tablero)
        
    entrada = input("""Elige una acción:
                    1. Revelar celda
                    2. Marcar celda
                    3. Salir""")
    while entrada != "3":
        if entrada == "1":
            mina = pideMina()
            if compruebaMina(tablero, mina):
                quit()
            else:
                tablero[mina[0]][mina[1]] = 2
                imprimirTablero(tablero)

if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    
    jugar()

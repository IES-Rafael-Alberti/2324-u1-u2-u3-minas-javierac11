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

def descubrirCeldasAdyacentes(tablero, posicion): 
   # posicion_tablero = tablero[posicion[0]][posicion[1]]
    
    for fila in range(-1, 2):
        for columna in range(-1, 2):
            if tablero[posicion[0]+fila][posicion[1]+columna] == 0:
                tablero[posicion[0]+fila][posicion[1]+columna] = 2

def pidePosicion():
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
    print(end="\t")
    for numero in range(1, len(tablero)+1):
        print(numero, end="\t")
    print("\n")
    for numero in range(1, len(tablero)+1):
        print(numero , end="\t")
        for celda in tablero[numero-1]:
            if celda == 2:
                print(" ", end="\t")
            else:
                print("·", end="\t")
        print("\n")
        
        
def jugar():
    """
    Esta función ejecuta el juego.

    """
    tablero = inicializaTablero()
    imprimirTablero(tablero)
        
    entrada = input("Elige una acción:\n1. Revelar celda\n2. Marcar celda\n3. Salir")
    while entrada != "3":
            mina = pidePosicion()
            if compruebaMina(tablero, mina):
                print("Has perdido")
                quit()
            else:
                tablero[mina[0]][mina[1]] = 2
                descubrirCeldasAdyacentes(tablero, mina)
                imprimirTablero(tablero)
                entrada = input("Elige una acción:\n1. Revelar celda\n2. Marcar celda\n3. Salir")
                
if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    
    jugar()

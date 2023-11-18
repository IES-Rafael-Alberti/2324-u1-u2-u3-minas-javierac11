"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.
"""

import random

def descubrirCeldasAdyacentes(tablero, posicion, descubiertas): 
   # posicion_tablero = tablero[posicion[0]][posicion[1]]
    try:
        for fila in range(-1, 2):
            for columna in range(-1, 2):
                if tablero[posicion[0]+fila][posicion[1]+columna] == 0:
                    descubiertas.add((posicion[0]+fila, posicion[1]+columna))
    except IndexError:
        pass
    
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
        esta_mina = True
        while esta_mina:
            fila = random.randint(0, 7)
            columna = random.randint(0, 7)
            mina = (fila, columna)
            if mina not in minas:
                minas.add(mina)
                esta_mina = False
    return minas

def generarTablero():
    tablero = []
    for fila in range(8):
        tablero.append([0, 0, 0, 0 ,0, 0, 0, 0])
    return tablero
"""
def inicializaTablero():
    tablero = generarTablero()
    minas = generaMinas(10)
    for mina in minas:
        tablero[mina[0]][mina[1]] = 1
    return tablero
"""
def compruebaMina(minas, posicion):
    if posicion in minas:
        return True
    else:
        return False
"""
def imprimirTablero(tablero, minas):
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
        print("\n")"""
        
def imprimirTablero(tablero, minas, descubiertos, banderas):
    print(end="\t")
    for numero in range(1, len(tablero)+1):
        print(numero, end="\t")
    print("\n")
    for fila in range(1, len(tablero)+1):
        print(fila, end="\t")
        for celda in range(1, len(tablero)+1):
            if (fila, celda) in banderas:
                print("F", end="\t")
            elif (fila, celda) in minas:
                print("·", end="\t")
            elif (fila, celda) in descubiertos:
                print(" ", end="\t")
            
            else: 
                print("·", end="\t")
        print("\n")
        
def compruebaGanar(minas, banderas, descubiertos, tablero: list):
    tablero_set = set()
    if minas == banderas:
        
        for fila in range(len(tablero)):
            for celda in range(len(tablero)):
                tablero_set.add((fila, celda))
        tablero_set = tablero_set - minas
        if tablero_set == descubiertos:
            return True
    return False

def jugar():
    """
    Esta función ejecuta el juego.

    """
#    tablero_visible = generarTablero()
    descubiertas = set()
    tablero = generarTablero()
    minas = generaMinas(10)
    banderas = []
    imprimirTablero(tablero, minas, descubiertas, banderas)
        
    entrada = input("Elige una acción:\n1. Revelar celda\n2. Marcar celda\n3. Salir")
    while entrada != "3":
        if entrada == "1":    
            posicion = pidePosicion()
            if compruebaMina(minas, posicion):
                print("Has perdido")
                return False
            else:
                descubiertas.add((posicion[0]+1, posicion[1]+1))
                descubrirCeldasAdyacentes(tablero, (posicion[0]+1, posicion[1]+1), descubiertas)
                imprimirTablero(tablero, minas, descubiertas, banderas)
                if compruebaGanar(minas, banderas, descubiertas, tablero):
                    print("has ganado")
                    return True
                entrada = input("Elige una acción:\n1. Revelar celda\n2. Marcar celda\n3. Salir")
        if entrada == "2":
            posicion = pidePosicion()
            banderas.append((posicion[0]+1, posicion[1]+1))
            imprimirTablero(tablero, minas, descubiertas, banderas)
            if compruebaGanar(minas, banderas, descubiertas, tablero):
                print("has ganado")
                return True
            entrada = input("Elige una acción:\n1. Revelar celda\n2. Marcar celda\n3. Salir")
        else:
            print("Opcion invalida")
            entrada = input("Elige una acción:\n1. Revelar celda\n2. Marcar celda\n3. Salir")
                
                
if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()

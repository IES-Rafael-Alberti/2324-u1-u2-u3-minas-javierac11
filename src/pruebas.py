import random

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

print(generaMinas(10))
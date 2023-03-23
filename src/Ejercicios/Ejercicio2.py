"""
Realiza el  código para calcular el determinante de una matriz cuadrada de [3 x 3], regla de Sarrus de forma recursiva y de forma iterativa.
"""

# FORMA RECURSIVA

import copy

def determinante_manera_recursiva(Matriz, total=0):
    """
    Función para el cálculo recursivo del determinante de cualquier matriz cuadrada.
    """
    tamaño = list(range(len(Matriz))) # tamaño que tendrá la matriz

    if len(Matriz) == 2 and len(Matriz[0]) == 2: # Si la matriz es de 2x2
        val = Matriz[0][0] * Matriz[1][1] - Matriz[1][0] * Matriz[0][1] # Calculamos el determinante
        return val # Devolvemos el determinante

    for fc in tamaño: # Para cada columna de la matriz ...
        As = copy.deepcopy(Matriz)  # haz una copia, y ...
        As = As[1:] # ... elimina la primera fila
        height = len(As) # Altura de la matriz

        for i in range(height):  # Para cada fila de la submatriz ...
            As[i] = As[i][0:fc] + As[i][fc+1:] # elimina la columna de la matriz

        sign = (-1) ** (fc % 2)  # Alternar signos para el multiplicador de la submatriz
        sub_det = determinante_manera_recursiva(As)  # Pasar submatriz recursivamente
        total += sign * Matriz[0][fc] * sub_det # Total de todos los retornos de la recursión

    return total # Devolvemos el determinante

# Creamos una matriz cuadrada de tamaño nxn
n = 3
Matriz = [[0] * n for i in range(n)]

# Rellenamos la matriz con valores aleatorios
import random

for i in range(n):
    for j in range(n):
        Matriz[i][j] = random.randint(-10, 10)

# Imprimimos la matriz
print("Matriz: ")
for i in range(n):
    for j in range(n):
        print(Matriz[i][j], end=" ")
    print()

# Si quiero calcular una matriz concreta
# Matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

# Calculamos el determinante de la matriz
determinante = determinante_manera_recursiva(Matriz)
print("Resultado del determinante de la matriz ramdom calculado de manera recursiva: ", determinante)




# FORMA ITERATIVA
Matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
size = len(Matriz1) # El tamaño de la Matriz1
print("Matriz1: ", Matriz1)

aux = 0 # aux es la variable que almacena el resultado del determinante
for o in range(0, size): # o es la variable que recorre las filas de la matriz
    temp = 1 # temp es la variable que almacena el resultado de la multiplicación de los elementos de la fila
    k = o # k es la variable que recorre las columnas de la matriz
    for i in range(0, size): # i es la variable que recorre las filas de la matriz
        temp *= Matriz1[i][k] # Multiplicar los elementos de la fila
        k += 1  # Incrementar k en 1
        if k == size: # Si k es igual al tamaño de la matriz
            k = 0 # k es igual a 0
    aux += temp # Sumar el resultado de la multiplicación de los elementos de la fila

for o in range(size-1, -1, -1): # o es la variable que recorre las filas de la matriz
    temp = 1 # temp es la variable que almacena el resultado de la multiplicación de los elementos de la fila
    k = o # k es la variable que recorre las columnas de la matriz
    for i in range(0, size): # i es la variable que recorre las filas de la matriz
        temp *= Matriz1[i][k] # Multiplicar los elementos de la fila
        k -= 1 # Decrementar k en 1
        if k == -1: # Si k es igual a -1
            k = size - 1 # k es igual al tamaño de la matriz - 1
    aux -= temp # Restar el resultado de la multiplicación de los elementos de la fila

print("El determinante de la matriz1 calculado de manera iterativa es: ", aux)
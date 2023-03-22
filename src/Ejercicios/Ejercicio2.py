"""
Realiza el  código para calcular el determinante de una matriz cuadrada de [3 x 3], regla de Sarrus de forma recursiva y de forma iterativa.
"""


# Forma recursiva





# Forma iterativa
M1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Definir una matriz cuadrada de tamaño 3x3
m = len(M1)# Definir m como el tamaño de la matriz M1

aux = 0 # aux es la variable que almacena el resultado del determinante
for o in range(0, m): # o es la variable que recorre las filas de la matriz
    temp = 1 # temp es la variable que almacena el resultado de la multiplicación de los elementos de la fila
    k = o # k es la variable que recorre las columnas de la matriz
    for i in range(0, m): # i es la variable que recorre las filas de la matriz
        temp *= M1[i][k] # Multiplicar los elementos de la fila
        k += 1  # Incrementar k en 1
        if k == m: # Si k es igual al tamaño de la matriz
            k = 0 # k es igual a 0
    aux += temp # Sumar el resultado de la multiplicación de los elementos de la fila

    for o in range(m-1, -1, -1): # o es la variable que recorre las filas de la matriz
        temp = 1 # temp es la variable que almacena el resultado de la multiplicación de los elementos de la fila
        k = o # k es la variable que recorre las columnas de la matriz
        for i in range(0, m): # i es la variable que recorre las filas de la matriz
            temp *= M1[i][k] # Multiplicar los elementos de la fila
            k -= 1 # Decrementar k en 1
            if k == -1: # Si k es igual a -1
                k = m - 1 # k es igual al tamaño de la matriz - 1
        aux -= temp # Restar el resultado de la multiplicación de los elementos de la fila

print("El determinante de la matriz calculada de manera iterativa es: ", aux)
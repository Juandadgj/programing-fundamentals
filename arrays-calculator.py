# -*- coding: utf-8 -*-
import numpy

def printArray(array):
    for i in array:             #Definimos la funcion
        for j in i:             #para imprimir las matrices
            print(j, end=' ')
        print("")

print("VAMOS A OPERAR MATRICES\n")
print("Las opciones son las siguientes:\n"\
      "1. Suma de vectores.\n2. Resta de vectores.\n"\
      "3. Multiplicacion de un vector por un escalar.\n"\
      "4. Multiplicacion de dos vectores.\n5. Suma de matrices\n"\
      "6. Resta de matrices.\n7. Multiplicacion de matrices por un escalar.\n"\
      "8. Multiplicacion de dos matrices.\n9. Crear matriz identidad.")

loop = True
while loop == True:

    opt = int(input("¿Qué opcion desea realizar?: "))
    if opt == 1 or opt == 2 or opt == 4:
        vect1 = []                          #Definimos los vectores
        vect2 = []                          #antes de operarlos
        vect3 = []
        len1 = int(input("Digite la longitud del primer vector: "))
        len2 = int(input("Digite la longitud del segundo vector: "))
        if len1 != len2:
            print("LOS VECTORES NO TIENEN LA MISMA DIMENSION.")
            break
        print("PRIMER VECTOR")
        for i in range(len1):
            vect1.append(float(input(f"Digite un elemento en el primer vector, {i+1}: ")))
        print("SEGUNGO VECTOR")
        for j in range(len2):
            vect2.append(float(input(f"Dijite un elemento en el segundo vector, {j+1}: ")))
    
    elif opt == 5 or opt == 6 or opt == 8:
        print("PRIMERA MATRIZ")
        row1 = int(input("Digite las filas de la primera matriz: "))
        col1 = int(input("Digite las columnas de la primera matriz: "))
        print("SEGUNDA MATRIZ")
        row2 = int(input("Digite las filas de la segunda matriz: "))
        col2 = int(input("Digite las columnas de la segunda matriz: "))
        if opt == 5 or opt == 6:
            if row1 != row2 or col1 != col2:
                print("LAS MATRICES NO TIENEN LA MISMA DIMENSION.")
                break
        array1 = numpy.zeros((row1, col1))      #Definimos las matrices
        array2 = numpy.zeros((row2, col2))      #antes de operarlas
        print("PRIMERA MATRIZ")
        for m in range(row1):
            for n in range(col1):
                array1[m, n] = float(input(f"Digite un elemento en la primera matriz. {m+1}, {n+1}: "))
        print("SEGUNDA MATRIZ")
        for m in range(row2):
            for n in range(col2):
                array2[m, n] = float(input(f"Digite un elemento en la segunda matriz. {m+1}, {n+1}: "))
    
    if opt == 1:
        for n in range(len1):
            vect3.append(vect1[n] + vect2[n])
        print("Su vector resultante es: ", vect3)
    
    elif opt == 2:
        for n in range(len1):
            vect3.append(vect1[n] - vect2[n])
        print("Su vector resultante es: ", vect3)
    
    elif opt == 3:
        vect1 = []
        len1 = int(input("Digite la longitud del vector: "))
        for n in range(len1):
            vect1.append(float(input(f"Dijite un elemento en {n+1}: ")))
        sca = float(input("Digite el escalar: "))
        for m in range(len1):
            vect1[m] = vect1[m] * sca
        print("Su vector resultante es: ", vect1)
    
    elif opt == 4:
        mul = 0
        for n in range(len1):
            mul += vect1[n] * vect2[n]
        print("Su determinante es: ", mul)
    
    elif opt == 5:
        array3 = numpy.zeros((row1, col1))
        for m in range(row1):
            for n in range(col1):
                array3[m, n] = array1[m, n] + array2[m, n]
        print("Su matriz resultante es: \n")
        printArray(array3)
    
    elif opt == 6:
        array3 = numpy.zeros((row1, col1))
        for m in range(row1):
            for n in range(col1):
                array3[m, n] = array1[m, n] - array2[m, n]
        print("Su matriz resultante es: \n")
        printArray(array3)
    
    elif opt == 7:
        row1 = int(input("Digite las filas de la matriz: "))
        col1 = int(input("Digite las columnas de la matriz: "))
        array1 = numpy.zeros((row1, col1))
        for m in range(row1):
            for n in range(col1):
                array1[m, n] = int(input(f"Digite un en la primera matriz, {m+1}, {n+1}: "))
        sca = sca = float(input("Digite el escalar: "))
        for m in range(row1):
            for n in range(col1):
                array1[m, n] = array1[m, n] * sca
        print("Su matriz resultante es: ")
        printArray(array1)
    
    elif opt == 8:
        array3 = numpy.zeros((row1, col2))
        if row2 != col1:
            print("No se pueden multiplicar las matrices.")
        else:
            for i in range(row1):
                for j in range(col2):
                    for k in range(row2):
                        array3[i, j] += array1[i, k] * array2[k, j]
        print("Su matriz resultante es: \n")
        printArray(array3)
    
    elif opt == 9:
        len1 = int(input("¿De qué longitud desea la matriz? "))
        array1 = numpy.zeros((len1, len1))
        for m in range(len1):
            for n in range(len1):
                if m == n:
                    array1[m, n] = 1
                else:
                    array1[m, n] = 0
        printArray(array1)

    loopSta = input("¿Desea realizar otra consulta? SI/NO: ")
    if loopSta.upper() == "SI":
        loop = True                 #Se valida si se quiere
    elif loopSta.upper() == "NO":   #realizar otra consulta
        loop = False
    else:
        print("Opcion no valida.")
        break
    
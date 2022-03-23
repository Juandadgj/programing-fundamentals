# -*- coding: utf-8 -*-

import math

# Esta vez pedimos disculpas por el
# spanglish, estamos trabajando en eso.

def factorial(n):
    if n == 0 or n == 1:        # Funcion para hallar el factorial
        resultado = 1
    elif n > 1:
        resultado = n * factorial(n - 1)
    return resultado

def radian(x):
    xI = x.split("/")
    if len(xI) > 1:
        xF = float(xI[0]) / float(xI[1]) #Funcion para convertir la entrada
    elif len(xI) <= 1:                    #a radianes en las funciones trigonometricas
        xF = float(xI[0])
    return xF

def sin(x):
    sen = 0
    for i in range(10):
        dividendo = (x*3.14159265359)**(2*i + 1)
        divisor = factorial(2*i + 1)
        sumatoria = dividendo / divisor     #Funcion seno en Tayor
        if i % 2 == 0:
            sen += sumatoria
        else:
            sen -= sumatoria
    return round(sen, 10)

def cos(x):
    cos = 0
    for i in range(10):
        dividendo = (x*3.14159265359)**(2*i)
        divisor = factorial(2*i)
        sumatoria = dividendo / divisor     #Funcion coseno en Taylor
        if i % 2 == 0:
            cos += sumatoria
        else:
            cos -= sumatoria
    return round(cos, 10)

def ln(x):
    ln = 0
    for i in range(10):             #Funcion logaritmo natural en Taylor
        multiplo1 = 1 / (2*i + 1)
        multiplo2 = ((x - 1) / (x + 1))**(2*i + 1)
        sumatoria = 2 * (multiplo1 * multiplo2)
        ln += sumatoria
    return ln

print("VAMOS A CALCULAR PUNTOS EN LAS FUNCIONES EXPONENCIALES, LOGARITMICAS Y TRIGONOMETRICAS")
print("Podrás calcular tus funciones con las siguientes opciones: \n"\
        "1: Seno \n"\
        "2: Coseno \n"\
        "3: Tangente \n"\
        "4: Cosecante \n"\
        "5: Secante \n"\
        "6: Cotangente \n"\
        "7: Exponencial \n"\
        "8: Logaritmo natural \n"\
        "9: Logaritmo decimal \n")

loop = True

while loop == True:

    opt = input("Digite la opcion de funcion que desea realizar: ")

    if opt != "7" and opt != "8" and opt != "9":
        xPre = input("Digite su angulo a evaluar -puedes escribirlo como fraccion tambien si es en radianes (1/3)-: ")
        optUni = input("Digite 1 si está en radianes, 2 si está en grados: ")
        if optUni == "1":
            x = radian(xPre)
        elif optUni == "2":
            if float(xPre) < 0 or float(xPre) > 360:    #Pido los datos que aplican para
                print("Opcion no valida.")              #las funciones trigonometricas
                break
            x = float(xPre) / 180
        else:
            print("Opcion no valida.")
            break

    elif opt == "7" or opt == "8" or opt == "9":
        x = float(input("Digite su X a evaluar: "))     #Pido los datos para las demas funciones
        if x < 0:
            print("Opcion no valida.")
            break

    if opt == "1":
        print(f"El seno de su X con serie de Taylor es: {sin(x)}")
        print(f"El seno de su X con funcion math es: {math.sin(x)}")

    elif opt == "2":
        print(f"El coseno de su X con serie de Taylor es: {cos(x)}")

    elif opt == "3":
        if cos(x) != 0:
            tan = sin(x) / cos(x)
            print(f"La tangente de su X con serie de Taylor es: {tan}")
        else:
            print("La tangente de su X no está determinada.")

    elif opt == "4":
        if sin(x) != 0:
            csc = 1 / sin(x)
            print(f"La cosecante de su X es: {csc}")
        else:
            print("La cosecante de su X no está determinada.")

    elif opt == "5":
        if cos(x) != 0:
            sec = 1 / cos(x)
            print(f"La secante de su X es de: {sec}")
        else:
            print("La secante de su X no está determinada.")

    elif opt == "6":
        if cos(x) != 0:
            tan = sin(x) / cos(x)
            if tan != 0:
                cot = 1 / tan
                print(f"La cotangente de X es: {cot}")
            else:
                print("La cotangente de su X no está determinada.")
        else:
            print("La cotangente de su X no está determinada.")

    elif opt == "7":
        e = 0
        for i in range(10):
            sumatoria = (x**i) / (factorial(i))
            e += sumatoria
        print(f"Su funcion exponencial en X es: {e}")

    elif opt == "8":
        print(f"El logaritmo natural de su X es: {ln(x)}")

    elif opt == "9":
        ld = ln(x) / 2.30259
        print(f"El logaritmo decimal de su X es: {ld}")

    else:
        print("Opcion no valida.")
        break

    loopSta = input("¿Desea realizar otra consulta? SI/NO: ")
    if loopSta.upper() == "SI":
        loop == True
    elif loopSta.upper() == "NO":       #Se pregunta al usuario por otra consulta
        loop = False
    else:
        print("Opcion no valida.")
        break

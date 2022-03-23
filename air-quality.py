# -*- coding: utf-8 -*-
import numpy

TMR = numpy.zeros((5, 12))
ICA = numpy.zeros((5, 12))

TMR[0,0]=24
TMR[0,1]=23
TMR[0,2]=13
TMR[0,3]=14
TMR[0,4]=20
TMR[0,5]=21
TMR[0,6]=16
TMR[0,7]=23
TMR[0,8]=15
TMR[0,9]=10
TMR[0,10]=17
TMR[0,11]=24
TMR[1,0]=22
TMR[1,1]=13
TMR[1,2]=16
TMR[1,3]=20
TMR[1,4]=16
TMR[1,5]=13
TMR[1,6]=24
TMR[1,7]=15
TMR[1,8]=19
TMR[1,9]=24
TMR[1,10]=19
TMR[1,11]=10
TMR[2,0]=28
TMR[2,1]=23
TMR[2,2]=21
TMR[2,3]=22
TMR[2,4]=33
TMR[2,5]=31
TMR[2,6]=31
TMR[2,7]=29
TMR[2,8]=25
TMR[2,9]=20
TMR[2,10]=22
TMR[2,11]=22
TMR[3,0]=31
TMR[3,1]=25
TMR[3,2]=25
TMR[3,3]=23
TMR[3,4]=20
TMR[3,5]=23
TMR[3,6]=28
TMR[3,7]=27
TMR[3,8]=32
TMR[3,9]=28
TMR[3,10]=32
TMR[3,11]=22
TMR[4,0]=21
TMR[4,1]=26
TMR[4,2]=28
TMR[4,3]=26
TMR[4,4]=25
TMR[4,5]=28
TMR[4,6]=24
TMR[4,7]=20
TMR[4,8]=21
TMR[4,9]=23
TMR[4,10]=24
TMR[4,11]=25

ICA[0,0]=49
ICA[0,1]=38
ICA[0,2]=9
ICA[0,3]=51
ICA[0,4]=57
ICA[0,5]=148
ICA[0,6]=156
ICA[0,7]=184
ICA[0,8]=103
ICA[0,9]=42
ICA[0,10]=65
ICA[0,11]=73
ICA[1,0]=79
ICA[1,1]=86
ICA[1,2]=38
ICA[1,3]=78
ICA[1,4]=93
ICA[1,5]=70
ICA[1,6]=140
ICA[1,7]=189
ICA[1,8]=150
ICA[1,9]=97
ICA[1,10]=54
ICA[1,11]=58
ICA[2,0]=50
ICA[2,1]=5
ICA[2,2]=10
ICA[2,3]=82
ICA[2,4]=70
ICA[2,5]=115
ICA[2,6]=114
ICA[2,7]=132
ICA[2,8]=155
ICA[2,9]=78
ICA[2,10]=55
ICA[2,11]=12
ICA[3,0]=84
ICA[3,1]=45
ICA[3,2]=28
ICA[3,3]=3
ICA[3,4]=59
ICA[3,5]=59
ICA[3,6]=78
ICA[3,7]=8
ICA[3,8]=59
ICA[3,9]=80
ICA[3,10]=41
ICA[3,11]=37
ICA[4,0]=6
ICA[4,1]=27
ICA[4,2]=20
ICA[4,3]=57
ICA[4,4]=145
ICA[4,5]=110
ICA[4,6]=180
ICA[4,7]=182
ICA[4,8]=175
ICA[4,9]=27
ICA[4,10]=28
ICA[4,11]=14

REG = ["Amazonía","Andina","Caribe","Orinoquía","Pacífico"]

CICA = [
    ["Verde","Buena"],
    ["Amarillo","Moderada"],
    ["Naranja","Dañina para grupos sensibles"],
    ["Rojo","Dañino"],
    ["Purpura","Alto grado de toxicidad"]
]

def proAnuTem(reg):
    prom = 0
    for m in range(12):
        prom = prom + TMR[reg-1,m]
    return prom / 12

def proAnuICA(reg):
    prom = 0
    for m in range(12):
        prom = prom + ICA[reg-1,m]
    return prom / 12

'''
def printArray(array):
    for i in array:
        for j in i:
            print(j, end=' ')
        print("")
'''

print("CAMBIO CLIMATICO EN COLOMBIA\n")
print("Las opciones son las siguientes:\n"\
    "1. Promedio de temperaturas por trimestre\n"\
    "2. Temperatura maxima y minima por region\n"\
    "3. Consulta en que momentos se dió un indice de contaminación\n"\
    "4. Calidad del aire promedio por región.\n"\
    "5. Promedio de temperaturas anuales en todas las regiones\n"\
    "6. Mostrar la temperatura o ICA en una region y mes.\n"\
    "7. Indicar meses con la peor calidad del aire.\n"\
    "8. Que regiones tuvieron un indicador por debajo del promedio.")
loop = True

while loop == True:

    opt = int(input("¿Qué opcion desea realizar?: "))

    if opt == 1:

        reg = int(input("1. Amazonía   2. Andina   3. Caribe  4. Orinoquía   5. Pacífico   Digite una opción: "))
        tri = int(input("Digite el trimistre: "))
        ind = int(input("Digite 1 si desea consultar la temperatura, 2 si es e ICA: "))
        if ind == 1:
            m = (tri - 1) * 3
            n = m + 3
            pro = 0
            while m < n:
                pro = pro + int(TMR[reg-1,m])
                m = m + 1
            pro = pro / 3
            print(f"El promedio de temperatura en el/la {REG[reg-1]} en el trimestre {tri} es de: {pro}")
        elif ind == 2:
            m = (tri - 1) * 3
            n = m + 3
            pro = 0
            while m < n:
                pro = pro + int(TMR[reg,m])
                m = m + 1
            print(pro)
            pro = pro / 3
            print(f"El promedio del ICA en el/la {REG[reg-1]} en el trimestre {tri} es de: {pro}")

    elif opt == 2:

        reg = int(input("1. Amazonía   2. Andina   3. Caribe  4. Orinoquía   5. Pacífico   Digite una opción: "))
        nmax = 0
        nmin = 200
        cmax = []
        cmin = []
        count = 0
        for m in range(12):
            if TMR[reg-1,m] > nmax:
                nmax = TMR[reg-1,m]
        for n in range(12):
            if TMR[reg-1,n] < nmin:
                nmin = TMR[reg-1,n]
        for o in range(12):
            if TMR[reg-1,o] == nmax:
                cmax.append(o+1)
            elif TMR[reg-1,o] == nmin:
                cmin.append(o+1)
        print(f"La temperatura maxima en el/la {REG[reg-1]} es {nmax} y se dió en los meses {cmax}, la minima es {nmin} "\
            f"y se dió en los meses {cmin}.")
    
    elif opt == 3:

        reg = int(input("1. Amazonía   2. Andina   3. Caribe  4. Orinoquía   5. Pacífico   Digite una opción: "))
        cica = int(input("Digite el ICA a buscar: "))
        busq = []
        for m in range(12):
            if ICA[reg-1,m] == cica:
                busq.append(m+1)
        if len(busq) != 0:
            print(f"El ICA de {cica} se dió en el/los mes(es) {busq}.")
        else:
            print("Esta temperatura no se dió en ningún mes.")

    elif opt == 4:

        reg = int(input("1. Amazonía   2. Andina   3. Caribe  4. Orinoquía   5. Pacífico   Digite una opción: "))
        print(f"El promedio anual de temperatura de el/la {REG[reg-1]} es de {proAnuTem(reg-1)}.")
    
    elif opt == 5:

        promTemp = []
        for m in range(len(REG)):
           promTemp.append(proAnuTem(m))
        promTemp = sorted(promTemp)
        for n in range(len(promTemp)):
            for o in range(len(REG)):
                if proAnuTem(n) == promTemp[o]:
                    print(f"El promedio anual de temperatura de el/la {REG[o]} es de {proAnuTem(o)}.")

    elif opt == 6:

        reg = int(input("1. Amazonía   2. Andina   3. Caribe  4. Orinoquía   5. Pacífico   Digite una opción: "))
        mes = int(input("Digite el mes: "))
        ind = int(input("Digite 1 si desea consultar el ICA, 2 si es la temperatura: "))
        if ind == 1:
            if ICA[reg-1,mes-1] >= 0 and ICA[reg-1,mes-1] <= 50:
                print(f"{REG[reg-1]}: {ICA[reg-1,mes-1]}. BUENA")
            elif ICA[reg-1,mes-1] >= 51 and ICA[reg-1,mes-1] <= 100:
                print(f"{REG[reg-1]}: {ICA[reg-1,mes-1]}. MODERADA")
            elif ICA[reg-1,mes-1] >= 101 and ICA[reg-1,mes-1] <= 150:
                print(f"{REG[reg-1]}: {ICA[reg-1,mes-1]}. DAÑINA PARA GRUPOS SENCIBLES")
            elif ICA[reg-1,mes-1] >= 151 and ICA[reg-1,mes-1] <= 200:
                print(f"{REG[reg-1]}: {ICA[reg-1,mes-1]}. DAÑINA")
            elif ICA[reg-1,mes-1] > 200:
                print(f"{REG[reg-1]}: {ICA[reg-1,mes-1]}. ALTO GRADO DE TOXICIDAD")
        elif ind == 2:
            print(f"{REG[reg-1]}: {TMR[reg-1,mes-1]}")

    elif opt == 7:

        for m in range(len(REG)):
            for n in range(12):
                if ICA[m,n] > 150:
                    print(f"{REG[m]} en el mes {n} con: {ICA[m,n]}")
        
    elif opt == 8:

        ind = int(input("Digite 1 si desea consultar la temperatura, 2 si es e ICA: "))
        promAnu = 0
        if ind == 1:
            for n in range(len(REG)):
                promAnu += proAnuTem(n)
            promAnu /= len(REG)
            print("Las regiones con un promedio de temperatura menor al promedio total son:\n")
            for m in range(len(REG)):
                if proAnuTem(m) < promAnu:
                    print(f"{REG[m-1]}, con un promedio de: {proAnuTem(m)}")
        elif ind == 2:
            for n in range(len(REG)):
                promAnu += proAnuICA(n)
            promAnu /= len(REG)
            print("Las regiones con un promedio de ICA menor al promedio total son:\n")
            for m in range(len(REG)):
                if proAnuICA(m) < promAnu:
                    print(f"{REG[m-1]}, con un promedio de: {proAnuICA(m)}")

    print("Nos fuimos de pachanga")

    loopSta = input("¿Desea realizar otra consulta? SI/NO: ")
    if loopSta.upper() == "SI":
        loop = True                 #Se valida si se quiere
    elif loopSta.upper() == "NO":   #realizar otra consulta
        loop = False
    else:
        print("Opcion no valida.")
        break

# -*- coding: utf-8 -*-

#PEDIMOS DISCULPAS POR LAS MALAS PRACTICAS :(
#RECONOCEMOS QUE ES UNA COMPLETA VERGUENZA :'(

print('AQUÍ PUEDES CONSULTAR CUANTO TIENES QUE PAGAR POR TUS SERVICIOS')

def disDat():
    if payTim1 == 1:
        if payTim2 >= 5:
            return (valSer * 0.03) * -1       #Definimos la funcion que nos ayudará a encontrar
        else:                                 #el descuento por fecha de pago.
            return 0
    elif payTim1 == 2:
        return (valSer * (0.002 * payTim2))
    else:
        return 0

def payDat1():
    if disTot > 0:
        return 'Con un descuento total de '    #Definimos la funcion que nos ayudará a establacer
    else:                                      #en la pantalla si la accion total sobre la factura
        return 'Con un incremento de '         #es descuento o incremento.

def disBus():
    if optBus == '1':          #Definimos la funcion que nos ayudará a encontrar
        return valSer * 0.05   #el descuento dependiente de la empresa que elija.
    elif optBus == '2':
        return valSer * 0.03

def disStr(case):
    if case == 1:
        if strat >= 1 and strat <= 3:
            return valSer * 0.1
        elif strat >= 4 and strat <= 6:
            return valSer * 0.02            
    elif case == 2:                       #Definimos la funcion que nos ayudará a encontrar
        if strat == 1 or strat == 2:      #el descuento por estrato dependiendo del servicio
            return valSer * 0.1           #que elija.
        elif strat == 3 or strat == 4:
            return valSer * 0.07                
        elif strat == 5 or strat == 6:
            return valSer * 0.03


def disQua():
    if quaMin > 0 and quaMin <= 300:
        return valSer * 0.1            #Definimos la funcion que nos ayudará a encontrar
    elif quaMin > 300:                 #el descuento dependiente de la cantidad de minutos
        return valSer * 0.15           #de la linea.

def disAge():
    if linAge > 10:            #Definimos la funcion que nos ayudará a encontrar
        return valSer * 0.03   #el descuento por antiguedad de la linea
    else:
        return 0

loop = True #Para marcar el flujo o corte del ciclo

while loop == True:

    #Todas las entradas están validadas en el instante
    #en que se ingresan con un contraejemplo de dominio
    #que cierra el ciclo por errores de digitacion.
    print('Usted tiene un descuento del 3% si paga 5 dias antes de la fecha o puede tener un recargo del 0.2% por cada dia de retraso')
    payTim1 = int(input('Digite 1 si va a pagar el servicio antes de la fecha, 2 si va a pagar después de fecha, o 3 si va a pagar en el dia requerido: '))
    if payTim1 == 1 or payTim1 == 2 or payTim1 == 3:
        payTim2 = int(input('¿Cuantos días?: '))
        if payTim1 == 1:
            if payTim2 >= 5:
                payDat2 = 'Descuento por pago temprano del 5%: '
            payDat2 = 'No tiene accion por fecha de pago, por lo tanto es de'
        elif payTim1 == 2:
            payDat2 = 'Recargo por pago tardío de 0.2% por cada dia: '      #Le pido la fecha en que va a pagar. Establezco si
        elif payTim1 == 3:
            payDat2 = 'No tiene accion por fecha de pago, por lo tanto es de'
        if payTim2 < 0:                                                     #hay descuento o recargo dependiendo dicha fecha.
            print('Usted digitó un valor no valido.')
            break
    else:
        print("Usted digitó una opcion no valida")
        break

    valSer = float(input('¿Cuánto es el valor del servicio?: '))
    if valSer < 0:                                                 #Pido el valor del servicio y defino la variable a trabajar.
        print("Usted digitó un valor no valido")                   #Valido la entrada con un contraejemplo negativo que cierra el ciclo.
        break
    finValSer = valSer

    disDat()

    optSer = input('Digite 1 si lo que desea pagar es el acueducto, 2 si es el la energía o 3 si es el teléfono: ')   #Pido el servicio a pagar

    if optSer == '1':
        print('Usted tiene un descuento del 5% si su distribuidora es EMP, o del 3% si es Aguas Capital. \n'\
              'Tambien tiene un descuento por estrato del 10% si está entre 1 al 3, o del 2% si está entre 4 al 6.')
        optBus = input('Digite 1 si su distribuidora es EPM, o 2 si es Aguas Capital: ')
        if optBus != '1' and optBus != '2':
            print('Usted digitó una opcion no valida')
            break
        disBus()
        strat = int(input('¿Cual es tu estrato socioeconomico?: '))
        if strat < 1 or strat > 6:
            print('Usted digitó un estrato no valido')
            break
        disStr(1)
        if payTim1 == 1: disTot= disBus() + disStr(1) + abs(disDat()) #Evaluo si hay descuento o recargo por fecha,
        else: disTot = disBus() + disStr(1)                            #para sumarla o restarla al descuento total
        finValSer = finValSer - disBus() - disStr(1) + disDat()
        print(f'El valor que debe pagar por el acueducto es de {finValSer}. \n'\
              f'{payDat1()}{disTot}, constituido por: \n   - Descuento por empresa de {disBus()}. \n'\
              f'   - Descuento por estrato de {disStr(1)} \n{payDat2} {abs(disDat())}')

    elif optSer == '2':
        print('Usted tiene un descuento del 10% si su estrato está entre 1 y 2, del 7% \n'\
              'si está entre 3 y 4, o del 2% si está entre 4 y 6')
        strat = int(input('¿Cual es tu estrato socioeconomico?: '))
        if strat < 1 or strat > 6:
            print('Usted digitó un estrato no valido')
            break
        disStr(2)
        if payTim1 == 1: disTot= disStr(2) + abs(disDat()) #Evaluo si hay descuento o recargo por fecha,
        else: disTot = disStr(2)                            #para sumarla o restarla al descuento total
        finValSer = finValSer - disStr(2) + disDat()
        print(f'El valor que debe pagar por la energia es de {finValSer}. \n'\
              f'{payDat1()}{disTot}, constituido por: \n   -Descuento por estrato de {disStr(2)} \n'\
              f'{payDat2} {abs(disDat())}')

    elif optSer == '3':
        print('Usted tiene un descuento del 10% si su linea es de 300 minutos o menos '\
              'o del 15% si es de mas de 300.\n Tambien tiene un descuento del 3% en el'\
              'caso de su linea tenga más de 10 años de antiguedad')
        quaMin = int(input('¿Cual es la cantidad de minutos de su plan?: '))
        if quaMin <= 0:
            print('Usted digitó una cantidad de minutos no valida.')
            break
        disQua()
        linAge = int(input('¿Cuantos años lleva con la linea: '))
        if linAge < 0:
            print('Usted digitó una cantidad de años no valida.')
            break
        disAge()
        if payTim1 == 1: disTot = disQua() + disAge() + abs(disDat()) #Evaluo si hay descuento o recargo por fecha,
        else: disTot = disQua() + disAge()                            #para sumarla o restarla al descuento total
        finValSer = finValSer - disQua() - disAge() + disDat()
        print(f'El valor que debe pagar por su linea telefonica es de {finValSer}. \n'\
              f'{payDat1()}{disTot}, constituido por: \n   - Descuento por cantidad de minutos de {disQua()}. \n'\
              f'   - Descuento por antiguedad de la linea de {disAge()}. \n{payDat2} {abs(disDat())}')

    else:
        print('Usted digitó una opción no valida.')
        break

    loopSta = input('¿Desea realizar otra consulta? SI/NO: ')

    if loopSta.upper() == 'SI' or loopSta.upper() == 'SÍ':   #Evaluo si el usuario quiere o no
        loop = True                                          #realizar otra consulta
    elif loopSta.upper() == 'NO':
        loop = False
    else:
        print('Usted digitó una opción no valida.')
        break

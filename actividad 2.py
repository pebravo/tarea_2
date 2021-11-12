error = 0
salir = False
import os
while not salir:
    print('=========================')
    print('|Convertidor \t\t|')
    print('=========================\n')
    print('=========================')
    print('|1.- Celsius a Farenheit|')
    print('|2.- Farenheit a Kelvin |')
    print('|3.- Kelvin a Celsius\t|')
    print('|4.- Salir \t\t|')
    print('=========================')

    variable = int(input('seleccione la convesion de teperatura: '))

    if variable == 1:
        cls=float(input('ingrese  grados Celsius: '))
        print(f'la convercion de {cls} °C a Farenheit es',round((cls*9.5)+32,4),'F')
        input('presione enter para continuar...')
        os.system('cls')


    elif variable == 2:
        fht=float(input('ingrese  grados Farenheit: '))
        print(f'la convercion de {fht} a Kelvin es', round((fht-32)*5.9 + 32,4),'K')
        input('presione enter para continuar...')
        os.system('cls')

    elif variable == 3:
        K=float(input('ingrese  grados Kelvin: '))
        print(f'la convercion de {K} a Celsius es', round(K-273.15,4),'K')
        input('presione enter para continuar...')
        os.system('cls')

    elif variable == 4:
        print('saliendo del sistema...')
        salir=True
    else:
        print('opcion ivalida')
        error+= 1
    if error ==3:
        print('!ha llegado al máx de intentos¡')
        break
    
        


    

    

#COMO PUEDO MOFICAR UNA LISTA 


bandas = []

opcion=100
while(opcion != 5):
    print('*********FESTIVAL ALTAZON********')
    print('*********************************')
    print(' 1. Registrar Banda ')
    print(' 2. Cartel Festival ')
    print(' 3.Buscar Banda ')
    print(' 4. Modificar Banda')
    print(' 5.Finalizar ')
    opcion=int(input("Digita una opcion: "))

    #Iniciamos un ciclo para validar la opcion a coger 

    if opcion == 1:
        banda['id']=int(input('Digite el id'))           #SE LLAMA EL OBJETO DE BANDA  #como usar la libreria randon en python 
        banda['nombre']=input(' ** Nombre ** ')  
        banda['genero']=input(' ** Genero ** ')
        banda['clasificacion']=input(' ** Clasificacion ** ')
        banda['costbanda']=int(input(' ** Costo Banda ** '))
        banda['clasificacion']=input(' ** Tiempo ** ')
        bandas.append(banda)
        
        
    elif opcion == 2: #RECORIENDO UNA LISTA PARA IMPRIRMIR SUS ELEMENTOS
        for bandaAuxiliar in bandas:
            print(f'{bandaAuxiliar['id']}--{bandaAuxiliar['nombre']}')


    elif opcion == 3:  #Buscando un elemento 
        bandaBuscada = input ('Digita la banda que quieras buscar')
        for bandaAuxiliar in bandas:
            if bandaAuxiliar ['nombre'] == bandaBuscada:
                print('Felicitaciones')
            else:
                print('No lo encontraste')

    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        print('Escogiste una opcion erronea')
        


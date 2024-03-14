import random

bandas = []

def generar_id_aleatorio():
    return random.randint(1000, 9999)  # Puedes ajustar el rango según tus necesidades

while True:
    print('********* FESTIVAL ALTAZON ********')
    print('*********************************')
    print(' 1. Registrar Banda ')
    print(' 2. Cartel Festival ')
    print(' 3. Buscar Banda ')
    print(' 4. Modificar Banda')
    print(' 5. Finalizar ')
    
    try:
        opcion = int(input("Digita una opción: "))
        if opcion == 1:
            banda = {}
            banda['id'] = generar_id_aleatorio()
            banda['nombre'] = input('Nombre de la banda: ')
            banda['genero'] = input('Género de la banda: ')
            banda['clasificacion'] = input('Clasificación de la banda: ')
            banda['costbanda'] = int(input('Costo de la banda: '))
            banda['tiempo'] = int(input('Tiempo de presentación (minutos): '))
            bandas.append(banda)
            print('Banda registrada exitosamente.')
        elif opcion == 2:
            # Implementar la lógica para mostrar el cartel del festival
            pass
        elif opcion == 3:
            id_buscar = int(input('Digite el ID de la banda a buscar: '))
            for b in bandas:
                if b['id'] == id_buscar:
                    print('Información de la banda:')
                    print(b)
                    break
            else:
                print('Banda no encontrada.')
        elif opcion == 4:
            # Implementar la modificación de datos de una banda
            pass
        elif opcion == 5:
            print('¡Hasta luego!')
            break
        else:
            print('Opción incorrecta. Debes elegir un número entre 1 y 5.')
    except ValueError:
        print('Error: Ingresa un número válido para la opción.')

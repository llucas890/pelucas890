import random
import msvcrt

puntaje = 0
eleccion = (input('Piedra, Papel o Tijera: '))
lista = ('Piedra', 'Papel', 'Tijera')
robot = random.choice(lista)
print(f'El robot elijio {robot}')
if eleccion == 'Piedra':
    if robot == 'Piedra':
        print('Los dos eligieron piedra es un empate')
    elif robot == 'Papel':
        puntaje -= 1
        print('Perdiste gana papel')
    elif robot == 'Tijera':
        puntaje += 1
        print('Gana piedra')
    else:
        print('Debes elegir uno de los 3')
elif eleccion == 'Papel':
    if robot == 'Piedra':
        puntaje -= 1
        print('Perdiste gana piedra')
    elif robot == 'Papel':
        puntaje += 1
        print('Gana tijera')
    elif robot == 'Tijera':
        print('Empate')
    else:
        print('Debes elegir uno de los 3')
elif eleccion == 'Tijera':
    if robot == 'Piedra':
        puntaje += 1
        print('Gana papel')
    elif robot == 'Papel':
        print('Empate')
    elif robot == 'Tijera':
        puntaje -= 1
        print('Perdiste gana tijera')
    else:
        print('Debes elegir uno de los 3')
else:
    print('Debes ingresar un valor correcto')
print('Programa creado por Lucas Lescano')
print('Presiona una tecla para salir...')
msvcrt.getch()
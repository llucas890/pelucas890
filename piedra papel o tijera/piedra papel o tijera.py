import random
import msvcrt


puntaje = 0
eleccion = None
lista = ('Piedra', 'Papel', 'Tijera')
print('Bienvenido a Piedra, papel o tijera. Diviertete')
print('Si deseas salir, escribe: Salir')
print('Si deseas ver tu puntaje, escribe: Puntaje')
while eleccion != 'Salir':
    print('1. Piedra, 2. Papel o 3. Tijera')
    eleccion = input('Cual es tu eleccion: \n')
    if eleccion == 'Puntaje':
        print(f'Tu puntaje es: {puntaje}')
    if eleccion == 'Ayuda':
        print('Nadie puede ayudarte ahora')
    if eleccion == 'Piedra' or eleccion == '1':
        robot = random.choice(lista)
        print(f'El robot elijio {robot}')
        if robot == 'Piedra':
            print('Los dos eligieron piedra... es un empate! \n')
        elif robot == 'Papel':
            puntaje -= 1
            print('Perdiste!!')
            print(f'Tu puntaje es: {puntaje} \n')
        elif robot == 'Tijera':
            puntaje += 1
            print('Ganaste!!')
            print(f'Tu puntaje es: {puntaje} \n')
    elif eleccion == 'Papel' or eleccion == '2':
        robot = random.choice(lista)
        print(f'El robot elijio {robot}')
        if robot == 'Piedra':
            puntaje -= 1
            print('Perdiste!!')
            print(f'Tu puntaje es: {puntaje}\n')
        elif robot == 'Papel':
            puntaje += 1
            print('Ganaste!!')
            print(f'Tu puntaje es: {puntaje}\n')
        elif robot == 'Tijera':
            print('Los dos eligieron tijera... es un empate! \n')
    elif eleccion == 'Tijera' or eleccion == '3':
        robot = random.choice(lista)
        print(f'El robot elijio {robot}')
        if robot == 'Piedra':
            puntaje += 1
            print('Ganaste!!')
            print(f'Tu puntaje es: {puntaje}\n')
        elif robot == 'Papel':
            print('Los dos eligieron papel... es un empate\n')
        elif robot == 'Tijera':
            puntaje -= 1
            print('Perdiste!!!')
            print(f'Tu puntaje es: {puntaje}\n')
print('Espero te hayas divertido!')
print('Programa creado por Lucas Lescano')
print('Presiona una tecla para salir...')
msvcrt.getch()

import msvcrt


def binario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario


numero = int(input('Introduce el numero que quieres convertir a binario: '))
print(binario(numero))
print('Programa creado por Lucas Lescano')
print('Presiona una tecla para salir...')
msvcrt.getch()
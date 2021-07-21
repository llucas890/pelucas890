import socket
import msvcrt

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f'El nombre de tu pc es: {hostname}')
print(f'Tu direccion de ip es: {ip}')
print('Programa creado por Lucas Lescano')
print('Presiona una tecla para salir...')
msvcrt.getch()

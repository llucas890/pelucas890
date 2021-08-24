class Convertidor:
    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def c_f(cls, celsius):
        if celsius >= Convertidor.MAX_CELSIUS:
            raise ValueError(f'La temperatura ingresada es demasiado elevada: {celsius}')
        return celsius * 9 / 5 + 32

    @classmethod
    def f_c(cls, fahrenheit):
        if fahrenheit >= Convertidor.MAX_FAHRENHEIT:
            raise ValueError(f'La temperatura ingresada es demasiado elevada: {fahrenheit}')
        return (fahrenheit - 32) * 5 / 9


print('Bienvenido al convertidor de temperatura: ')
print('Programa creado por Lucas Lescano')
print('Opciones:')
print('1. C a F')
print('2. F a C')
print('3. Salir')
opcion = None
while opcion != 3:
    opcion = int(input('Elije una opcion: '))
    if opcion == 1:
        temperatura = int(input('Ingrese la temperatura (0-100C): '))
        temperatura = Convertidor.c_f(temperatura)
        print(f'La temperatura convertida en fahrenheit es {temperatura:.2f}')
    if opcion == 2:
        fahren = int(input('Ingrese la temperatura (0-213F): '))
        fahren = Convertidor.f_c(fahren)
        print(f'La temperatura convertida en celcius es {fahren:.2f} ')
    if opcion == 3:
        break

# if __name__ == '__main__':
#     resultado = Convertidor.c_f(30)
#     resultado2 = Convertidor.f_c(120)
#     print(f'La temperatura convertida en fahrenheit es {resultado:.2f}')
#     print(f'La temperatura convertida en celcius es {resultado2:.2f} ')

from math import pi

def area():
    a = pi * r ** 2
    return a


def circ():
    c = r * 2 * pi
    return c

def resultado(a, c):
    print('Datos del círculo')
    print(f'Área: {a}')
    print(f'Circunferencia: {c}')

print('Ingrese una medidad de radio para calcular el area y circunferencia de un círculo')

while True:
    r = input('Radio: ')
    try:
        r = float(r)
    except ValueError:
        print('Ingrese un número válido')
        continue
    
    if r <= 0:
        print('No es una medida posible')
    else:
        break

resultado(area(),circ())

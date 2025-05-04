def get_int(s):
    while True:
        try:
            return int(input(s))
        except ValueError:
            print('Ingrese un número entero')

print('Ingrese los siguientes datos')

nombre = input('Nombre: ')
edad = get_int('Edad: ')
direccion = input('Dirección: ')
telefono = get_int('Teléfono: ')

persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}

print(f'{persona["nombre"]} tiene {persona["edad"]} años, con domicilio en {persona["direccion"]} y su número telefónico es {persona["telefono"]}.')
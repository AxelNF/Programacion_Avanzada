print('Ingrese los siguientes datos')

nombre = input('Nombre: ')
edad = int(input('Edad: '))
direccion = input('Dirección: ')
telefono = int(input('Teléfono: '))

persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}

print(f'{nombre} tiene {edad} años, con domicilio en {direccion} y su número telefónico es {telefono}.')
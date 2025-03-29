productos = {'leche': 23, 'aceite': 40, 'arroz': 28, 'huevo': 54 }

prod = input('Producto: ')
cant = int(input('Cantidad de unidades: '))

precio = productos[prod] * cant

try:    
    print(f'Precio total: ${precio}')
except ValueError:
    print('Ingresó un producto no.. existente')
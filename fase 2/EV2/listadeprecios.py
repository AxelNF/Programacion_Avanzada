productos = {
    'leche': 23, 
    'aceite': 40, 
    'arroz': 28, 
    'huevo': 54
}

while True:
    prod = input('Producto: ')
    if prod in productos:
        break
    else:
        print('El producto que ingresó no existe, intente con otro')

while True:
    try:
        cant = int(input(f'Cantidad de {prod} a comprar: '))
    except ValueError:
        print('La cantidad debe ser un número entero')
        continue
    
    if cant < 0:
        print('Ingrese una cantidad válida')
    elif cant == 0:
        print('No puede comprar una cantidad de 0')
    else:
        break

precio = productos[prod] * cant

print(f'El precio total es: {precio}')
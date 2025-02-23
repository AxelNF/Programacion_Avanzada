calificaciones = 0
contador = 0

print('A continuación ingrese calificaciones para obtener un promedio, y escriba letras para finalizar')

while True:
    calificacion = (input('Calificación: '))
    try:
        calificacion = float(calificacion)
    except ValueError:
        break

    if 0 <= calificacion <= 100:
        calificaciones += calificacion
        contador += 1
        continue
    else:
        print('Los números válidos son del 0 al 100')

if contador > 0:
    promedio = calificaciones / contador
    print(f'El promedio es: {promedio}')
else:
    print('No ingresó calificaciones')
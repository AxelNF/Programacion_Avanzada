import os
import csv
import re
from datetime import datetime
from clases import participante

participantes = []

def main():
    menu()

def menu():
    while True:
        print('MENU')
        print('[1] Cargar información de CSV')
        print('[2] Registrar participante')
        print('[3] Buscar participante')
        print('[4] Modificar participante')
        print('[5] Eliminar participante')
        print('[6] Ver lista de participantes')
        print('[7] Actualizar información de CSV')
        print('[8] Serializar información a JSON')
        print('[X] Salir')
        opc = input('¿Qúe opción deseas? ')
        if opc.lower() not in ['1', '2', '3', '4', '5', '6', '7', '8', 'x']:
            print('Opción no válida, intenta de nuevo.')
            continue
        elif opc == '1':
            cargar()
        elif opc == '2':
            registrar()
        elif opc == '3':
            buscar()
        elif opc == '4':
            modificar()
        elif opc == '5':
            eliminar()
        elif opc == '6':
            ver()
        elif opc == '7':
            actualizar()
        elif opc == '8':
            serializar()
        else:
            print('Saliendo...')
            break


def cargar():
    global participantes
    archivo = 'participantes.csv'
    if not os.path.exists(archivo):
        with open(archivo, 'w', newline='') as f:
            f.write('Correo|Nombre|Nacimiento|Momento\n')
        participantes = []
        print('Archivo CSV creado.')
    else:
        with open(archivo, 'r', newline = '') as f:
            reader = csv.reader(f, delimiter='|')
            next(reader)
            for row in reader:
                if len(row) == 4:
                    correo, nombre, nacimiento, momento = row
                    p = participante(correo, nombre, nacimiento, momento)
                    participantes.append(p)
        print('Archivo CSV cargado.')

def registrar():
    while True:
        correo = input('Correo: ')
        if correo == '':
            print('Regresando al menú')
            break
        if not validar_correo(correo):
            print('Correo inválido, intenta de nuevo.')
            continue
        if repetido(correo):
            print('El correo ya existe, intenta de nuevo.')
            print('Regresando al menú')
            break
        nombre = input('Nombre: ')
        if not validar_nombre(nombre):
            print('Nombre inválido, intenta de nuevo.')
            continue
        nacimiento = input('Fecha de nacimiento (YYYY/MM/DD): ')
        if not validar_fecha(nacimiento):
            print('Fecha inválida, intenta de nuevo.')
            continue
        momento = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        p = participante(correo, nombre, nacimiento, momento)
        participantes.append(p)
        print('Participante registrado.')

def buscar():
    pass

def modificar():
    pass

def eliminar():
    pass

def ver():
    pass

def actualizar():
    pass

def serializar():
    pass

def repetido(correo):
    for p in participantes:
        if p.correo == correo:
            return True
    return False

def validar_correo(correo):
    if not 10 <= len(correo) <= 40:
        return False
    if not re.match(r'^[\w\.]+@[\w\.]+\.\w+$', correo):
        return False
    return True

def validar_nombre(nombre):
    if not 5 <= len(nombre) <= 40:
        return False
    if not re.match(r'^[A-Z ]+$', nombre):
        return False
    return True

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, '%Y/%m/%d')
        return True
    except ValueError:
        return False

main()
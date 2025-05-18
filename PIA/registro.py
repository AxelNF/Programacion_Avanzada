import os
import csv
import re
import json
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
    correo = pedir_correo()
    if not correo:
        return
    if coincidencia(correo):
        print('El correo ya existe.')
        print('Regresando al menú')
        return

    nombre = pedir_nombre()
    nacimiento = pedir_nacimiento()

    momento = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    p = participante(correo, nombre, nacimiento, momento)
    participantes.append(p)
    print('Participante registrado.')
    

def buscar():
    correo = pedir_correo()
    if not correo:
        return
    p = coincidencia(correo)
    if p:
        print(p)
    else:
        print('Ese correo no está registrado en la lista.')

def modificar():
    while True:
        correo = pedir_correo()
        if not correo:
            return
        p = coincidencia(correo)
        if p:
            print('Información actual:')
            print(p)

            print('Ingrese nueva información:')
            nombre = pedir_nombre()
            nacimiento = pedir_nacimiento()

            p.nombre = nombre
            p.nacimiento = nacimiento

            print('Información actualizada.')
            return
        else:
            print('Ese correo no está registrado en la lista.')
            return

def eliminar():
    while True:
        correo = pedir_correo()
        if not correo:
            return
        p = coincidencia(correo)
        if p:
            print(p)
            opc = input('¿Deseas eliminar este registro? (s/n): ')
            if opc.lower() == 's':
                participantes.remove(p)
                print('Registro eliminado.')
            else:
                print('Registro no eliminado.')
            return
        else:
            print('Ese correo no está registrado en la lista.')
            return

def ver():
    if not participantes:
        print('No hay participantes registrados.')
        return
    print(f"{'Correo':<40} {'Nombre':<40} {'Nacimiento':<15} {'Momento':<20}")
    print('-' * 115)
    for p in participantes:
        print(f"{p.correo:<40} {p.nombre:<40} {p.nacimiento:<15} {p.momento:<20}")

def actualizar():
    archivo = 'participantes.csv'
    respaldo = 'participantes.bak'
    if os.path.exists(archivo):
        os.replace(archivo, respaldo)
    with open(archivo, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow(['Correo', 'Nombre', 'Nacimiento', 'Momento'])
        for p in participantes:
            writer.writerow([p.correo, p.nombre, p.nacimiento, p.momento])
    print('Archivo CSV actualizado.')

def serializar():
    json_data = json.dumps(participantes, default=lambda p: p.__dict__, indent=4)
    print(json_data)

def coincidencia(correo):
    for p in participantes:
        if p.correo == correo:
            return p
    return

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
    
def pedir_correo():
    while True:
        correo = input('Correo: ')
        if correo == '':
            print('Regresando al menú')
            return
        if not validar_correo(correo):
            print('Correo inválido, intenta de nuevo.')
            continue
        return correo

def pedir_nombre():
    while True:
        nombre = input('Nombre: ')
        if not validar_nombre(nombre):
            print('Nombre inválido, intenta de nuevo.')
            continue
        return nombre
    
def pedir_nacimiento():
    while True:
        nacimiento = input('Fecha de nacimiento (YYYY/MM/DD): ')
        if not validar_fecha(nacimiento):
            print('Fecha inválida, intenta de nuevo.')
            continue
        return nacimiento
    
participantes.append(participante('jesus.perez@gmail.com', 'Jesus Perez', '2000/01/01', '2023/10/01 12:00:00'))

main()
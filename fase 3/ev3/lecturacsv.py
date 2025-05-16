import csv

with open('estudiantes.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    contador_lineas = 0
    
    for linea_datos in lector_csv:
        if contador_lineas == 0:
            print(f'Los nombres de columna son {", ".join(linea_datos)}')
        else:
            print (f'\tMATRICULA: {linea_datos[0]}.')
            print (f'\tNOMBRE: {linea_datos[1]}.')
            print (f'\tAPELLIDO PATERNO: {linea_datos[2]}.')
            print (f'\tAPELLIDO MATERNO: {linea_datos[3]}.')
            print (f'\tFECHA DE NACIMIENTO: {linea_datos[4]}.')
            print (f'\t--------------------------------------------')
        contador_lineas += 1

    print(f'Procesadas {contador_lineas} líneas.')
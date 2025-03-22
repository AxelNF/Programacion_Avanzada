from datetime import *

def  fecha_nac():
    while True:
        fn = input ('Fecha de nacimineto (formato dd/mm/aaaa): ')
        
        fn = datetime.strftime('%d/%m/%Y')
        
    
fecha_nac()
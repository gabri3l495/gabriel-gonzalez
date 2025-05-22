# creacion de armas en minecraft
# crear espadas de diamante
# para crear na espada necesitas
# 2 diamantes y un Palo 
# para obtener los recursos debe tener el 
# seguiente menu:
# 1-minar y buscar recursos, la posibilidad de encontrar
# diamante es entre 7 y palo 1 entre 3 y la de carbon 1 entre 3(10c = 1 diamante)
# minar toma 3 segundos
# 2-consultar recursos, recursos acumulados
# 3-crear espada, va a crear tantas como pueda 
# con los recursos existentes 
# 4-salir,sale

import random
import time

diamantes=0
palos=0
carbons=0
espada=0
while True:
    menu=int(input('''
    que haras:
    1- minar
    2- consultar recursos
    3- crear espada
    4- salir                                          
    -> '''))
    match menu:
        case 1:
            time.sleep(3)
            print("minando")
            diamante=random.randint(1,7)
            diamantes+=diamante
            palo=random.randint(1,3) 
            palos+=palo
            carbon=random.randint(1,3)
            carbons+=carbon
            print("terminando de minar")
        case 2:
            if carbons>10:
                carbons-=10
                diamantes+=1
            print(f'''
        los diamantes que tienes son {diamantes}
        los palos que tienes son {palos} 
        el carbon que tienes es {carbons}        ''')
            
            
        case 3:
            while True:
                if diamantes>=2 and palos>=1:
                    diamantes-=2
                    palos-=1
                    espada+=1
                else:
                    print(f"no tienes los recursos suficientes, lograste crear {espada} espadas")
                    break

           
        case 4:
            print("pa fuera puto")
            break
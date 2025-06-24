#crud de diccionarios

# def MostrarJuegos(juegos):
#      for j, datos in juegos.items:
#          print(j, datos)
# juegos={
#     1:{"nombre":"metroid dread",
#        "precio": 50000,
#        "code":"mmdd2023"
#        },               
#     2:{"nombre":"pikmin 4",
#        "precio": 55000,
#        "code":"pkmn2022"
#        },
#     }
# MostrarJuegos(juegos)
# ultima=list(juegos.keys())[-1]       #ayuda en la organizacion ,con repecto a los numeros?
# nombre=input("ingrese nombre del juego")
# precio=int(input("ingrese el precio del juego"))
# code=input("ingrese el codigo del juego")
# juegos[ultima+1]={"nombre": nombre,
#                   "precio": precio,
#                   "code":   code
#                 },
# MostrarJuegos(juegos)



#--------------------------------------------#

juegos={
    1:{"nombre":"metroid dread",
       "precio": 50000,
       "code":"mmdd2023"
       },               
    2:{"nombre":"pikmin 4",
       "precio": 55000,
       "code":"pkmn2022"
       },
    }
def Mostrar_Juegos(dic):
     for j, datos in dic.items():
         print(j, datos)


def valida_codigo(clave):
    mayuscula=0
    minuscula=0
    numero=0
    for palabra in clave:
        if palabra.isupper():
                mayuscula+=1
        if palabra.islower():
                minuscula+=1
        if palabra.isdigit():
                numero+=1
    if mayuscula==2 and minuscula==2 and numero==4: #len(clave)==6:
        print("contraseña valida")
        return True
    else:
        print("mal")
        return False
        
 
def agregar_juego(dic):
    ultima=list(dic.keys())[-1]
    nombre=input("ingrese el nombre del juego -> ")
    precio=int(input("ingrese el precio del juego -> "))
    while True:
        codigo=input("ingrese el codigo del juego ->")
        if valida_codigo(codigo):
            dic[ultima+1]={"nombre": nombre,
                            "precio": precio,
                            "code": codigo}
            break
        else:
            print("el juego no fue ingresado")
            


def actualizar(dic):
     Mostrar_Juegos(dic)
     opc=int(input("seleccione el perro a actualizar ->"))
     while True:
          dato=int(input('''
1-nombre
2-precio
3-codigo
4-salir
-> '''))
          match dato:
               case 1:
                    nom=input("ingrese el nombre")
                    dic[opc]["nombre"]=nom
               case 2:
                    nom=int(input("ingrese el precio"))
                    dic[opc]["precio"]=nom
               case 3:
                    nom=input("ingrese el codigo")
                    if valida_codigo(nom):
                       dic[opc]["code"]=nom
               case 4:
                    break
               case _:
                    print("opcion invalida")

    
def borrar(dic):
    Mostrar_Juegos(dic)
    fuera=int(input("cual decea borrar"))
    if fuera in dic:
       del dic[fuera]
       return True
    else:
        print("el juego no existe")
        return False
    
def valida_precio(precio):
     if precio<8000 or precio>100000:
          return False
     else:
          return True
    

def valida_nombre(frase):
     if " " in frase:
          return True
     else:
          return False


#-----------------------------------------#
while True:
    try:
          print('''
1-agregar juego
2-mostrar juego
3-actualizar juego
4-borrar juego
5-salir
            ''')
          op=int(input("selecciones una opcion ->"))
          match op:
               case 1:
                    agregar_juego(juegos)
               case 2:
                    Mostrar_Juegos(juegos)
               case 3:
                    actualizar(juegos)
               case 4:
                    borrar(juegos)
               case 5:
                    print("saliendo")
                    break
               case _:
                    print("opcion invalida")
                    break
    except Exception:            
        print("opcion invalida")
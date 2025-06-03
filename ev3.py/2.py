
# NUEVO
#append(E) -> agreaga un elemento al final de la lista
#pop(int)  -> elimina un elemento de la lisa del index especificado

# lista_productos=[1,"hola",0.15]
# print(lista_productos[1])          #primer producto

# print(lista_productos)
# lista_productos.append("maria")    #agrega a maria a la lista

# print(lista_productos)             #muestra la lista con el nuevo producto

# for i in lista_productos:
#     print(i)                       #muestra los productos ordenadamente



# EJERCICIO 1 -> crear menu el cual tenga la opcion de agregar elemento, quitarlo o eliminar , mostrar elementos de la lista y salir de este

# lista=[1,2,3]
# while True:
#     menu=int(input('''
# 1-agregar elemento a lista
# 2-eliminar elemento de la lista
# 3-mostrar cada uno de los elementos de la lista
# 4-cerrar sistema
# -> '''))
#     match menu:
#         case 1:
#             nuevo=(input("que desea agregar a la lista ->"))
#             lista.append(nuevo)
#         case 2:
#             cont=1
#             for i in lista:
#                 print(f"{cont} - {i}")
#                 cont+=1
#             fuera=int(input("cual pa fuera ->"))-1
#             print(f"producto {lista[fuera]} eliminado exitosamente")
#             lista.pop(fuera)
#         case 3:
#             for i in lista:
#                   print(i)            
#         case 4:
#             print("saliendo")
#             break




# la wea rara del profe
from os import system  #es como el limpiar pantalla 
from validaciones import  validar_numero       #esto genera la conexion a la otra carpeta llamada validaciones
lista_productos=["tomates","arroz","bebidas"]
while True:
    print('''
1-agregar 
2-eliminar
3-ver
4-salir
 ''')
    # opc=int(input("->"))
    opc=validar_numero(1,4,"opcion")
    match opc:
        case 1:
            producto=input("agrege nombre del producto")
            lista_productos.append(producto)
            print(f"producto {producto} agregado exitosamente")
            input("presione enter para continuar...")
            system("cls")                      #con esto se limpia la pantalla
        case 2:
            if len(lista_productos)==0:
                print("info la lista esta vacia ")
                input("presione enter para continuar...")
                system("cls")
            else:
                cont=1
                for i in lista_productos:
                    print(f"{cont}.-{i}")
                    cont+=1
                eliminar=int(input("eliminar -> "))-1
                lista_productos.pop(eliminar)
                input("presione enter para continuar...")
                system("cls")
        case 3:
            cont=1
            for i in lista_productos:
                print(f"{cont}.-{i}")
                cont+=1
            input("presione enter para continuar...")
            system("cls")           
        case 4:
            print("saliendo")
            break
        case _:
            print("error, valor no valido")
            input("presione enter para continuar...")
            system("cls") 
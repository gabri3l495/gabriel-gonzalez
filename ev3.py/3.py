
#                                                             "AGREGAR MEDIANTE UN MENU, ELEMENTOS A UNA LISTA"
# nombres=[]
# while True:
#     print('''
# 1- insertar nombre
# 2- salir
#           ''')
#     op=int(input("seleccione uan opcion -> "))
#     match op:
#         case 1:
#             nom=input("ingrese un nombre")
#             nombres.append(nom)     #agregar algo a la lista -> lista.append.[variable]
#             print(nombres)

#         case 2:
#             print("saliendo")
#             break
#         case _:
#             print("opcion invalida")

#                                                  "CREAR MENU CON MAS OPCIONES QUE EL ANTERIOR, CON UN PAR DEASPECTOS NUEVOS"
# nombres=[]
# apellidos=[]
# while True:
#     print('''
# 1- insertar nombre y apellido
# 2- buscar nombre
# 3- mostar nombres
# 4-salir
#           ''')
#     opc=int(input("seleccione una opcion -> "))
#     match opc:
#         case 1:
#             nom=input("ingrese el nombre -> ")
#             nombres.append(nom)
#             apell=input("ingrese su apellido")
#             nombres.append(apell)
#         case 2:
#             buscar=input("ingrese el nombre a buscar ->")
#             if buscar in nombres:
#                 print(f"el nombre {buscar} se encuentra en la lista ")
#             else:
#                 print(f"el nombre {buscar} no s eencuentra en la lista")
#         case 3:
#            cont=0
#            for nombre in nombres:
#                print( cont+1,"-",nombres[cont], apellidos[cont])
#                cont+=1
#         case 4:
#             print("saliendo")
#             break
#         case _:
#             print("opcion invalida")

#                                                                      "CREAR CARRITO DE COMPRAS 3.0"
# tomar el carrito de compras anterior y 
# hacerlo con listas
# 1 ingresar producto
# 2 comprar
# 3 crear boleta
# 4 salir
# que el carrito comience con 3 productos 
# hay que hacer 3 listas, produtos, precios y carrito

total=0
productos=["pollo","cerdo","vaca"]
precios=[50000,100000,200000]
carrito=[]
while True:
    print('''
1- ingresar un producto nuevo
2- comprar algo
3- crear boleta 
4- salir 
''')
    opc=int(input("ingrese una opcion -> "))
    match opc:
        case 1:
            nom=input("ingrese un producto -> ")
            productos.append(nom)
            apell=int(input("ingrese un precio ->"))
            precios.append(apell)          
        case 2:      
            while True:
                for i in range(len(productos)):
                    print(i+1, ".-", productos[i], "$", precios[i]) 
                pro=int(input("selecciones l que quiere comprar"))
                carrito.append(pro-1)
                break      
        case 3:
            print("bienvenido a tortura animal :3")
            for i in range(len(carrito)):
                print(productos[i], "---$", precios[i])  
                total=total+precios[i] 
            print(f"el total de articulos es {len(carrito)} ")                     
            print(f"su total neto es {total}")                     
            print(f"su total con IVA es {total*1.19}")                     
        case 4:
            print("saliendo :3")
            break
        case _:
            print("opcion invalida")

# NUEVO
# numeros.insert(3,1000)
# numeros.remove(66)
# numeros.sort()
# numeros.append()




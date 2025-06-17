# recordar el concepto de definir el cual es colocar, algo dentro de 
# def "variable()", la cual para lograr que sea ejecutada se debe de colocar
# "variable()" para qie asi se realize este proceso

#ej:
# def suma():
#     n1=int(input("numero 1"))
#     n2=int(input("numero 2"))
#     print(n1+n2)

# suma() #-> este es quien hace que se ejecute, si no esta no se desarrolla nada delo que esta dentro del def suma()

#OTRA 

# def sumas():
#     n1=int(input("numero 1"))
#     n2=int(input("numero 2"))
#     return n1+n2
# suma=sumas()
# print(suma)
#en esta parte el return nos ayuda a poder manipular el resultado para modificarlo a nuestra idea

#-------------------------------------------------------------#

# realizar una funcion que calcule el IVA 

# realizar otra funcion que al pagarle un Precio 
# y un numero como porcentaje  (ej: 20)
# calcule el descuento y muestre el valor final

# def iva(n):
#     return n*1.19

# def num():
#     precio=int(input("ingrese un precio -> "))
#     porcentaje=int(input("ingrese el porcentaje de descuento -> "))
#     return precio*(porcentaje/100)
# neto=1500
# desc=num()
# total=iva(neto-desc)

# print(f"la wea es {total}")


#diccionario


# productos=[
#     {"nombre":"portamina"},
#     {"nombre":"goma"},
# ]
# print(productos{0}{"nombre"})

# ajercicio:
# agregar articulo, borrar articulo, actualizar articulo, mostrar listado de articulos y salir






# productos=[
#     {"nombre":"lapiz","precio":400},
#     {"nombre":"goma","precio":200},
#     {"nombre":"estuche","precio":1600},
# ]

# def agregar(lista):
#     titulo=input("ingrese porducto -> ") 
#     precio=int(input("ingrese el precio ->"))  
#     lista.append({"nombre":titulo, "precio":precio})     # se coloca lista para que esta se peda ir cambiando a otras diferentes 

# def mostrar(lista):
#     for n,producto in enumerate(lista):
#         print(n+1, producto["nombre"], producto["precio"])

# while True:
#     try:
#        opc=int(input('''
# 1- agregar articulo
# 2- borrar articulo
# 3- actualizar articulo
# 4-mostrar listado
# 5-salir
# -> '''))
#        match opc:
#            case 1:
#                 agregar(productos)
#             #    titulo=input("ingrese porducto -> ") 
#             #    precio=int(input("ingrese el precio ->"))  
#             #    productos.append({"nombre":titulo, "precio":precio})           
#            case 2:
#                 for n,producto in enumerate(productos):
#                    print(n+1, productos["nombre"], producto["precio"])
#                 borrar=int(input("seleccione cual decea sacar"))
#                 productos.pop(borrar-1)
#            case 3:
#                 for n, producto in enumerate(producto):
#                    print(n+1, producto["nombre"], producto["precio"])
#                 act=int(input("selecciona cual decea actializar -> "))
#                 nombre=input("ingrese nombre del articulo")
#                 precio=int(input("ingrese el nombre del precio ->")) 
#                 productos[act-1]["nombre"]=nombre
#                 productos[act-1]["precio"]=precio

#            case 4:
#                for n, producto in enumerate(producto):
#                    print(n+1, producto["nombre"], producto["precio"])
#            case 5:
#                break
#            case _:
#                print("numero invalido")
               
#     except Exception as error:
#         print("el error es:", error)


#DICCIONARIO
personas={
    1:{"nombre":"liam neeson",
       "telefono":123456789,
       "estado civil":"soltero",
       "ciudadano":True,},
    2:{"nombre":"liam neeson",
       "telefono":123456789,
       "estado civil":"soltero",
       "ciudadano":True,},
    3:{"nombre":"liam neeson",
       "telefono":123456789,
       "estado civil":"soltero",
       "ciudadano":True,},
}
print(personas[2]["telefono"])
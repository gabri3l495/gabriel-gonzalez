'''
crear menu de carrito con las siguientes opciones
1- ingresar nombre del usuario
sera mostrado en la boleta con un saludo 
2- comprar poner productos para poder comprar 
con un precio correspondiente
3- sacar boleta calcular el precio mas iva mostrar totales
4- salir
consideraciones:
por lo menos 3 preductos 
no hay limite  de compra 
se puede salir en cualquier momento
los montos de los productos fijos
'''

# total=0
# nombre=input("ingrese su nombre")
# print(f"hola {nombre}")
# while True:
#     prod=int(input('''
#                     que producto desea lleaval
#                    1-arroz
#                    2-carne
#                    3-pollo
#                    4- salir 
#                    '''))
#     match prod:
#         case 1:
#             print("arroz")
#             total+=1000
#         case 2:
#             print("carne")
#             total+=2000
#         case 3:
#             print("pollito")
#             total+=3000

#         case 4:
#             print("salir")
#             break
#         case _:
#             print("error")
# print(f"hola {nombre} gastaste un total de {total} neto y con el IVA incluido", round(total*1.19) )
#-------------------------------------------------------# forma del profe -> algoa asi
# total=0
# while True:
#     print('''
#     seleccione opcion
#       1-ingresar nombre
#       2-comprar
#       3-mostar boleta
#       4-salir
#       ''')
#     op=int(input())
#     match op:
#         case 1:    
#             nombre=int("ingrese nombre")
#         case 2:
#              prod=int(input('''
#                     que producto desea lleaval
#                    1-arroz 1000
#                    2-carne 2000
#                    3-pollo 3000
#                    4- salir 
#                    '''))
#              match prod:
#                 case 1:                    
#                      total+=1000
#                 case 2:
#                      total+=2000
#                 case 3:
#                      total+=3000
#                 case 4:
#                      print("salir")
#                      break
#                 case _:
#                      print("error")
#         case 3:
#             print (f"hola {nombre} gastaste un total de {total} neto y con el IVA incluido", round(total*1.19), "gracias por venir")
    





#-------------------------------------------------------#
'''
pedir cantidad de alumnos 
pedir notas por cada alumno
promediar a cada alumno
y mostrar sia prueba o reprueba 
extra: mostrar el promedio de todos los alumnos ingresados  
'''
total=0
cantidad=int(input("cantidad de alumnos"))
for i in range(cantidad):
    notas=int(input(f" cantidad de notas del alumno {i+1}"))
    for k in range(notas):
        n1=float(input())
        n1+=n1
        prom=n1/notas
        print(f"la notas del alumno son {round(prom)}")
        if prom>4:
           print(f"aprueba el alumno {i+1}")
        else:
            print("reprueba")



    
        
    

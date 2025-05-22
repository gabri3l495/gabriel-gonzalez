# Perros de caza
# Pida al usuario la cantidad de perros
# Muestre cual es la cuota minima de conejos
# lugo consulte cauntos conejos trajo
# si el perro trajo la cantidad minima
# cumplio la cuota, sino, se queda sin filete
# mostrar resumen de perro que cumplieron y los que no
# import random, time
# while True:
#     try:
#         perros=int(input("ingrese los perros que irán a la caza: "))
#         while perros<1:
#             print("Ingrese un valor entero positivo")
#             perros=int(input("ingrese los perros que irán a la caza: "))
#         cuota=3
#         cumple=0
#         print("Comienza la caza")
#         for p in range(perros):
#             conejos=random.randint(0,6)
#             if conejos>=cuota:
#                 print(f"El perro {p+1} trajo {conejos} conejos")
#                 print("Hay Flete!")
#                 cumple+=1
#             else:
#                 print(f"El perro {p+1} trajo {conejos} conejos")
#                 print("no hay filete")
#         print(f" La cant de perro que cumplio fue {cumple}")
#         print(f" La cant de perro que NO cumplio fue {perros-cumple}")
#         break
#     except Exception:
#         print("Ingrese solo numeros enteros")

#--------------------------------------------#

# cant_rojos = int(input("Cuantos rojos hay en el curso???\n"))

# for i in range(cant_rojos):
#     respuesta = int(input(f"Hay 4 talleres en el semestre, ¿A cuantos asistio el alumno {i+1}?\n"))

#     decimas = 0

#     if respuesta == 1:
#         decimas += 0.3
#         print("No obtiene la bendicion del profe, no se le puede ayudar\n")
#     elif respuesta == 2:
#         decimas += 0.6
#         print("No obtiene la bendicion del profe, no se le puede ayudar\n")
#     elif respuesta == 3:
#         decimas += 0.9
#         print("No obtiene la bendicion del profe, no se le puede ayudar\n")
#     elif respuesta == 4:
#         decimas += 1.2
#         print("Obtiene la bendicion del profe, se le puede ayudar")
#     elif respuesta == 0:
#         print("No tienes decimas, asiste a los talleres para la proxima\n")
#     else:
#         print("Solo hay 4 talleres\n")

#     if decimas == 1.2:
#         print(f"\nObtuvo {decimas} decimas")
#         nota = float(input("\nIngrese su nota\n"))
#         nota_final = nota + decimas
#         print(f"La nota final del alumno {i+1} es {nota_final}")
#         if nota_final >= 4:
#             print(f"El estudiante {i+1} aprobo")
#         else:
#             print(f"El estudiante {i+1} NO aprobo")







# Lavado de autos
# Crear un menu para lavar autos
# 1.- Cursar pago del lavado 
# 2.- Ver ventas diarias
# 3.- salir
# El lavado tiene 3 niveles
# 1.- Full $ 15.000, 2- standard 10.000, 3.- Básico $7.000.
# al mostrar las ventas diarias, debe mostar la 
# cantidad de autos que han ingresado y el monto total 
# recaudado. Tambien debe mostrar el monto mas alto pagado  .
auto=0
pago=0
while True:
    menu=int(input('''
                   que desea hacer
                   1-cursar pago del lavado
                   2-cer ventas diarias
                   3-salir                   
                   -> '''))
    match menu:
        case 1:
            while True:
                niveles=int(input('''
                                  1- Full $ 15.000
                                  2- standard 10.000
                                  3- Básico $7.000                                 
                                  -> '''))
                match niveles:
                    case 1:
                        pago+=15000
                        auto+=1
                        break
                    case 2:
                        pago+=10000
                        auto+=1
                        break
                    case 3:
                        pago+=7000
                        auto+=1
                        break
        case 2:
            print(f"la cantidad de dinero conseguido con {auto} es ${pago}")
                


        case 3:
            print("saliendo puto")
            break
           
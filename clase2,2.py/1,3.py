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
#uso y aplicacion de listas
#     -6 -5 -4 -3 -2  -1     #lo que se debe colocar en []
# lista=[5 ,7 ,2 ,9 ,10,2 ]
# #      0  1  2  3  4  5      #otra opcion 

# #el que esta dentro de [] se puede cambiar dependiendo el numero de la lista
# print(lista[-6])             #acceso al valor indice negatico
# print(lista[0])              #acceso al valor indice positivo

# #acceso a lista completa
# print(lista)      #lista completa

# for num in lista:      #muestra la lista
#     print(num)


#ejercicio 1
# #hacer una lista de 5 notas 
# #luego sacar su promedio
# c=0
# suma=0
# lista=[10,20,30,40,50]
# for i in lista:
#     suma+=i
#     c+=1
# prom=suma/c
# print("promedio es", round(prom))


# ejercicio 2
# nombres=["robin","noelia","coni"]
# apellidos=["hood","maldonado","chan"]

# print(len(nombres))
# for i in range(len(nombres)):
#     print(f"su nombre es {nombres[i]} {apellidos[i]}")


#ejercicio 3
#contar caracteres de algo
# frutas=["sandia","melon","chirimoya"]
# for fruta in frutas:
#     print(f"la {fruta} tiene {len(fruta)} caracteres")

#si el len esta con una lista cuenta la cantidad de cosas que hay
#mientras que si len esta con una palabra especifica, cuenta sus caracteres (cantidad de letras)


#ejercicio 4
#ver cual de los autos tiene una letra A
# autos=["audi","toyota","bwm","kia","mercedes"]
# for auto in autos:
#     print(auto)
#     if "a" in auto.lower():
#         print("la marca tiene una A")
#     else:
#         print("ninguna A encontrada")


#ejercicio 5:
notas=[10,20,30,40,50]
c=0
suma=0
for nota in notas:
    suma+=nota
    c+=1
prom=suma/c
print("promedio es", round(prom))


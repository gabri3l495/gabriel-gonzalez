#     TAREA :o
# crear programa de manejo de notas
# 1 ingresar Nota 
# 2 borrar nota 
# 3 mostrar nota 
# 4 sacar promedio, nota mayor y menor
# 5 limpiar todas las notas 
# 6 salir
#(no se qui mierda paso, pero la wea funciona ._.)

# notas=[55,60]
# promedio=0
# while True:
#     opc=int(input('''
# 1- ingresar nota
# 2- borrar nota
# 3- mostar nota
# 4- sacar promedio
# 5- limpiar todas las notas
# 6- salir
# -> '''))
#     match opc:
#         case 1:
#             nueva=int(input("ingrese una nota -> "))
#             notas.append(nueva)
#         case 2:
#             for i in range (len(notas)):
#                 print(i+1, ".-", notas[i])
#             fuera=int(input("ingrese la nota que decea sacar -> "))
#             notas.pop(fuera-1)
#         case 3:
#             for i in notas:
#                 print( "-", i)            
#         case 4:
#             cont=0
#             for i in notas:            
#                 promedio+=i
#                 cont+=1
#             prom=promedio/cont 
                          
#             print(f"el promedio obtenido hasta ahora es {round(prom)}")
#         case 5:
#             print("limpiando lista")
#             notas.clear()
#         case 6:
#             print("saliendo")
#             break
#         case _:
#             print("opcion invalida")

# PROFE
# notas=[]
# while True:
#     while True:
#         try:
#         except Exception:


# NUEVO
# for num, n in enumerate(notas):
#     print(num+1, "._", n)
#el num corresponde al numero y el n a una de las notas en este caso

# promedio=sum(notas)/len(notas)
# print(max(notas))
# print(min(notas))
# print(promedio)
#este como es logico, da los datos minimos y maximos y el primero, pus saca el promedio 


#pueden haber listas dentro de listas 
# vero=[
#     [3,7],          #-> lista numero 0
#     ["put","si"]    #-> lista numero 1
# ]
# print (vero[0])


#DICCIONARIOS

# dic={
#     "nombre": "alan grant",   
#     "numero": 97856,
#     "casado": True,
#     133: "oa"
# }
# print(dic)
# print(dic["numero"])
# dic["nombre"] = "alan grant brito"   #cambiar nombre u asignacion 
# print(dic)                           #este mostraria el cambio realizado
# dic["yo"] = "nose" # si se coloca algo que no existe, este se agregara al diccionario


#OTRO CASO
frutas={
    "manzana": 500,   # "key": value
    "numero": 500,
    "pera":700 
}
print(frutas)    #muestra el diccionario completo
frutas["granadas"]=1500    # agrega algo nuevo al diccionadio
print(frutas)

for key, value in frutas.items():   #muestra todo mas ordenadamente 
    print(key,"$",value)     


 


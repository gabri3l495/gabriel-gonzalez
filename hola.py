#declaracion de variables
#nombre="link"
#edad=64
#ejemplo de concatenacion
#print("hola", nombre, " y su edad es", edad)


#seleccion de nombre
# print("ingrese su nombre")
# nombre=input()
# print ("ingrese los numeros")


#suma de dos numeros
# n1=int(input("ingrese un numero"))
# n2=int(input("ingrese un numero"))
# print ("el resultado de la suma es", n1+n2)



#sacar promedio
# print("ingrese 3 numeros para sacar su promedio")
# n1=int(input("ingrese un numero"))
# n2=int(input("ingrese un numero"))
# n3=int(input("ingrese un numero"))
# prom=(n1+n2+n3)/3
# print("el ptromedio es", prom)

# if prom>=40:
#     print("el alumno aprobo")
# else:
#     print("el alumno reprobo")


#si es mayor o menor de edad
# print("ingrese su edad ")
# n1=int(input("ingrese su edad"))
# print("su edad es", n1)

# if n1>=18:
#     print("es mayor de edad")
# else:
#     print("es menor de edad")



# niño menor de 12
#adolecnte entre 12 y 17
#mayor de edad mas o igual a 18
# n1=int(input("ingrese su edad"))
# if edad < 12:
#     print("tiene", n1 "años por lo tanto es un niño")
# elif n1>=12 and n1<=17:
#     print("tiene", n1 "años por lo que es adolecente")
# else:
#     print("tiene", n1 "años por lo que es mayor de edad")


#ingrese 3 numeros y muestre el mayor de ellos
# n1=int(input("ingrese un numero"))
# n2=int(input("ingrese un numero"))
# n3=int(input("ingrese un numero"))
# if n1>n2 and n1>n3:
#     print(" el numero", n1 "es mayor")
# elif n2 >n3:
#     print(" el numero", n2 "es mayor"")
# else:
#     print(" el numero", n1 "es mayor")





#deletrea el nombre 
cantcar=0
v=0
cons=0
e=0
frase=input("ingrese la frase")
for i in frase:
    print(i)
    cantcar+=1
    # if i == "a" or "b" or ....
    if i.lower() in "aeiouAEIOUáéíóúÁÉÍÓÚ":
        v+=1
    elif i ==" ":
        e+=0
    else:
        cons+=1

print(f"el total de caracteres es {cantcar}")
print(f"el total de vocales es{v}")
print(f"el total de consonantes es{cons}")
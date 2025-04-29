    #numero inpar o par con cosas extras 
# num=int(input("ingrese un numero"))
# if num % 2 ==0:
#     print(num, "es par")
# else:
#     print(num, "es inpar")
# print("mostrar numeros pares")
# for i in range(1,num+1):
#     if i%2==0:
#         print(i)

# print("mostar numeros inpares")
# for i in range(1,num+1):
#     if i% 2 !=0:
#         print(i)



#ingrese numero
# opc=0
# cont=0
# total=0
# while opc!=2:
#     print("1-agregar nuevo numero")
#     print("2-salir")
#     opc=int(input("->"))
#     if(opc==1):
#         num=int(input("ingrese numero ->"))
#         cont+=1
#         total+=num
# print(f"la cantidad de numeros ingresados son {cont}")
# print(f"la suma de cada uno de ellos es {total}")


# 3 
from random import randint


a=0
b=0
r=a*b
while a < 50:
      a =int(input("ingrese el valor de a : "))
      b=randint (2,8)
      r=a*b
      print(f"el numero aleatorio es {b}")
      print(f"la multiplicacion entre {a} x {b} = {r}")
      if r < 50:
        print("intente nuevamente")
print("logro la meta wn")



num=-1
while(num<0):
    num=int(input("ingrese un numero positivo:  "))
    if(num<0):
        print("error, ingresa un numero menor a 0, vuelve a intentarlo")
print("numero ingresado")
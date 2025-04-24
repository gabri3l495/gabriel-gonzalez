#explicacion y uso de while 

#mientras
#conteo del 1 al 5
# num=0
# while num<5:
#     print("hola")
#     num+=1



# conteo en retroseso hasta un limite
# import time


# num=15
# while num>7:
#     print(num)
#     time.sleep(1)
#     num-=1

#ingresar clave
# clave=3344

# password=int(input("ingrese su clave :"))

# while clave!=password:
#     print("error")
#     password=int(input("ingrese su clave :"))
# print("usted ingreso al sistema")

#ingresa clave con 3 intentos 
# clave=3344
# intento=3
# password=int(input("ingrese su clave :"))

# while clave!=password:
#     intentos-=1
#     print(f"error, le quedan {intentos} intentos")
#     password=int(input("ingrese su clave :"))
#     if intentos <=1:
#         break

# if intentos>=0 and clave==password:
#     print("usted ingreso al sistema")
# else:
#     print("sistema bloqueado, no accedes puto/a")


#pedir al usuario numeros que s evayan sumando, mostar la suma de todos y salir del program hasta poner 0 

suma=0
while True:
    num=int(input("ingrese un numero, 0 para salir :"))
    if num==0:
        break
suma+=num
print(suma)
print(f"la suma total es {suma}")
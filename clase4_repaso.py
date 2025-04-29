# a=int(1.97)
# print(a)
# #el int se encarga de rodondear

# a=int(1h)
# print(a)
#esto daria error devido a que el 1h no es adecuado

# "%" se define como mod, me da lo que sobra
# ej:   6% 2=0


# a=int(input("elije un puto numero"))
# for i in range (1,10001):
#     print(f"{i}x{a}={i*a}")


edad=-1
while(edad<0 or edad >100):
    edad=int(input("tu edad"))
    if(edad< 0 or edad >100):
        print("error, fuera del sistema")
print("ingreso axitosamente")
print(edad)



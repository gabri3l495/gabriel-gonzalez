personas={
    1:{"nombre":"liam neeson",
       "telefono":1234567891,
       "estado civil":"soltero",
       "ciudadano":True,},
    2:{"nombre":"jose neeson",
       "telefono":1234567892,
       "estado civil":"soltero",
       "ciudadano":True,},
    3:{"nombre":"pedro neeson",
       "telefono":1234567893,
       "estado civil":"soltero",
       "ciudadano":True,},
    4:{"nombre":"sam neeson",
       "telefono":1234567894,
       "estado civil":"casado",
       "ciudadano":True,}
}
while True:
    try:
        opc=int(input('''
1- ingresar persona
2- mostrar listado
3- actualizar persona
4-borrar persona
5- salir
-> '''))
        match opc:
            case 1:
                nombre=input("ingrese un nombre ->")
                numero=int(input("telefono -> "))
                estado=int(input("1-casado   2-soltero"))
                if estado==1:
                     estadocivil="casado"
                else:
                     estadocivil="soltero"
                ciud=int(input("es ciudadano: 1-si   2_no"))
                if ciud==1:
                     ciudadadano=True
                else:
                     ciudadano=False
                ld=len(personas)+1
                personas[ld]={"nombre":nombre,                   
                            "telefono":numero,
                            "estado civil":estadocivil,
                            "ciudadano":ciudadano,}
                #de esta forma de agrega algo a los diccionarios(es diferente a las listas)                
            case 2:
                  for n,persona in personas.items():
                     print(n, persona)                               
            case 3: 
                perso=int(input("que persona decea actualizar->"))
                opc=int(input('''
1- nombre
2- numero
3- estado civil
4-es ciudadano
5- salir
-> '''))
                dato=int(input("que dato decea actualizar->")) 
                match dato:
                    case 1:
                        n=input("ingrese el nombre nuevo  ")
                        dat="nombre"
                        personas[perso][dat]= n
                    case 2:
                        num=int(input("ingrese el nuevo numero  "))
                        dat="telefono"
                        personas[perso][dat]=num
                    case 3:
                        estado=int(input("1-casado   2-soltero"))
                        if estado==1:
                            estcivil="casado"
                        else:
                            estcivil="soltero"
                        dat=estadocivil
                        personas[perso][dat]=estcivil
                    case 4:
                        ciud=int(input("es ciudadano: 1-si   2_no"))
                        if ciud==1:
                            ciuda=True
                        else:
                            ciuda=False
                        dat="ciudadano"
                        personas[perso][dat]=ciuda
                    case 5:
                        break                                                       
            case 4:
                 print("cual decea borrar")
                 for n,persona in personas.items():
                     print(n, persona) 
                 opc=int(input("-> "))
                 personas.pop(opc)
                 #el comando 'pop' si se puede utlizar en los diccionarios
            case 5:
                print("saliendo")
                break
            case _:
                print("algo paso...algo malo")
    except Exception as error:
        print(f"el error es {error}")
def validar_numero(minimo,maximo,texto):
    while True:
        try:
            opc=int(input(f"ingrese {texto}"))
            if opc < minimo or opc > maximo:
                print("error de rango")
            else:
                return opc
        except ValueError:
            print("error, otro tipo de dato")

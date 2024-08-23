mensaje = f"""
    Bienvenidos a la calculadora
    \nPara salir escriba \"Salir\"
    \nLas operaciones son:
    \nSuma
    \nResta
    \nMultiplicacion
    \nDivision
"""
print(mensaje.strip())

while True:
    n1 = input("Ingrese un numero: ")
    n2 = input("Ingrese otro numero: ")

    if n1.lower() == "salir" or n1.lower() == "salir" :
        break

    n1 = int(n1)
    n2 = int(n2) 

    operacion = ""
    resultado = 0
    operacion = input("Ingrese la operacion a realizar: ")

    if operacion.lower() == "salir":
        print("Adios....")
        break
    
    if operacion.lower() == "suma":
        resultado = n1 + n2
    elif operacion.lower() == "resta":
        resultado = n1 - n2
    elif operacion.lower() == "multiplicacion":
        resultado = n1 * n2
    elif operacion.lower() == "division":
        resultado = n1 / n2
    else:
        print("ERROR")
    
    print(resultado)

    
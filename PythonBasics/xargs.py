def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(1,2,3)
suma(2,5)
suma(1,36,54,26,3)
for numero in range(1,5):
    print(numero)

print("----------------")

for numero in range(5):
    print(numero)

print("----------------")

for numero in range(5):
    print("Hola mundo "*numero)

print("----------------")

buscar = 3

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
    else:
        print("No encontre el numero")

print("----------------")

for char in "Hola Mundo":
    print(char)
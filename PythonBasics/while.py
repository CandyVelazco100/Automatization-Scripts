numero = 1

while numero < 100:
    print(numero)
    numero *= 2

print("-----------------")

comando = ""
while comando != "salir":
    comando = input("$ ")
    print(comando)

print("-----------------")

comando = ""
while True:
    comando = input("$ ")
    if comando.lower() == "salir":
        break
    print(comando)
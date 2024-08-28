numeros = (1,2,3) + (4,5,6)
print(numeros)
punto = tuple([1,2])
menos = numeros[:2]
print(menos)
primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

listaNumeros = list(numeros)
listaNumeros.append("Hola mundi")
print(listaNumeros)

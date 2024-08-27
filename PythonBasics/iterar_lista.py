""" Listas en python son dinamicas
 """

mascotas = ["Poncho", "Ronald", "Teodoro", "Pulga"]

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)


if "Bicho" in mascotas:
    print(mascotas.index("Bicho"))

if "Poncho" in mascotas:
    print(mascotas.index("Poncho"))

mascotas.insert(1, 'Melvin')
print(mascotas)
mascotas.append('Rosita')
print(mascotas)
mascotas.remove("Pulga")
mascotas.pop()
""" mascotas.pop(1)"""
del mascotas[0]
print(mascotas)
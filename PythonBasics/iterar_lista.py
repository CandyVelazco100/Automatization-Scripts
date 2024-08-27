mascotas = ["Poncho", "Ronald", "Teodoro"]

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)


if "Bicho" in mascotas:
    print(mascotas.index("Bicho"))
    
if "Poncho" in mascotas:
    print(mascotas.index("Poncho"))
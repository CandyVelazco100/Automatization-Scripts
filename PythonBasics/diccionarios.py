""" Conexion de datos agrupados por una llave y un valor """
punto = {"x": 25, "y": 30}
print(punto)
print(punto["y"])

punto["z"] = 45
print(punto)
""" print(punto, punto["la"]) """

if "la" in punto:
    print('Encontre la', punto["la"])

print(punto.get("x"))
print(punto.get("la", 97))

del punto["x"]
del (punto["y"])
print(punto)
punto["x"] = 25

print("print(llave, punto[llave])")
for llave in punto:
    print(llave, punto[llave])

print("print(valor)")
for valor in punto.items():
    print(valor)

print("print(llave, valor)")
for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "name": "Dell"},
    {"id": 2, "name": "Juan"},
    {"id": 3, "name": "Pablo"},
    {"id": 4, "name": "Luisa"}
]

for usuario in usuarios:
    print(usuario["name"])
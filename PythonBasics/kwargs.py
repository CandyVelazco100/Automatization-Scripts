def get_product(**datos):
    print(datos)
    print(datos["id"], datos["name"])

get_product(id="23", name="IPhone", desc="Esto es un IPhone")

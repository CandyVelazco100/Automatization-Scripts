lista1 = [1,2,3,4]
""" print(1,2,3,4) """""" print(*lista) """

lista2 = [5,6] 
combinada = ["Hola", *lista1, "Mundo", *lista2]   

print(combinada)

punto1 = {"x": 19}
punto2 = {"y": 30}

nuevoPunto = {**punto1, **punto2}

print(nuevoPunto)
primer = {1,1,2,2,3,4}
""" print(primer)
primer.add(5)
primer.remove(1)
print(primer) """

segundo = [3,4,5] 
""" Parentesis cuadadrasoe es lista """

segundo = set(segundo)
print(segundo)
print(primer | segundo)

""" Interseccion """
print(primer & segundo)

""" Solo los elemetos del grupo de la izquierda """
print(primer - segundo)
print(segundo - primer)

""" Diferencia simetrica """
print(primer ^ segundo)
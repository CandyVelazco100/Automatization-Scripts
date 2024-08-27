def esPalindromo(texto):
    texto = texto.replace(" ", "").lower()
    alreves = reves(texto)

    return texto == alreves

def reves(texto):
    texto_reves = ""

    for i in range(len(texto) - 1, -1, -1):
        texto_reves += texto[i]

    return texto_reves

print("Abba", esPalindromo("Abba"))
print("Reconocer", esPalindromo("Reconocer"))
print("Hola Mundo", esPalindromo("Hola Mundo"))
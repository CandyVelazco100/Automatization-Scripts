# and, or, not

gas = True
encendido = False

if gas and encendido:
    print("Puedes avanzar AND")

if gas or encendido:
    print("Puedes avanzar OR")
    
if not gas and not encendido:
    print("Puedes avanzar AND NOT")

if not gas or not encendido:
    print("Puedes avanzar OR NOT")


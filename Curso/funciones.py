#Funcion: Es un conjunto de instrucciones que realizan un proceso-.
#Su principal ventaja es que nos ayudan a evitar codigo repetido.

def saludar():
    print("Garcia")
    print("Andrea")
    print("Evelyn")
    return "Hola"

print(saludar())

def evaluarSueldoMinimo(sueldo):
    if sueldo>=850:
        print("Cumple con el sueldo")
    else:
        print("Ganas menos que el sueldo minimo")

evaluarSueldoMinimo(100)

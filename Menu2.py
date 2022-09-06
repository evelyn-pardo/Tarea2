import os

from Curso.Conversiones import *
from Curso.Numeros_Operaciones import *
from Curso.Concatenacion import *
from Curso.Cadenas import *
from Curso.Tuplas import *
from Curso.Listas import *
from Curso.Diccionarios import *
from Curso.funciones import *
from Curso.OperadoresLogicos import *
from Curso.OperadorTernario import *
from Curso.Generadores import *
from Curso.Generadores2 import *
from Curso.Raise import *
from Curso.Modulos.modulos import *
from Curso.PruebaPaquete import *
from Curso.POO.Persona import Personas
from Curso.POO.Curso import *
from Curso.POO.Cuenta import *
from Curso.POO.Herencia import *
from Curso.POO.HerenciaMultiple import *
from Curso.POO.Polimorfismo import *
from Curso.POO.RelacionesClases import *

class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elija opcion[1...{}]:".format(len(self.opciones)))
        return opc

opc =""
while opc !="34":
    os.system("cls")
    men = Menu("Menu Operaciones",["1) Hola Mundo","2) Variables","3) Conversiones","4) Números y Operaciones Matemáticas ","5) Concatenación","6) Funciones de Cadena","7) Tuplas","8) Listas","9) Diccionarios","10) Lectura de Datos","11) Estructura Condicional","12) Funciones","13) Operadores Lógicos","14) Operadores Ternarios","15) Funcion Range","16) Bucle For","17) If con Tuplas y Listas","18) Factorial de un Número","19) Bucle While","20) Sentencia Break, Continue y Pass","21) Generadores","22) Generadores 2","23) Excepciones","24) Sentencia Raise","25) Módulos","26) Paquetes","27) POO","28) Curso y __str__","29) Método Accesores","30) Herencia, Sobreescritura de Método y Principio de Sustitución","31) Herencia Múltiple","32) Polimorfismo","33) Relaciones entre Clases","34) Salir"])
    opc = men.menu()
    if opc == "1":
        opc = ""
        # numeros = ()
        print("Hola Mundo")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "2":
        opc2 = ""
        #numeros = ()
        print("VARIABLES")
        print("25")
        print("True")
        print("205.10")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "3":
        opc3 = ""
        #numeros = ()
        print("CONVERSIONES")
        print(numero1 + numero2)
        print(num1 + num2)
        print(sueldoEntero)
        print(valorDecimal * 3)
        print(len(str(edad)))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "4":
        print("Numeros_Operaciones")
        print("Suma:",(num1 + num2))
        print("Resta:",(num1 - num2))
        print("Multiplicacion:",(num1 * num2))
        print("Division:",(num1 / num2))
        print("Division Exacta:",(num1 // num2))
        print("Potencia:",(num1 ** num2))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "5":
        #numeros = ()
        print("Concatenación")
        print(textoFinal)
        print("El saludo es: %s %s " % (texto1, texto2))
        print(saludoFinal)
        print(saludoFinal2)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "6":
        #numeros = ()
        print("Funciones de Cadena")
        print(texto)
        print(texto.lower())  # es minuscula
        print(texto.upper())  # es mayuscula
        print(texto.title())  # Convierte una cadena a un formato de titulo
        print(texto.find("al"))  # Posicion donde encuentra la caxdena o porcio.
        print(texto.count("e"))  # cantidad de ocurrencias de una letra o porcion.
        print(textoFinal)
        print(valor)
        print(cadenaSeparada)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "7":
        #numeros = ()
        print("Tuplas")
        print(tupla)
        print(tupla2)
        print(tupla3)
        print(tupla2[1])
        print(tupla2[-1])  # Acceder al ultimo elemento.
        print(tupla2[0:4])
        print(tupla2[-2])
        print(a)
        print(b)
        print(c)
        print(tuplaFinal)
        print(tuplaFinal.count(21))
        print(tuplaFinal.index(3))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "8":
        #numeros = ()
        print("LISTAS ")
        print(listas1)  # lista completa
        print(listas1[:])
        print(listas1[2])  # de la lista solo los numeros
        print(listas1[-1])
        print(listas1[0:3])
        print(listas1[:2])
        print(listas1[3:])
        print(listas1)
        print(listas1)
        print(listas1)
        print(listas1.index("Flavio"))
        print(listas1)
        print(lista3)
        print(lista2 * 4)
        print("UskokruM2010" in listas1)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "9":
        #numeros = ()
        print("Diccionario")
        print(miDiccionario["Ecuador"])
        print(miDiccionario)
        print(miDiccionario)
        print(miDiccionario)
        print(miDiccionario)
        print(dic2[24])
        print(dicPaises)
        print(datosPersonales)
        print(datosPersonales["Anios"])
        print(datosPersonales.get('Apel', "Evelyn"))
        print(datosPersonales.keys())
        print(valores)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "10":
        #numeros = ()
        print("Lectura de Datos")
        nombre = input("Ingrese su nombre:")
        edad = int(input("Ingrese su edad:"))
        sueldo = float(input("Ingrese su sueldo"))
        print("Hola," + nombre)
        edadFutura = edad + 20
        print("Tu edad es", edad)
        print("Tu edad (dentro de 20 años) sera:", edadFutura)
        print("Tu sueldo es:", sueldo)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "11":
        #numeros = ()
        print("Estructura Condicional")
        edad = int(input("Ingrese su edad:"))
        if edad >= 18:
            print("Eres mayor de edad.")
        elif edad == 18:
            print("Tienes 18 años")
        else:
            print("No eres mayor de edad.")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "12":
        #numeros = ()
        print("Funciones")
        print(saludar())
        evaluarSueldoMinimo(100)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "13":
        #numeros = ()
        print("Operadores Lógicos")
        print(not tieneBeneficio)
        print("Es mentira...")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "14":
        #numeros = ()
        print("Operadores Ternarios")
        print(sexo)
        print(sexo)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "15":
        #numeros = ()
        print("Funcion Range")
        numeros = range(5)  # [0, 1, 2, 3, 4,]
        print(numeros[1])
        numeros1 = range(4, 10)  # [4, 5, 6, 7, 8, 9, 10]
        print(numeros1[5])
        numeros2 = range(10, 100, 8)
        print(numeros2[9]) #[10, 10, 26,34, 42, 50, 58, 66, 74, 82, 90, 98]
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "16":
        #numeros = ()
        print("Bucle For")
        for i in range(1, 13):
            print(" {0} x {1} es: {2}".format(i, i, (i * i)))
        for nom in ["Karen", "Oscar", "Hector", "Leonardo"]:
            print("Cantidad de letras de (0) es: (1)".format(nom, len(nom)))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "17":
        #numeros = ()
        print("If con Tuplas y Listas")
        print("--Cursos--")
        print("Matematica - Biologia - Lenguaje - Ciencias")
        curso = input("Ingreso al curso deseado:")
        if curso in ("Matematica", "Biologia", "Lenguaje", "Ciencias"):
            print("Curso [0] seleccionado.".format(curso))
        else:
            print("No existe ese curso...")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "18":
        #numeros = ()
        print("Factorial de un Número")
        numero = int(input("Ingrese un numero: "))
        factorial = 1
        for n in range(1, (numero + 1)):
            factorial = factorial * n
        print("El factorial de {0} es: {1}".format(numero, factorial))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "19":
        #numeros = ()
        print("Bucle While")
        inicio = 2
        while inicio <= 100:
            print("Numero par: {0}".format(inicio))
            inicio += 2
        print("Hemos terminado el bucle while.")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "20":
        #numeros = ()
        print("Sentencia Break")
        for numero in range(1, 6):
            if numero <= 3:
                # Aqui no pasa nada y el bucle sigue trabajando
                pass
            print("El numero es: {0}".format(numero))
        print("Bucle terminado.")
        def funcionSinImplementar():
            pass
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "21":
        #numeros = ()
        print("Generadores")
        obtieneMultiplos7 = generadorMultiplo7(10)
        print(next(obtieneMultiplos7))
        print("Aca hay 300 lineas de codigo...")
        print(next(obtieneMultiplos7))
        print("Aca hay 100 lineas de codigo...")
        print(next(obtieneMultiplos7))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "22":
        #numeros = ()
        print("Generadores 2")
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "23":
        #numeros = ()
        print("Excepciones")
        print("Yo siempre aparezco.")
        print("Aqui termina mi programa.")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "24":
        #numeros = ()
        print("Sentencia Raise")
        evaluarNota(7)
        print("Este es el fin de mi programa")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "25":
        #numeros = ()
        print("Módulos")
        print(sumar(5, 6))
        print(multiplicar(5, 6))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "26":
        #numeros = ()
        print("Paquetes")
        print(multiplicar(5, 6))
        print(contarLetras("Jessenia"))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "27":
        #numeros = ()
        print("POO")
        per = Personas()
        per.despertar()
        print(per.despertar())
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "28":
        #numeros = ()
        print("Curso y __str__")
        cur = Curso("Matematica","2", "Ingenieria Software")
        cur.mostrarDatos()
        print(cur.mostrarDatos())
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "29":
        #numeros = ()
        print("Método Accesores")
        cuen = Cuenta()
        cuen.set_Moneda()
        cuenta1 = Cuenta("Oscar Garcia", 15000, "Soles")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_Moneda("Dolares")
        print(cuenta1.get_Moneda())
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "30":
        #numeros = ()
        print("Herencia, Sobreescritura de Método y Principio de Sustitución")
        heren = Persona("Torre","Lopez","Juan")
        heren.mostrarNombreCompleto()
        print(heren.mostrarNombreCompleto())
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "31":
        #numeros = ()
        print("Herencia Múltiple")
        mul = ClaseB("Par3", "Par4","Par5")
        print(mul)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "32":
        #numeros = ()
        print("Polimorfismo")
        poli = Docente()
        poli.describir()
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "33":
        #numeros = ()
        print("Relaciones entre Clases")
        rela = Urbanizacion("Maria de los Angeles", ciudad1)
        print(rela)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "34":
            print("Gracias por usar el sistema ")
    else:
            print("Opcion no valida")


print("Lo esperamos en una proxima ocasion")



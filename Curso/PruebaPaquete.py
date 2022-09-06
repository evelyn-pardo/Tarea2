"""
Paquetes:
Directorios (carpetas) donde se almacenan modulos relacionados entre si.

¿Para que sirve?
Para organizar mejor el codigo y poder reutilizar mejor (modularizacion y reutilizacion).

¿Como se crea un paquete?
Crear una carpeta o directorio con un archivo dentro llamado __init__.py

Lo que hace __init__.py es "convertor" un directorio en un modulo (paquete)
aue contiene otros modulos, y esto lo hace para poder importarlos.
"""

from Curso.Paquete1.funcionCadena import contarLetras
from Curso.Paquete1.funcionesNumericas import *

print(multiplicar(5, 6))
print(contarLetras("Jessenia"))
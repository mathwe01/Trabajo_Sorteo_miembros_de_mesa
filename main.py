"""Sistema de sorteo y asignación de miembros de mesa y observadores.

Programa principal: muestra el menú y llama a las funciones de los módulos
de la carpeta src/. Para ejecutarlo:  python main.py
"""

import os
import random
from datetime import datetime

from src import archivos, electores as mod_electores, sorteo, validaciones

CARPETA = os.path.dirname(os.path.abspath(__file__))
RUTA_ELECTORES = os.path.join(CARPETA, "data", "electores.txt")
RUTA_ASIGNACIONES = os.path.join(CARPETA, "data", "asignaciones.txt")
RUTA_REGISTRO = os.path.join(CARPETA, "data", "registro_sorteos.txt")


# ------------------------------------------------------------- ENTRADA DE DATOS

def pedir_dato(mensaje, validador, mayusculas=False):
    """Pide un dato por teclado y repite hasta que sea válido."""
    while True:
        texto = " ".join(input(mensaje).split())  # quita espacios sobrantes
        if mayusculas:
            texto = texto.upper()
        es_valido, error = validador(texto)
        if es_valido:
            return texto
        print("  Error:", error)


def pedir_opcion(mensaje, opciones_validas):
    """Pide una opción de menú hasta que sea una de las permitidas."""
    while True:
        texto = input(mensaje).strip()
        if texto in opciones_validas:
            return texto
        print("  Opción no válida.")


# ------------------------------------------------------------------- PANTALLAS

def mostrar_menu():
    print("\n===== SORTEO DE MIEMBROS DE MESA Y OBSERVADORES =====")
    print("1. Registrar elector")
    print("2. Buscar elector por DNI")
    print("3. Listar electores ordenados")
    print("4. Sortear miembros de mesa")
    print("5. Asignar observadores")
    print("6. Ver asignaciones de una mesa")
    print("7. Comparar algoritmos (búsqueda y ordenamiento)")
    print("0. Salir")


def nombre_por_dni(lista, dni):
    """Devuelve el nombre del elector con ese DNI (o '?' si no existe)."""
    indice, _ = mod_electores.buscar_secuencial(lista, dni)
    if indice == -1:
        return "?"
    return lista[indice]["nombre"]


def mostrar_asignaciones(lista, asignaciones):
    """Imprime una tabla con mesa, rol, DNI y nombre."""
    for mesa, rol, dni in asignaciones:
        print(f"  {mesa} | {rol:<14} | {dni} | {nombre_por_dni(lista, dni)}")
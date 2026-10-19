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

# ------------------------------------------------------------------- OPCIONES

def opcion_registrar(lista):
    print("\n--- Registrar elector ---")
    dni = pedir_dato("DNI (8 dígitos): ", validaciones.validar_dni)
    indice, _ = mod_electores.buscar_secuencial(lista, dni)
    if indice != -1:
        print("Ya existe un elector registrado con ese DNI.")
        return
    nombre = pedir_dato("Apellidos y nombres: ", validaciones.validar_nombre, True)
    edad = pedir_dato("Edad: ", validaciones.validar_edad)
    mesa = pedir_dato("Mesa (ejemplo M001): ", validaciones.validar_mesa, True)
    print("Grado de instrucción: 1=Primaria 2=Secundaria 3=Técnica 4=Universitaria")
    instruccion = pedir_dato("Opción: ", validaciones.validar_instruccion)
    veces = pedir_dato("Veces que fue miembro de mesa en 5 años: ",
                       validaciones.validar_veces)
    observador = pedir_dato("¿Es observador acreditado? (S/N): ",
                            validaciones.validar_si_no, True)

    nuevo = mod_electores.crear_elector(dni, nombre, edad, mesa, instruccion,
                                        veces, observador)
    registrado, motivo = mod_electores.registrar_elector(lista, nuevo)
    if registrado:
        archivos.agregar_elector(RUTA_ELECTORES, nuevo)
        print("Elector registrado y guardado en el archivo.")
    else:
        print("No se registró:", motivo)


def opcion_buscar(lista, asignaciones):
    print("\n--- Buscar elector por DNI ---")
    if len(lista) == 0:
        print("No hay electores registrados.")
        return
    dni = pedir_dato("DNI a buscar: ", validaciones.validar_dni)
    print("Método: 1=Secuencial  2=Binaria")
    metodo = pedir_opcion("Opción: ", ["1", "2"])
    if metodo == "1":
        indice, comparaciones = mod_electores.buscar_secuencial(lista, dni)
        encontrado = lista[indice] if indice != -1 else None
    else:
        ordenada, _ = mod_electores.ordenar_seleccion(lista, "dni")
        indice, comparaciones = mod_electores.buscar_binaria(ordenada, dni)
        encontrado = ordenada[indice] if indice != -1 else None

    if encontrado is None:
        print(f"No se encontró el DNI {dni} ({comparaciones} comparaciones).")
        return
    print(f"Encontrado en {comparaciones} comparaciones:")
    print(" ", mod_electores.texto_elector(encontrado))
    roles = sorteo.buscar_asignaciones(asignaciones, dni)
    if len(roles) == 0:
        print("  Sin asignación todavía.")
    for mesa, rol in roles:
        print(f"  Asignación: {rol} en la mesa {mesa}")


def opcion_listar(lista):
    print("\n--- Listar electores ordenados ---")
    if len(lista) == 0:
        print("No hay electores registrados.")
        return
    print("Ordenar por: 1=DNI  2=Nombre  3=Mesa")
    campo = {"1": "dni", "2": "nombre", "3": "mesa"}[pedir_opcion("Opción: ", ["1", "2", "3"])]
    print("Algoritmo: 1=Burbuja  2=Selección")
    algoritmo = pedir_opcion("Opción: ", ["1", "2"])
    if algoritmo == "1":
        ordenada, comparaciones = mod_electores.ordenar_burbuja(lista, campo)
    else:
        ordenada, comparaciones = mod_electores.ordenar_seleccion(lista, campo)
    for e in ordenada:
        print(" ", mod_electores.texto_elector(e))
    print(f"Total: {len(ordenada)} electores ({comparaciones} comparaciones).")
    

def nueva_semilla():
    """Crea una semilla y el generador aleatorio que la usa."""
    semilla = random.randrange(1, 1000000000)
    return semilla, random.Random(semilla)


def anotar_sorteo(alcance, semilla):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivos.registrar_sorteo(RUTA_REGISTRO, fecha, alcance, semilla)
    print(f"Semilla del sorteo: {semilla} (anotada en el registro de auditoría).")


def opcion_sortear(lista, asignaciones):
    print("\n--- Sortear miembros de mesa ---")
    if len(lista) == 0:
        print("No hay electores registrados.")
        return asignaciones
    print("1=Una mesa  2=Todas las mesas")
    alcance = pedir_opcion("Opción: ", ["1", "2"])
    semilla, rng = nueva_semilla()
    if alcance == "1":
        mesa = pedir_dato("Mesa (ejemplo M001): ", validaciones.validar_mesa, True)
        nuevas, mensaje = sorteo.sortear_mesa(lista, mesa, rng)
        if mensaje != "":
            print("No se pudo sortear:", mensaje)
            return asignaciones
        asignaciones = sorteo.reemplazar_asignaciones(asignaciones, nuevas,
                                                      mesas=[mesa])
        etiqueta = f"MIEMBROS {mesa}"
    else:
        nuevas, problemas = sorteo.sortear_todas_las_mesas(lista, rng)
        for p in problemas:
            print("Aviso:", p)
        if len(nuevas) == 0:
            print("No se pudo sortear ninguna mesa.")
            return asignaciones
        mesas_sorteadas = []
        for a in nuevas:
            if a[0] not in mesas_sorteadas:
                mesas_sorteadas.append(a[0])
        asignaciones = sorteo.reemplazar_asignaciones(asignaciones, nuevas,
                                                      mesas=mesas_sorteadas)
        etiqueta = "MIEMBROS TODAS"
    archivos.guardar_asignaciones(RUTA_ASIGNACIONES, asignaciones)
    anotar_sorteo(etiqueta, semilla)
    mostrar_asignaciones(lista, nuevas)
    return asignaciones


def opcion_observadores(lista, asignaciones):
    print("\n--- Asignar observadores ---")
    semilla, rng = nueva_semilla()
    nuevas, mensaje = sorteo.asignar_observadores(lista, rng)
    if mensaje != "":
        print("No se pudo asignar:", mensaje)
        return asignaciones
    asignaciones = sorteo.reemplazar_asignaciones(asignaciones, nuevas,
                                                  solo_observadores=True)
    archivos.guardar_asignaciones(RUTA_ASIGNACIONES, asignaciones)
    anotar_sorteo("OBSERVADORES", semilla)
    mostrar_asignaciones(lista, nuevas)
    return asignaciones


def opcion_ver_mesa(lista, asignaciones):
    print("\n--- Asignaciones de una mesa ---")
    mesa = pedir_dato("Mesa (ejemplo M001): ", validaciones.validar_mesa, True)
    de_la_mesa = []
    for a in asignaciones:
        if a[0] == mesa:
            de_la_mesa.append(a)
    if len(de_la_mesa) == 0:
        print("Esa mesa no tiene asignaciones todavía.")
        return
    mostrar_asignaciones(lista, de_la_mesa)


def opcion_comparar(lista):
    print("\n--- Comparación de algoritmos ---")
    if len(lista) < 2:
        print("Se necesitan al menos 2 electores registrados.")
        return
    _, c_burbuja = mod_electores.ordenar_burbuja(lista, "dni")
    ordenada, c_seleccion = mod_electores.ordenar_seleccion(lista, "dni")
    print(f"Ordenar {len(lista)} electores por DNI:")
    print(f"  Burbuja:   {c_burbuja} comparaciones")
    print(f"  Selección: {c_seleccion} comparaciones")
    peor = lista[-1]["dni"]
    _, c_sec = mod_electores.buscar_secuencial(lista, peor)
    _, c_bin = mod_electores.buscar_binaria(ordenada, peor)
    print(f"Buscar el último DNI registrado ({peor}):")
    print(f"  Secuencial: {c_sec} comparaciones")
    print(f"  Binaria:    {c_bin} comparaciones")
    

# ------------------------------------------------------------------ PRINCIPAL

def main():
    lista, lineas_con_error = archivos.cargar_electores(RUTA_ELECTORES)
    asignaciones = archivos.cargar_asignaciones(RUTA_ASIGNACIONES)
    print(f"Se cargaron {len(lista)} electores y {len(asignaciones)} asignaciones.")
    if lineas_con_error > 0:
        print(f"Aviso: se omitieron {lineas_con_error} líneas dañadas del archivo.")

    while True:
        mostrar_menu()
        opcion = pedir_opcion("Elige una opción: ", ["0", "1", "2", "3", "4", "5", "6", "7"])
        if opcion == "1":
            opcion_registrar(lista)
        elif opcion == "2":
            opcion_buscar(lista, asignaciones)
        elif opcion == "3":
            opcion_listar(lista)
        elif opcion == "4":
            asignaciones = opcion_sortear(lista, asignaciones)
        elif opcion == "5":
            asignaciones = opcion_observadores(lista, asignaciones)
        elif opcion == "6":
            opcion_ver_mesa(lista, asignaciones)
        elif opcion == "7":
            opcion_comparar(lista)
        else:
            print("Hasta pronto. Los datos ya están guardados en la carpeta data/.")
            break


if __name__ == "__main__":
    main()
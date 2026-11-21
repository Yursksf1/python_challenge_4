"""
Nombre del tema: Palabra reservada global
Objetivo de aprendizaje: Modificar una variable global desde una función cuando realmente sea necesario.
Descripción breve: La palabra reservada global indica que una asignación debe afectar la variable del ámbito global.
Conceptos que se explicarán: global, asignación local accidental, modificación global y buenas prácticas.
"""

contador = 0


# Ejemplo 1: básico. Sin global, la asignación crea una variable local.
contador_sin_global = 0


def aumentar_sin_global():
    contador_sin_global = contador_sin_global + 1
    print("Ejemplo 1 - contador local:", contador_sin_global)


# Ejemplo 2: intermedio. global permite modificar la variable real.
puntos = 100


def sumar_puntos(cantidad):
    global puntos  # Indica que puntos se refiere a la variable global.
    puntos = puntos + cantidad
    print("Ejemplo 2 - Puntos actualizados:", puntos)


# Ejemplo 3: práctico. Contador de visitas.
visitas = 0


def registrar_visita():
    global visitas
    visitas = visitas + 1
    print("Ejemplo 3 - Visitas registradas:", visitas)


if __name__ == "__main__":
    print("=== PALABRA GLOBAL ===")

    # La siguiente llamada produciría UnboundLocalError si se ejecutara.
    # La dejamos comentada para explicar el problema sin detener el programa.
    # aumentar_sin_global()
    print("Ejemplo 1 - Sin global:")
    print("La asignación contador_sin_global = contador_sin_global + 1")
    print("crea una variable local antes de leer el nombre: Python reportaría UnboundLocalError.")
    print("También puede evitarse usando una variable diferente o devolviendo un valor.")

    sumar_puntos(25)
    sumar_puntos(10)
    registrar_visita()
    registrar_visita()

    print("\nRecomendación:")
    print("- Evite global si puede pasar valores como parámetros y recuperar resultados con return.")
    print("- Use global solo cuando compartir o actualizar un estado global sea realmente necesario.")

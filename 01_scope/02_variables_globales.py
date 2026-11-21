"""
Nombre del tema: Variables globales
Objetivo de aprendizaje: Diferenciar variables globales y locales y consultar una global desde varias funciones.
Descripción breve: Una variable global se declara fuera de las funciones y puede ser visible dentro de ellas.
Conceptos que se explicarán: Declaración global, consulta desde funciones, alcance amplio y diferencia con variable local.
"""

# Variable global: se declara fuera de todas las funciones.
nombre_curso = "Python básico"


# Ejemplo 1: básico. Una función consulta la variable global.
def mostrar_curso():
    print("Ejemplo 1 - Curso:", nombre_curso)


# Ejemplo 2: intermedio. Dos funciones consultan la misma global.
def mostrar_bienvenida():
    print("Ejemplo 2 - Bienvenida al curso:", nombre_curso)


def mostrar_despedida():
    print("Ejemplo 2 - Gracias por estudiar:", nombre_curso)


# Ejemplo 3: práctico. Información global de una tienda.
nombre_tienda = "Tienda Estudiantil"
descuento = 0.10


def mostrar_producto(nombre_producto, precio):
    # Las variables locales son los parámetros y el precio final calculado.
    precio_final = precio * (1 - descuento)
    print("Ejemplo 3 -", nombre_tienda)
    print("Ejemplo 3 -", nombre_producto, "- precio con descuento:", precio_final)


if __name__ == "__main__":
    print("=== VARIABLES GLOBALES ===")
    mostrar_curso()
    mostrar_bienvenida()
    mostrar_despedida()
    mostrar_producto("Cuaderno", 12000)
    print("\nGlobal vs. local:")
    print("- Global: se declara fuera de las funciones y puede consultarse desde ellas.")
    print("- Local: se declara dentro de una función y solo existe en ese ámbito.")

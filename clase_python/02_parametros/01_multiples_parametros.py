"""
Nombre del tema: Funciones con múltiples parámetros
Objetivo de aprendizaje: Crear funciones que reciban varios parámetros y utilizar los argumentos recibidos.
Descripción breve: Un parámetro es una variable de entrada definida en la función; un argumento es el valor enviado al llamarla.
Conceptos que se explicarán: Función, parámetro, argumento, asignación de valores y múltiples parámetros.
"""


# Ejemplo 1: básico. Dos parámetros reciben dos argumentos numéricos.
def sumar(numero_uno, numero_dos):
    resultado = numero_uno + numero_dos
    print("Ejemplo 1 - Suma:", resultado)


# Ejemplo 2: intermedio. Tres parámetros representan información de una persona.
def presentar_persona(nombre, edad, ciudad):
    print("Ejemplo 2 -", nombre, "tiene", edad, "años y vive en", ciudad)


# Ejemplo 3: práctico. Precio y cantidad producen el total de una compra.
def calcular_total_compra(precio, cantidad):
    total = precio * cantidad
    print("Ejemplo 3 - Total de la compra:", total)


if __name__ == "__main__":
    print("=== FUNCIONES CON MÚLTIPLES PARÁMETROS ===")
    sumar(8, 5)
    presentar_persona("Valentina", 16, "Bogotá")
    calcular_total_compra(4500, 4)

    print("\nExplicación:")
    print("- En sumar(numero_uno, numero_dos), numero_uno y numero_dos son parámetros.")
    print("- En sumar(8, 5), 8 y 5 son argumentos.")
    print("- Python asigna 8 al primer parámetro y 5 al segundo, según el orden.")

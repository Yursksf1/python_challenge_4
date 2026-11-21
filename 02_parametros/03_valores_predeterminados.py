"""
Nombre del tema: Valores predeterminados
Objetivo de aprendizaje: Definir parámetros opcionales mediante valores predeterminados.
Descripción breve: Un parámetro con = utiliza su valor predeterminado si no recibe argumento.
Conceptos que se explicarán: Definición con =, reemplazo del valor, parámetros obligatorios y valor predeterminado.
"""


# Ejemplo 1: básico. idioma tiene un valor predeterminado.
def saludar(nombre, idioma="español"):
    print("Ejemplo 1 - Hola", nombre, "| Idioma:", idioma)


# Ejemplo 2: intermedio. cantidad es opcional.
def calcular_precio(precio, cantidad=1):
    print("Ejemplo 2 - Total:", precio * cantidad)


# Ejemplo 3: práctico. curso tiene un valor predeterminado.
def registrar_estudiante(nombre, curso="Python básico"):
    print("Ejemplo 3 -", nombre, "| Curso:", curso)


if __name__ == "__main__":
    print("=== VALORES PREDETERMINADOS ===")
    saludar("Daniel")
    saludar("Daniel", "inglés")
    calcular_precio(35000)
    calcular_precio(35000, 3)
    registrar_estudiante("Mariana")
    registrar_estudiante("Mariana", "Python intermedio")

    print("\nError de sintaxis:")
    print("Esta declaración es incorrecta:")
    print("def ejemplo(obligatorio='valor', opcional):")
    print("Explicación: Python exige que los parámetros obligatorios aparezcan antes")
    print("de los parámetros con valor predeterminado.")
    print("Forma correcta: def ejemplo(obligatorio, opcional='valor'):")

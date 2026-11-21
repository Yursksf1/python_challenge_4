"""
Nombre del tema: Visibilidad de variables
Objetivo de aprendizaje: Identificar cuándo una variable puede consultarse y cómo se resuelven nombres repetidos.
Descripción breve: La visibilidad indica desde qué partes del programa puede utilizarse una variable.
Conceptos que se explicarán: Visibilidad global y local, resolución de nombres y creación de locales con el mismo nombre.
"""

# Variable global disponible para las funciones.
nivel = "Básico"


# Ejemplo 1: básico. La función consulta una global y crea una local.
def describir_estudiante():
    nombre = "Camila"  # Variable local.
    print("Ejemplo 1 - Estudiante:", nombre)
    print("Ejemplo 1 - Nivel global:", nivel)


# Ejemplo 2: intermedio. La función crea una local con el mismo nombre.
nivel = "Básico"


def mostrar_nivel_local():
    nivel = "Avanzado"  # Esta asignación crea una variable local.
    print("Ejemplo 2 - Nivel local:", nivel)


# Ejemplo 3: práctico. La local no modifica automáticamente la global.
def cambiar_temporalmente():
    nivel = "Intermedio"  # Local por la asignación dentro de la función.
    print("Ejemplo 3 - Nivel dentro de la función:", nivel)


if __name__ == "__main__":
    print("=== VISIBILIDAD DE VARIABLES ===")
    describir_estudiante()
    print("Ejemplo 2 - Nivel global antes:", nivel)
    mostrar_nivel_local()
    print("Ejemplo 2 - Nivel global después:", nivel)
    cambiar_temporalmente()
    print("Ejemplo 3 - Nivel global final:", nivel)
    print("\nExplicación:")
    print("- Consultar nivel usa la variable global si no existe una local.")
    print("- Asignar nivel = ... dentro de una función crea una variable local.")
    print("- No modifica la global automáticamente.")

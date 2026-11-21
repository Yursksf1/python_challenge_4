"""
Título: Ejercicio 1 - Alcance de variables
Objetivo: Identificar variables locales y globales y explicar su visibilidad.
Descripción del problema:
Analiza el código propuesto. Una variable global representa el nombre del curso.
Dentro de una función existe una variable local con otro nombre.
"""

# Variable global proporcionada.
nombre_curso = "Python"


def mostrar_datos():
    # Espacio para que el estudiante identifique el alcance.
    nombre_estudiante = "Ana"
    print("Dentro de la función:")
    print("Estudiante:", nombre_estudiante)
    print("Curso:", nombre_curso)


# Requerimientos:
# 1. Ejecuta la función.
# 2. Identifica cuál variable es global y cuál es local.
# 3. Escribe tu explicación debajo.
# 4. Intenta controlar el acceso fuera de la función con try/except NameError.

# Ejemplo de ejecución esperada:
# Dentro de la función:
# Estudiante: Ana
# Curso: Python
# La variable nombre_estudiante no puede consultarse fuera de la función.

if __name__ == "__main__":
    mostrar_datos()

    # Espacio para la solución del estudiante:
    # try:
    #     print(nombre_estudiante)
    # except NameError:
    #     print("nombre_estudiante es una variable local.")

    # Pistas:
    # - Una variable declarada dentro de una función es local.
    # - Una variable declarada fuera de todas las funciones es global.
    # - NameError significa que el nombre no está disponible en el alcance actual.

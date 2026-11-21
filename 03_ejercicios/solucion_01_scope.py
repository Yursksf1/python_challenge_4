"""
Título: Solución 1 - Alcance de variables
Objetivo: Resolver el ejercicio identificando alcance y visibilidad.
Descripción: Muestra una global consultable desde una función y una local protegida por el alcance.
"""

# La variable global se declara fuera de todas las funciones.
nombre_curso = "Python"


def mostrar_datos():
    # La variable local se declara dentro de la función.
    nombre_estudiante = "Ana"
    print("Ejemplo - Dentro de la función:")
    print("Estudiante:", nombre_estudiante)
    print("Curso:", nombre_curso)
    # Una función puede leer la variable global porque su nombre es visible desde aquí.


if __name__ == "__main__":
    print("=== SOLUCIÓN: ALCANCE DE VARIABLES ===")
    mostrar_datos()

    # Al salir de la función, el programa ya no puede utilizar nombre_estudiante.
    try:
        print(nombre_estudiante)
    except NameError:
        print("Ejemplo - Error controlado: NameError.")
        print("Explicación: nombre_estudiante es local y no existe fuera de mostrar_datos().")

    print("Conclusión:")
    print("- nombre_curso es global: puede consultarse desde el programa y la función.")
    print("- nombre_estudiante es local: solo puede consultarse dentro de mostrar_datos().")

"""
Título: Solución 3 - Registro de estudiantes
Objetivo: Resolver el registro utilizando todas las formas de argumentos vistas.
Descripción: La función tiene dos parámetros obligatorios y dos parámetros con valores predeterminados.
"""


def registrar_estudiante(nombre, edad, curso="Python básico", ciudad="Sin especificar"):
    # La función imprime toda la información recibida.
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Curso:", curso)
    print("Ciudad:", ciudad)
    print("---")


if __name__ == "__main__":
    print("=== SOLUCIÓN: REGISTRO DE ESTUDIANTES ===")

    # 1. Argumentos posicionales, con ambos valores predeterminados.
    registrar_estudiante("Ana", 16)

    # 2. Argumentos posicionales que reemplazan los valores predeterminados.
    registrar_estudiante("Luis", 17, "Python intermedio", "Bogotá")

    # 3. Argumentos con nombre; el orden no importa.
    registrar_estudiante(nombre="Sofía", edad=18, ciudad="Cali")

    # 4. Combinación: nombre y edad son posicionales; ciudad es un argumento con nombre.
    registrar_estudiante("Mateo", 15, ciudad="Medellín")

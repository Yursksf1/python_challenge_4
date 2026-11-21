"""
Nombre del tema: Regla LEGB
Objetivo de aprendizaje: Comprender el orden que sigue Python para buscar una variable.
Descripción breve: Python busca nombres en Local, Enclosing, Global y finalmente Built-in.
Conceptos que se explicarán: Alcances Local, Enclosing, Global y Built-in.
"""

valor = "Global"


# Ejemplo 1: básico. Existen variables global y local con el mismo nombre.
def mostrar_local():
    valor = "Local"
    print("Ejemplo 1 - Resultado local:", valor)


# Ejemplo 2: intermedio. Función anidada y variable del ámbito externo.
def exterior():
    mensaje = "Enclosing"

    def interior():
        # Python busca primero local, después enclosing, luego global y built-in.
        print("Ejemplo 2 - Resultado enclosing:", mensaje)

    interior()


# Ejemplo 3: práctico. Funciones incorporadas: Built-in.
def identificar_built_in():
    nombres = ["Ana", "Luis", "Sofía"]
    print("Ejemplo 3 - print y len son nombres Built-in:")
    print("Ejemplo 3 - Cantidad de estudiantes:", len(nombres))


if __name__ == "__main__":
    print("=== REGLA LEGB ===")
    print("Orden: Local -> Enclosing -> Global -> Built-in")
    print("Ejemplo 1 - Resultado global:", valor)
    mostrar_local()
    exterior()
    identificar_built_in()
    print("\nExplicación:")
    print("L: variable dentro de la función actual.")
    print("E: variable en una función externa que contiene una función anidada.")
    print("G: variable declarada fuera de las funciones.")
    print("B: nombres incorporados por Python, como print(), len() y sum().")

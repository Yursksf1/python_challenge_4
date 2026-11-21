"""
Nombre del tema: Argumentos con nombre
Objetivo de aprendizaje: Utilizar argumentos con nombre y combinarlos correctamente con argumentos posicionales.
Descripción breve: Un argumento con nombre indica explícitamente a qué parámetro corresponde su valor.
Conceptos que se explicarán: Keyword Arguments, cambio de orden, combinación y reglas de sintaxis.
"""


def registrar_producto(nombre, precio, cantidad):
    total = precio * cantidad
    print("Producto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", total)


# Ejemplo 1: básico. Uso de argumentos posicionales.
def ejemplo_posicional():
    registrar_producto("Cuaderno", 12000, 2)
    print("Ejemplo 1 - Los valores siguen el orden nombre, precio, cantidad.")


# Ejemplo 2: intermedio. Uso de argumentos con nombre y otro orden.
def ejemplo_nombre():
    registrar_producto(cantidad=3, nombre="Lapicero", precio=2500)
    print("Ejemplo 2 - Los nombres permiten cambiar el orden.")


# Ejemplo 3: práctico. Combinación posicional y con nombre.
def ejemplo_combinado():
    registrar_producto("Mochila", cantidad=1, precio=85000)
    print("Ejemplo 3 - Primero se utilizan posiciones y luego nombres.")


if __name__ == "__main__":
    print("=== ARGUMENTOS CON NOMBRE ===")
    ejemplo_posicional()
    ejemplo_nombre()
    ejemplo_combinado()

    print("\nSintaxis incorrecta:")
    print("registrar_producto(nombre='Cuaderno', 12000, 2)")
    print("Explicación: no se permiten argumentos posicionales después de argumentos con nombre.")
    print("Forma correcta:")
    print("registrar_producto('Cuaderno', precio=12000, cantidad=2)")
    print("También puede escribirse:")
    print("registrar_producto(nombre='Cuaderno', precio=12000, cantidad=2)")

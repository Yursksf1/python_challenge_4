"""
Nombre del tema: Variables locales
Objetivo de aprendizaje: Comprender qué es una variable local y dónde puede utilizarse.
Descripción breve: Una variable local pertenece al alcance de la función en la que se declara.
Conceptos que se explicarán: Scope, variable local, declaración local, acceso fuera de la función y NameError.
"""


# Ejemplo 1: básico. La variable existe dentro de la función.
def mostrar_mensaje():
    # Esta variable se crea al ejecutar la función y es local.
    mensaje = "¡Hola desde una función!"
    print("Ejemplo 1 - Mensaje:", mensaje)


# Ejemplo 2: intermedio. Una función puede declarar varias variables locales.
def calcular_total_basico(precio, cantidad):
    # Las variables locales calculan el resultado únicamente dentro de la función.
    subtotal = precio * cantidad
    impuesto = subtotal * 0.19
    total = subtotal + impuesto
    print("Ejemplo 2 - Subtotal:", subtotal)
    print("Ejemplo 2 - Impuesto:", impuesto)
    print("Ejemplo 2 - Total:", total)


# Ejemplo 3: práctico, controlado. Intentar leer la variable desde fuera genera NameError.
def preparar_nombre():
    # nombre_estudiante existe solo durante esta llamada.
    nombre_estudiante = "Laura"
    print("Ejemplo 3 - Dentro de la función:", nombre_estudiante)


if __name__ == "__main__":
    print("=== VARIABLES LOCALES ===")
    mostrar_mensaje()
    calcular_total_basico(25000, 3)
    preparar_nombre()

    try:
        # El intento es controlado: fuera de la función, el nombre no existe.
        print(nombre_estudiante)
    except NameError:
        print("Ejemplo 3 - Error controlado: NameError.")
        print("Explicación: nombre_estudiante es local y termina su alcance al finalizar preparar_nombre().")

    print("\nError frecuente:")
    print("- Usar una variable local fuera de su función.")
    print("Solución: devolver el valor con return o usar la variable únicamente dentro de la función.")

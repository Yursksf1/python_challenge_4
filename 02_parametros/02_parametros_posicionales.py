"""
Nombre del tema: Parámetros posicionales
Objetivo de aprendizaje: Comprender cómo el orden de los argumentos determina el parámetro que recibe cada valor.
Descripción breve: Los argumentos posicionales se asignan de izquierda a derecha.
Conceptos que se explicarán: Posición, cambio de orden, argumentos faltantes y argumentos sobrantes.
"""


# Ejemplo 1: básico. El primer argumento corresponde al primer parámetro.
def restar(minuendo, sustraendo):
    print("Ejemplo 1 - Resultado:", minuendo - sustraendo)


# Ejemplo 2: intermedio. Cambiar el orden puede cambiar el significado del resultado.
def registrar_persona(nombre, edad, ciudad):
    print("Ejemplo 2 -", nombre, "|", edad, "años |", ciudad)


# Ejemplo 3: práctico. Precio, cantidad y descuento no deben cambiar de posición.
def calcular_precio_producto(precio, cantidad, descuento):
    total = precio * cantidad
    total_con_descuento = total - (total * descuento)
    print("Ejemplo 3 - Total con descuento:", total_con_descuento)


if __name__ == "__main__":
    print("=== PARÁMETROS POSICIONALES ===")
    restar(20, 7)
    registrar_persona("Mateo", 17, "Medellín")
    registrar_persona("Medellín", 17, "Mateo")  # Orden incorrecto: las posiciones no coinciden.
    calcular_precio_producto(8000, 3, 0.10)

    print("\nErrores TypeError controlados:")
    try:
        restar(20)  # Falta el argumento obligatorio sustraendo.
    except TypeError as error:
        print("Falta un argumento:", error)

    try:
        restar(20, 7, 5)  # Se envía un argumento que no está permitido.
    except TypeError as error:
        print("Sobran argumentos:", error)

    print("Solución: enviar exactamente un argumento por cada parámetro obligatorio.")

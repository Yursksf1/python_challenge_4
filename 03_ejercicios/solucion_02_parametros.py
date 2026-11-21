"""
Título: Solución 2 - Área y perímetro de un rectángulo
Objetivo: Resolver el cálculo usando una función con múltiples parámetros.
Descripción: Recibe base y altura, calcula área y perímetro y muestra los resultados.
"""


def calcular_rectangulo(base, altura):
    # Los parámetros base y altura reciben los valores enviados en cada llamada.
    area = base * altura
    perimetro = 2 * (base + altura)

    print("Base:", base, "| Altura:", altura)
    print("Área:", area)
    print("Perímetro:", perimetro)
    print("---")


if __name__ == "__main__":
    print("=== SOLUCIÓN: ÁREA Y PERÍMETRO ===")

    # Primera llamada: los argumentos se asignan por posición.
    calcular_rectangulo(5, 3)

    # Segunda llamada: se usan argumentos con nombre.
    calcular_rectangulo(base=8, altura=4)

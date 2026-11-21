# Python: Alcances y funciones con múltiples parámetros

Material educativo en español para explicar el alcance de las variables y la creación y uso de funciones con múltiples parámetros en Python. El contenido está organizado para una clase virtual, con ejemplos progresivos, errores controlados y ejercicios prácticos.

## Información del profesor

**Nombre:** Yurley Sánchez.

**Profesión:** Ingeniera de Sistemas.

**Perfil:** Desarrolladora Full Stack, con experiencia en desarrollo de software, programación con Python y JavaScript, desarrollo backend y frontend, bases de datos y formación en programación.

**Rol:** Docente y facilitadora de formación en programación y desarrollo de software.

- LinkedIn del profesor: [Agregar enlace]
- GitHub del profesor: [Agregar enlace]
- Correo de contacto: [Agregar correo]

## Grabación de la clase

**YouTube:** [Agregar aquí el enlace de la grabación]

## Objetivos de aprendizaje

Al finalizar la clase, el estudiante podrá:

- Comprender el alcance de las variables en Python.
- Diferenciar variables locales y globales.
- Comprender la visibilidad de las variables.
- Utilizar correctamente la palabra reservada `global`.
- Crear funciones con múltiples parámetros.
- Utilizar parámetros posicionales.
- Definir parámetros con valores predeterminados.
- Utilizar argumentos con nombre.

## Requisitos previos

El estudiante debe conocer variables, tipos de datos, operadores, condicionales, ciclos y conceptos básicos de funciones en Python.

## Índice de contenidos

### 4.4 Alcances en Python

- [Scope](#scope)
- [Variables locales](#variables-locales)
- [Variables globales](#variables-globales)
- [Visibilidad de variables](#visibilidad-de-variables)
- [Palabra reservada global](#palabra-reservada-global)
- [Regla LEGB](#regla-legb)

### 4.5 Creación de funciones con múltiples parámetros

- [Parámetros y argumentos](#parametros-y-argumentos)
- [Funciones con múltiples parámetros](#funciones-con-multiples-parametros)
- [Parámetros posicionales](#parametros-posicionales)
- [Valores predeterminados](#valores-predeterminados)
- [Argumentos con nombre](#argumentos-con-nombre)

### Práctica

- [Ejercicio 1: Alcance de variables](#ejercicio-1-alcance-de-variables)
- [Ejercicio 2: Funciones con múltiples parámetros](#ejercicio-2-funciones-con-multiples-parametros)
- [Ejercicio 3: Registro de estudiantes](#ejercicio-3-registro-de-estudiantes)
- [Soluciones](#soluciones)

## Resumen teórico

### Scope

El *scope* o alcance determina dónde existe un nombre de variable y desde qué partes del programa puede consultarse.

### Variables locales

Una variable local se declara dentro de una función. Solo existe y puede consultarse dentro de esa función.

```python
def mostrar_saludo():
    mensaje = "Hola"
    print(mensaje)
```

Intentar usar `mensaje` fuera de `mostrar_saludo()` produce `NameError`.

### Variables globales

Una variable global se declara fuera de todas las funciones y puede consultarse desde diferentes funciones.

```python
curso = "Python"

def mostrar():
    print(curso)
```

| Característica | Variable local | Variable global |
|---|---|---|
| Lugar de declaración | Dentro de una función | Fuera de las funciones |
| Visibilidad | Solo dentro de la función | Dentro del archivo o módulo |
| Duración | Mientras se ejecuta la función | Mientras se ejecuta el programa |
| Riesgo | Bajo para compartir datos | Mayor: puede modificarse desde varios lugares |

### Visibilidad de variables

Python empieza a buscar un nombre desde el ámbito local. Si no lo encuentra, continúa hacia ámbitos externos.

Asignar el nombre dentro de una función crea una variable local, incluso si ya existe una global con ese nombre.

```python
mensaje = "Global"

def ejemplo():
    mensaje = "Local"
    print(mensaje)  # Local
```

### Palabra reservada global

La palabra `global` permite modificar una variable global desde una función.

```python
puntos = 0

def sumar_puntos(cantidad):
    global puntos
    puntos = puntos + cantidad
```

Aunque `global` puede ser útil, es preferible pasar datos como parámetros y devolver resultados con `return`.

### Regla LEGB

Python busca los nombres siguiendo el orden LEGB:

| Letra | Significado | Ejemplo |
|---|---|---|
| L | Local | Variable dentro de la función actual |
| E | Enclosing | Variable de una función externa que contiene otra función |
| G | Global | Variable fuera de las funciones |
| B | Built-in | Nombre incorporado por Python, como `print` o `len` |

```python
nombre = "Global"

def exterior():
    nombre = "Enclosing"

    def interior():
        nombre = "Local"
        print(nombre)
```

### Parámetros y argumentos

Un parámetro es el nombre definido en la declaración de una función. Un argumento es el valor enviado al llamar la función.

```python
def sumar(numero_uno, numero_dos):  # parámetros
    return numero_uno + numero_dos

resultado = sumar(4, 7)  # argumentos
```

### Funciones con múltiples parámetros

Una función puede recibir varios parámetros separados por comas.

```python
def presentar(nombre, edad, ciudad):
    print(nombre, edad, ciudad)
```

### Parámetros posicionales

Los argumentos posicionales se asignan según su posición, de izquierda a derecha.

```python
def restar(a, b):
    print(a - b)

restar(10, 3)  # a recibe 10 y b recibe 3
```

### Valores predeterminados

Un parámetro puede tener un valor que se utiliza si no se envía un argumento.

```python
def registrar(nombre, curso="Python básico"):
    print(nombre, curso)
```

Los parámetros obligatorios deben declararse antes que los parámetros con valor predeterminado.

### Argumentos con nombre

Los argumentos con nombre indican explícitamente el parámetro al que corresponden.

```python
def registrar(nombre, edad):
    print(nombre, edad)

registrar(edad=16, nombre="Ana")
```

## Referencias a los archivos de código

### Alcances

- [Variables locales](01_scope/01_variables_locales.py) — Scope, variables locales y acceso controlado a `NameError`.
- [Variables globales](01_scope/02_variables_globales.py) — Declaración y consulta global desde varias funciones.
- [Visibilidad de variables](01_scope/03_visibilidad_variables.py) — Resolución de nombres y nombres repetidos.
- [Palabra global](01_scope/04_palabra_global.py) — Modificación de globales y buenas prácticas.
- [Regla LEGB](01_scope/05_regla_legb.py) — Orden Local, Enclosing, Global y Built-in.

### Parámetros

- [Múltiples parámetros](02_parametros/01_multiples_parametros.py) — Parámetros, argumentos y funciones de varios datos.
- [Parámetros posicionales](02_parametros/02_parametros_posicionales.py) — Orden, argumentos faltantes y sobrantes.
- [Valores predeterminados](02_parametros/03_valores_predeterminados.py) — Parámetros opcionales con `=`.
- [Argumentos con nombre](02_parametros/04_argumentos_nombre.py) — Keyword Arguments y combinación de estilos.

### Ejercicios

- [Ejercicio 1: Alcance de variables](03_ejercicios/ejercicio_01_scope.py) — Identificación de variables locales y globales.
- [Solución 1: Alcance de variables](03_ejercicios/solucion_01_scope.py) — Resolución comentada del alcance.
- [Ejercicio 2: Rectángulo](03_ejercicios/ejercicio_02_parametros.py) — Área y perímetro con múltiples parámetros.
- [Solución 2: Rectángulo](03_ejercicios/solucion_02_parametros.py) — Implementación comentada.
- [Ejercicio 3: Registro de estudiantes](03_ejercicios/ejercicio_03_argumentos.py) — Argumentos posicionales y con nombre.
- [Solución 3: Registro de estudiantes](03_ejercicios/solucion_03_argumentos.py) — Implementación comentada.

## Cómo ejecutar los ejemplos

Desde la carpeta `clase_python`, puede ejecutar cada archivo con Python:

```bash
python 01_scope/01_variables_locales.py
python 02_parametros/01_multiples_parametros.py
python 03_ejercicios/solucion_01_scope.py
```

En Windows, si `python` no está configurado, pruebe:

```bash
python .\01_scope\01_variables_locales.py
```

En Linux o macOS, o si el entorno utiliza Python 3 directamente:

```bash
python3 01_scope/01_variables_locales.py
```

Desde la raíz del repositorio también puede indicar la ruta completa del proyecto educativo:

```bash
python clase_python/01_scope/01_variables_locales.py
```

No se requieren instalaciones adicionales ni librerías externas.

## Preguntas frecuentes

### ¿Cuál es la diferencia entre una variable local y una global?

La local se declara dentro de una función y solo existe en su alcance. La global se declara fuera de las funciones y puede consultarse desde varias partes del archivo.

### ¿Por qué no puedo acceder a una variable local desde fuera de una función?

Al finalizar la función, su variable local deja de existir en ese contexto. En su lugar, devolvemos el dato con `return`.

### ¿Para qué sirve `global`?

Sirve para indicar que una asignación debe modificar una variable global desde una función.

### ¿Qué diferencia existe entre un parámetro y un argumento?

El parámetro forma parte de la declaración de la función. El argumento es el valor concreto que se envía al llamarla.

### ¿Qué sucede si cambio el orden de los argumentos posicionales?

Los valores se asignan a los parámetros según la posición. Cambiar el orden puede producir resultados incorrectos o sin sentido.

### ¿Qué es un valor predeterminado?

Es el valor que utiliza un parámetro si la llamada no proporciona un argumento para él.

### ¿Cuándo debo utilizar argumentos con nombre?

Son útiles cuando hay varios parámetros, cuando se desea aumentar la claridad o cuando se quiere enviar los datos en un orden distinto al posicional.

## Errores frecuentes

### NameError

Ocurre al usar un nombre que no está disponible en el alcance actual.

```python
def ejemplo():
    dato = "Local"

ejemplo()
print(dato)  # NameError
```

Solución: declarar la variable en el alcance necesario o devolverla con `return`.

### TypeError

Ocurre al enviar una cantidad o tipo incorrecto de argumentos.

```python
def sumar(a, b):
    print(a + b)

sumar(3)  # Falta un argumento.
```

Solución: enviar todos los argumentos obligatorios y no enviar argumentos sobrantes.

### Error de sintaxis al declarar parámetros

Los parámetros obligatorios deben aparecer antes de los predeterminados.

```python
# Incorrecto
def ejemplo(opcional="sí", obligatorio):
    pass

# Correcto
def ejemplo(obligatorio, opcional="sí"):
    pass
```

### Uso incorrecto de global

Sin `global`, una asignación dentro de una función puede crear una variable local.

Solución: utilizar `global` solo cuando sea necesario modificar el estado global; preferir parámetros y `return`.

### Orden incorrecto de argumentos

Los argumentos posicionales no pueden aparecer después de argumentos con nombre.

```python
# Incorrecto
def registrar(nombre, edad):
    pass

registrar(nombre="Ana", 16)

# Correcto
registrar("Ana", edad=16)
```

## Buenas prácticas

- Use nombres descriptivos para funciones y variables.
- Utilice parámetros para reutilizar una función con diferentes datos.
- Evite variables globales si el problema puede resolverse con parámetros y `return`.
- Utilice funciones cortas con una responsabilidad clara.
- Prefiera argumentos con nombre cuando varios parámetros puedan confundirse.
- Declare primero los parámetros obligatorios y después los parámetros opcionales.
- Capture errores solo en ejemplos didácticos o situaciones donde se espere que ocurran.

## Documentación oficial

- [Tutorial de funciones](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Parámetros y argumentos](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [Ámbitos y espacios de nombres](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Referencia de expresiones](https://docs.python.org/3/reference/expressions.html)

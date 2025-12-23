"""
Funcioes definidas por el usuario
"""

# Simple


def greet():
    print("Hola, Python")


greet()

# Con retorno -devuelve algo


def return_greet():
    return "Hola con retorno"


print(
    return_greet()
)  # si no se coloca los corchetes imprime la direccion de la memoria.

# con argumento- que le podemos pasar parametros a la funcion


def arg_greet(name):
    print(f"Hola, {name}")


arg_greet("Juli")


# con argumento predeterminado
def default_arg_greet(name="Python"):
    print(f"Hola, {name}")


default_arg_greet("Juli2")
default_arg_greet()

# con argumento y retorno


def return_arg_greet(greet, name):
    return f"{greet},{name}"


print(return_arg_greet("Hi", "Brais"))

# con retorno de varios valores
"""
En python no se retornan dos cosas separadas , se retorna una sola cosa
"""


def multiple_return_greet():
    return "Hola", "retorno de valores"  # retorna una tupla (hola, retorno de valores)


greet, name = multiple_return_greet()  # desempaquetado
print(greet)
print(name)

# con un numero variables de argumentos


def variable_arg_greet(
    *names,
):  # con el asterisco puedo pasarle todos los argumentos que quieras
    for name in names:
        print(f"Holam {name}")


variable_arg_greet("python", "brais", "juli", "comunidad")


# con numero variable de argumentos con palabra clave
def variable_key_arg_greet(
    **names,
):  # con el asterisco puedo pasarle todos los argumentos que quieras
    for param, name in names:
        print(f"Holam {name} ({param})!")


variable_arg_greet(
    language="python", name="brais",
    student="juli", age_teacher="36"
    )

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
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    language="python", name="brais",
    student="juli", age_teacher="36"
    )
"""
Funciones dentro de funcioes
"""

def outer_function ():
    def inner_function():
        print("Funcion interna: Hola, Python ! dentro de la funcion")
    inner_function()
outer_function()
"""
Funciones del lenguaje (built-in), funciones que ya estan creadas dentro del lenguaje,
por ejemplo print, len, type
"""
print(len("Juliana"))
print(type(36))
print("Juliana".upper())

"Variables locales y globales"
global_var ="Python"
def hello_python():
    local_var="hola"
    print(f"{local_var},{global_var}")

print(global_var)
#print(local_var) # no imprime porque la variable esta dentro de una funcion
hello_python()

"""
Extra
crea una funcion que reciba dos parametros de tipo cadena de texto y retornu numeros.
la funcion imprime todos los numeros del 1 al 100 teniendo en cuenta:
si el mumero es multiplo de 3, muestra la cadena de texto del primer parametro
si el mumero es multiplo de 5, muestra la cadena de texto del segundo parametro
si el mumero es multiplo de 3 y 5, muestra las dos cadenas de texto concatenados
la funcion retorna el numero de veces que se a impreso el numero en lugar de los textos

"""

def print_number(text_1, text_2) -> int:
    count=0
    for number in range (1,101):
        if number %3 ==0 and number % 5 ==0:
            print(text_1+""+text_2)
        elif number %3 ==0:
            print(text_1)
        elif number %5 ==0:
            print(text_2)
        else:
            print(number)
            count +=1
    return count
print (print_number("Fizz", "Buzz"))
#Comentario , en python se hacen comentarios de una linea con el simbolo # y de varias lineas con """ """
#url oficial de python https://www.python.org/
""" Esto es una comentario 
en varias lineas """

''' Las comillas simples tambien 
se pueden usar para comentarios en varias lineas'''

#VARIABLES
#En python no es necesario declarar el tipo de variable

my_variable = "mi variable"
my_variable = "nuevo valor de la variable"

'''En python no existe las constantes todos los datos que se crea pueden mutar,
pero se puede simular con variables en mayusculas MY_CONSTANT = "valor"
'''
MY_CONSTANT = 100

"Python tiene tipos de datos primitivos como: int, float, str, bool"

my_int = 5 # numero entero, que no tiene decimales
my_float = 5.5 # numero decimal o flotante
my_bool = True # True o False
my_str = "Hola mundo" # cadena de texto

""" En python para imprimir texto por consola se usa la funcion print() """

print("Hola gente, el lenguaje de programacion python es muy facil de aprender")

#Note : python es un lenguaje debilmente tipado, es decir que no es necesario declarar el tipo de variable

#Para saber que tipo de variable es se usa la funcion type()

print(type(my_int)) # <class 'int'>
print(type(my_float)) # <class 'float'>
print(type(my_bool)) # <class 'bool'>
print(type(my_str)) # <class 'str'>

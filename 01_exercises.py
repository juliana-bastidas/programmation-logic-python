#\nEjercicio 1: Imprimir mensajes

#1.Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas

#name = input("Cúal es tu nombre: ")
#city = input("Cúal es tu ciudad: ")

#print(f"Hola me llamo {name} \ny soy de la ciudad de {city}")

#2 Usa el comando 'type()' para determinar el tipo de datos de cada variable.
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(f"variable a es de tipo a:_{type(a)}")
print(f"variable b es de tipo b:_{type(b)}")
print(f"variable c es de tipo c:_{type(c)}")
print(f"variable d es de tipo d:_{type(d)}")
print(f"variable e es de tipo e:_{type(e)}")

#Convierte la cadena \"12345\" a un entero y luego a un float. 
#"Convierte el float 3.99 a un entero. ¿Qué ocurre?"

cadena = "12345"
convert_int = int(cadena)
convert_float = float(convert_int)

float_number = 3.99
convert_int_2= int(float_number)

print("Float original:", float_number)
print("Float convertido a entero (se trunca la parte decimal):",convert_int_2)

#4 Crea variables para tu nombre, edad y altura.

name = "juliana"
age =32
height = "1.75 metros"

print (f" Hola me llamo {name} tengo {age} años y mido {height}")

""" 5. Crea una variable con el número PI (sin asignar una variable)
Redondea el número con round()
Haz la división entera entre el número que te salió y el número 2
el resultado debe ser 1.
"""

pi = 3.1416
round_pi = round(pi) #3
convert_int_pi = int(round_pi) #3
divide = convert_int_pi/2 #3/2 la division en python siempre devuelve un float

print (f"el resultado de la división es {divide}")

resultado = int(round(3.1416) / 2) # primero hace el round, 3, luego la diviosion 1.5 pero el entero lo trunca
print(resultado)
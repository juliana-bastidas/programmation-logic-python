""" EXCEPCIONES TRY CATCH en python es try except"""

try:
    print(10/0)
    print("Esto no se imprime")
except Exception as e:
    print(f"Se ha producido un error:{e}")

print("Esto si se imprime")

#error list index out or range

try:
    print(10/1)
    my_list= [1,2,3,4]
    print(my_list[4])
except Exception as e:
    print(f"Se ha producido un error:{e} ({type(e).__name__})")

"""EXTRA
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado.

"""
class SrtTypeError (Exception):
    pass
def process_params (parameters: list):
    if len(parameters) <3:
        raise IndexError()
    elif parameters [1] ==0:
        raise ZeroDivisionError
    elif type(parameters[2])==str:
        raise SrtTypeError ("El segundo elemento no puede ser una cadena de texto!!")
    
    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2]+ 5)

try:
    process_params([1,2,4,3])
    #process_params([1,2,"brais",3])
    
#captura de excepciones concretas de un tipo concreto desencadenando el codigo adaptado al tipo de error
except IndexError:
    print("El numero de elementos de la lista debe ser mayor que dos")
except ZeroDivisionError:
    print("El segundo elemento de la lista no puede ser cero")
except SrtTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado : {e}")
else: 
    print("No se ha producido ningún error")
finally: # si o si al final se va al final 
    print("El programa a finalizado")
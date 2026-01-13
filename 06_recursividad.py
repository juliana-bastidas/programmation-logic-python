"""RECURSIVIDAD
Es una función que se llama a ella misma
"""


def countdown (number: int):
    if number >=0:
        
        print(f"al inicio {number}")
        countdown(number-1)
        print(f"al final{number}")

countdown(5)

def levels(n):
    if n == 0:
        return

    print("Entrando al nivel", n)
    levels(n - 1)
    print("Saliendo del nivel", n)

levels(3)

def sum_recursive(num):
    if num == 1:  # Base case
        return num
    return num + sum_recursive(num - 1)  # Recursive case
    
print(sum_recursive(3)) # 3 + 2 + 1 

"""EXTRA
 Utiliza el concepto de recursividad para:
 Calcular el factorial de un número concreto (la función recibe ese número).
 Calcular el valor de un elemento concreto (según su posición) en la 
 sucesión de Fibonacci (la función recibe la posición).
"""
"""La recursividad se puede utilizar cuando una funcion se pueda dividir en subproblemas dentro del problema
general

"""
def factorial (number:int)->int:
    if number < 0 :
        print("Los numero negativos no son validos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number-1)
    
print(factorial(5))

def fibonacci (number:int)-> int:
    if number <= 0 :
        print("La posicion debe ser mayor a 0 ")
        return 0
    elif number == 1:
        return 0
    elif number ==2:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)
print(fibonacci(5))        
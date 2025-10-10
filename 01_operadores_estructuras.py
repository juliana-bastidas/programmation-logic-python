'''
OPERADORES
'''

# Operadores aritméticos   +, -, *, /, //, %, **
sum = 10 + 3
print (f"Suma: 10 + 3 = {10 + 3}")
print (f"Suma 2: 10 + 3 = {sum}")

print (f"Resta: 10 - 3 = {10 - 3}")
print (f"Multiplicación: 10 * 3 = {10 * 3}")
print (f"División: 10 / 3 = {10 / 3}")
print (f"División entera: 10 // 3 = {10 // 3}")
print (f"Modulo: 10 % 3 = {10 % 3}")
print (f"Exponente: 10 ** 3 = {10 ** 3}") 

# Operadores de comparación
print (f"igualdad: 10 == 3 = {10 == 3}")
print (f"Desigualdad: 10 != 3 = {10 != 3}")
print (f"Mayor que: 10 > 3 = {10 > 3}")
print (f"Menor que: 10 < 3 = {10 < 3}")
print (f"Mayor o igual que: 10 >= 3 = {10 >= 3}")
print (f"Menor o igual que: 10 <= 3 = {10 <= 10}")

# operadores logicos 
print (f"AND &&: 10 + 3 == 13 and 5-1 ==4 es {10 + 3 == 13 and 5-1 ==4}")
print (f"OR ||: 10 + 3 == 13 OR 5-1 ==4 es {10 + 3 == 14 or 5-1 ==4}")
print (f"NOT !: 10 + 3 == 14 {not 10 + 3 == 14} ")

# operadores de asignación
my_number = 10 # el igual sirbe para asignar un valor a una variable
print (f"my_number: {my_number}")
my_number += 3 # suma y asignacion 
print(my_number)
my_number -= 2 # resta y asignacion
print(my_number)
my_number *= 2 # multiplicacion y asignacion
print(my_number)
my_number /= 2 # division y asignacion
print(my_number)
my_number //= 2 # division entera y asignacion
print(my_number)
my_number %= 2 # modulo y asignacion
print(my_number)

#operadores de identidad: sirven para comparar el valor no da la variable si no la direccion o posicion de la memoria
my_new_number = 1.0 
print (f"my_number is my_new_number: {my_number is my_new_number}")

my_new_number = my_number
print (f"my_number is my_new_number: {my_number is my_new_number}")

#operadores de pertenencia: sirven para saber si algo pertenece a algo, no existe en todos los lenguajes
print(f"'u' in 'curso'= {'u' in 'curso'}")
print(f"'b' not in 'curso'= {'u' not in 'curso'}")

#operadores de bit a bit: operan a nivel de bits
a = 10 # 1010
b = 3 # 0011

print(f"AND 10 & 3 = {a & b}") # 0010
print(f"OR 10 & 3 = {a | b}") # 1011
print(f"XOR 10 & 3 = {a ^ b}") # 1001
print(f"Not: ~10 = {~a}") # 0101
print(f"Desplazamiento a la izquierda 10 << 2 = {a << 2}") # 101000
print(f"Desplazamiento a la derecha 10 >> 2 = {a >> 2}") # 0010

s="hola mundo"
print(s[2])
print(s[-1])
print(s[::1])
print(s[::2])
print(s.upper())
print(s.split())
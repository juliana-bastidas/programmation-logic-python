"""MANEJO DE FICHEROS"""

import os

#os modulo que nos permite compartir con nuestro sistema operativo
#el with se encargca de cerrar el fichero

#creando un fichero 

file_name = "mouredev.txt"

#escribir fichero
with open(file_name, "w") as file:
    file.write("Brais \n")
    file.write("36\n")
    file.write("python")

    #leyendo el fichero 
with open(file_name, "r") as file:
    print(file.read())  

#borrando el fichero
#os.remove(file_name)

"""EXTRA

Desarrolla un programa de gestión de ventas que almacena sus datos en un 
archivo .txt.
- Cada producto se guarda en una línea del archivo de la siguiente manera:
  [nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
  actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.
"""

file_name = "mouredev_shop.txt"
open(file_name, "a")
while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar producto")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("Selecciona una opcion:")

    if option == "1":
        name = input ("Nombre: ").strip()
        quantity = input ("Cantidad: ").strip()
        price = input ("Precio: ").strip()

        #la a permite seguir enlistando
        with open(file_name, "a") as file: 
            file.write(f"{name}, {quantity}, {price}\n")
    elif option == "2":
        name = input ("Nombre: ").strip()
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] ==name:
                    print(line)
                    break
    elif option == "3":
        name = input ("Nombre: ").strip()
        quantity = input ("Cantidad: ").strip()
        price = input ("Precio: ").strip()
        with open(file_name, "r") as file:
            lines_copy = file.readlines() # leyo todas las linea y crea una copia
        with open (file_name, "w") as file:
            for line in lines_copy:
                if line.strip().split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
    elif option == "4":
        name = input ("Nombre: ").strip()
        with open(file_name, "r") as file:
            lines_copy = file.readlines()
        with open (file_name, "w") as file:
            for line in lines_copy:
                if line.strip().split(", ")[0] != name:
                    file.write(f"{name}, {quantity}, {price}\n")

    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(",") 
                quantity = int(components[1])
                price = float(components[2])
                total += quantity*price
        print(f"El total es: {total}")
    elif option == "7":
        total = 0
        name = input ("Nombre: ").strip()
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(",") 
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity*price
                    break
        print(f"El total es: {total}")
    elif option == "8":
        #os.remove(file_name)
        break
    else:
        print("Seleccione una opcion valida")
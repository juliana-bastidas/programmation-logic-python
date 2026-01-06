"""ESTRUCTURAS DE DATOS"""

#Listas
my_list = ["Brais", "Juli", "wolfy", "visionos"]
print(type(my_list))
print(my_list)
my_list.append("castor nuevo") #Insercion
print(my_list)
my_list.remove("Brais") #Eliminacion
print(my_list[1]) # Acceso
my_list[1]="Cuervo" #Actualizacion
my_list.sort() #Ordenacion alfabetica

#Tuplas
my_tuple =("Brais", "Moure", "@mouredev","36")
print(my_tuple[2])
print(my_tuple[3])
my_tuple=tuple(sorted(my_tuple)) #Ordenacion de tuplas con el truco de tuple el sorted vuelve todo string
print(type(my_tuple))

#Sets
my_set:set={"Brais", "Moure","@mouredev","36"}
my_set.add("coreo@gmail.com") #Insercion
my_set.add("coreo@gmail.com") #No permite datos duplicados
my_set.remove("Brais") #Eliminacion
my_set= set(sorted(my_set)) #LOS SET NO SE PUEDEN ORDENAR 
print(type(my_set))

#Diccionario
my_dict:dict = {"name":"Brais", "surname":"Moure", "email":"@mouredev","age":"36"}
print(my_dict["name"]) #Acesso
my_dict["email"]="nuevocorreo@example.com" #Actualizacion
del my_dict["surname"] #Eliminacion
print(my_dict)
my_dict= dict(sorted(my_dict.items()))
print(my_dict)
print(type(my_dict))

"""EXTRA

 Crea una agenda de contactos por terminal.
 * Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * Cada contacto debe tener un nombre y un número de teléfono.
 * El programa solicita en primer lugar cuál es la operación que se quiere realizar,
y a continuación los datos necesarios para llevarla a cabo.
 * El programa no puede dejar introducir números de teléfono no numéricos y con más
de 11 dígitos (o el número de dígitos que quieras).
 * También se debe proponer una operación de finalización del programa.
"""

def my_agenda():
    agenda ={}
    while True:
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir contacto")
        option = input("\nSelecciona una opcion: ")

        match option:
            case "1":
                name = input ("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El numero de telefono de {name} es {agenda[name]}")
                else:
                    print (f"el contacto {name} no existe")
            case "2":
                name = input ("Introduce el nombre del contacto: ")
                phone = input( "Introduce el telefomno del contacto")
                if phone.isdigit() and len(phone) > 0 and len(phone)<=11:
                    agenda[name] = phone
                else:
                    print ("Debes introducir un numero de telefono con menos de 12 digitos")
            case "3":
                pass
            case "4":
                pass
            case "5":
                print("Saliendo de la agenda")
                break
            case _:
                print("Opcion no valida. Elige una opcion del 1 al 5")

my_agenda()
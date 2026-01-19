"""HERENCIA Y POLIMORFISMO"""

class Animal:
    def __init__(self, name:str):
        self.name = name
    def sound(self):
        #print("Algun sonido")
        pass

#Subclases 
class Dog (Animal):
    def sound(self):
        print ("Guau")
class Cat (Animal):
    def sound(self):
        print( "Miua")

# my_animal= Animal("Animal")
# my_animal.sound()
# my_dog = Dog ("Perro")
# my_dog.sound()
# my_cat = Cat ("Gato")
# my_cat.sound()

#Polimorfismo

def print_sound(animal:Animal):
    animal.sound()

my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = Dog ("Perro")
print_sound(my_dog)
my_cat = Cat ("Gato")
print_sound(my_cat)

"""EXTRA:
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo
"""

class Employee:
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
        self.employees = []
    def add (self, employee):
        self.employees.append(employee)

    def print_employess (self):
        for employee in self.employees:
            print(employee.name)

class Manager(Employee):
    def cordinate_project(self):
        print(f"{self.name} esta coordinando todos los proyectos de la empresa")
 
class ProjectManager(Employee):

    def __init__(self,id:int, name:str ,project:str):
        super().__init__(id, name)
        self.project = project
    def cordinate_project(self):
        print(f"{self.name} esta coordinando el proyecto ")

class Programmer(Employee):
    def __init__(self,id:int, name:str ,language:str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} esta programando en ")

    def add(self, employee:Employee):
        print (f"Un programador no tiene empleados a su cargo. {employee.name} no sé añadirá.")

## empleados generales

my_manager = Manager(1, "MoureDev")
my_project_manager = ProjectManager(2,"Brais", "Proyecto1")
my_project_manager2 = ProjectManager(3,"Moure", "Proyecto2")
my_programmer = Programmer(4, "kontrol", "Swift")
my_programmer2 = Programmer(5, "ros","cobol")
my_programmer3 = Programmer(6, "bushi", "dart")
my_programmer4 = Programmer(7, "nasos", "python")

my_manager.add(my_project_manager) # guarda objetos
my_manager.add(my_project_manager2) # guarda objetos

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.add(my_programmer2)

my_programmer.code()
my_project_manager.cordinate_project()
my_manager.cordinate_project()

my_manager.print_employess()
my_project_manager.print_employess()
my_programmer.print_employess()
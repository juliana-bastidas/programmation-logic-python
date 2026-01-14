"""CLASES"""

class Programmer:
    surname:str = None
    def __init__(self, name:str, age:int, languages : list): #las funciones son los metodos
        #Atributos
        self.name = name
        self.age = age
        self.languages = languages
    def print (self):
        print(f" Nombre: {self.name} | Apellido: {self.surname} | Edad: {self.age} | Lenguajes: {self.languages}")

my_programmer = Programmer("Brais", 36, ["Python", "Kotlin", "Swift"]) # Obejto o instancia 
my_programmer.print()
my_programmer.surname = "Moure"
my_programmer.print()
my_programmer.age = 37
my_programmer.print()

"""EXTRA
DIFICULTAD EXTRA (opcional):
 Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
  en el ejercicio número 7 de la ruta de estudio)
 Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
  retornar el número de elementos e imprimir todo su contenido.
"""

#LIFO
class Stack:
    def __init__(self):
        self.stack = []
        
    def push (self, item):
        self.stack.append(item)
    
    def pop (self):
        if self.count == 0:
            return None
        return self.stack.pop ()
    def count (self):
        return len(self.stack)
    def print (self):
        for item in reversed(self.stack):
            print(item)
    
my_stack= Stack()
my_stack.push("a")
my_stack.push("b")
my_stack.push("c")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
my_stack.print()

#FIFO

class Queue:
    def __init__(self):
        self.queue = []

    def equeue (self, item):
        self.queue.append (item)
    def qeequeue (self):
        if self.count()==0:
            return None
        return self.queue.pop(0)
    def count (self):
        return len(self.queue)
    def print (self):
        for item in self.queue:
            print(item)
my_queue= Queue()
my_queue.equeue("a")
my_queue.equeue("b")
my_queue.equeue("c")
print(my_queue.count())
my_queue.print()
my_queue.qeequeue()
print(my_queue.count())
my_queue.print()
"""JSON Y XML"""

import xml.etree.ElementTree as xml
import os

import json

data ={
    "name" : "Juli Bastidas",
    "age" : 31,
    "birth_date" : "05-12-1993",
     "programming_languages" : ["Python", "Kotlin", "Swift"]
}

#XML

xml_file = "mouredev.xml"

#la funcion guarda datos 
def create_xml ():
    root = xml.Element("data")

    for key, value in data.items ():
        child = xml.SubElement(root,key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:    
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)

create_xml()

#leer el archivo xml
with open(xml_file, "r") as xml_data:
    print(xml_data.read())

#borrar el archivo xml
os.remove(xml_file)

#JSON

json_file = "mouredev.json"

#escritura
def create_json ():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

create_json()
#lectura
#with open(json_file, "r") as json_data:
#    json.dump(data, json_data)
#borrar
#os.remove(json_file)

"""EXTRA
Utilizando la lógica de creación de los archivos anteriores, crea un
programa capaz de leer y transformar en una misma clase custom de tu 
lenguaje los datos almacenados en el XML y el JSON.
Borra los archivos.
"""

create_json()
create_xml()

class Data:
    def __init__ (self, name, age, birth_date, programming_languages) -> None:
        self.name = name 
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

with open(xml_file, "r") as xml_data:
    root = xml.fromstring(xml_data.read())     
    name = root.find("name").text  
    age = root.find("age").text  
    birth_date = root.find("birth_date").text  
    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    xml_class = Data(name, age, birth_date, programming_languages)
    print(xml_class.__dict__)
    

with open(json_file, "r") as json_data:
    #json_dict = json_data.read() trae cadena de texto mas no el diccionario 
    json_dict = json.load (json_data)
    json_class = Data(
        name = json_dict["name"],
        age = json_dict["age"],
        birth_date = json_dict["birth_date"],
        programming_languages= json_dict["programming_languages"]
    )
    print(json_class.__dict__)
    
os.remove(xml_file)
os.remove(json_file)
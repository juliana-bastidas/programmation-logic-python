"""CADENA DE CARACTERES"""

#Operaciones

s1="hola"
s2="python"
#Concatenacion
print(s1 + ","+ s2 +"!")
#repeticion
print(s1*3)
#Indexacion
print( s1[0] + s1[1]+ s2[0])
#Longitud
print(len(s2))
#Slicing (porcion)
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])
print(s2[1:4])
#Busqueda
print("a" in s1)
print("i" in s1)
#Remplazo
print(s1.replace("o","a"))
#Division
print(s2.split("t"))

#Máyusculas,mínisculas y primera letra en masycula
print(s1.upper())
print(s2.lower())
print("brais moure".title())
print("brais moure".capitalize())

#Eliminacion de espacios al principio y al final 
print(" brais moure ".strip())

#Busqueda al prinicpio y al final 
print(s1.startswith("Ho"))
print(s1.startswith("py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3 ="Brais Moure @mouredev"
#busqueda de posicion 
print(s3.find("moure"))
print(s3.find("Moure"))
print(s3.find("M"))
print(s3.lower().find("m")) #se queda con lo primero que encuentra
#busqueda de ocurrencia 
print(s3.lower().count("m"))
#formateo
print("Saludo: {}, lenguaje: {}!".format(s1,s2))
#Interpolacion 
print(f"Saludo: {s1}, lenguaje: {s2}!")

#transformacion en lista de caracteres
print(list(s3))
#trasnformacion de lista de cadena
l1= [s1, ", ", s2, "!"]
print("".join(l1))
#transformacion numericas
s4 = "12345"
s4= int(s4)
print(s4)

s5="12345.789"
s5= float(s5)
print(s5)

#Comprabaciones varias
s4="123456"
print(type(s4))

print(s1.isalnum())
print(s4.isalpha())
print(s4.isnumeric())


"""EXTRA
Crea un programa que analice dos palabras diferentes y realice comprobaciones 
para descubrir si son :
-palindromos : se lee igual al derecho o al reves, ejemplo radar
-anagramas: palabra que resulta de la transposicion de todas las letras de otra palabra ejemplo: amor, roma
-isogramas:es una palabra que cada letra aparece el mismo numero de veces
"""
def check (word1:str, word2:str):
    #Palindromo
    print(f"¿ {word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿ {word2} es un palíndromo?: {word2 == word2[::-1]}")
    #Anagrama
    print(f"{word1} es anagrama de {word2}?: {sorted(word1)==sorted(word2)}")
    #Isograma

    # word_dict = dict()
    # for word in word2:
    #     word_dict[word] = word_dict.get(word,0) +1
    # isogram = True
    # values = list(word_dict.values())
    # isogram_len = values[0]
    # for word_count in values:
    #     if word_count != isogram_len:
    #         isogram = False
    #         break
    # print(f"{word2} es isograma?: {len(word2)== len(set(word2))}")

    #Lo podemos hacer con una funcion 

    def isogram (word:str) ->bool:
        word_dict = dict()
        for char in word:
            word_dict[char] = word_dict.get(char,0) +1
        # debe haber al menos dos letras distintas
        if len(word_dict) < 2:
            return False
        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isogram
    print(f"{word1} es isograma?: {isogram(word1)}")
    print(f"{word2} es isograma?: {isogram(word2)}")

check("radar", "aaaa")
#check("amor", "roma")
#Dia 12 
print("\nDIVIDIR NUESTRO CODIGO")
print("Dia 12")

#2.  Definir una función llamada que tenga un solo parámetro. 
# El argumento que se le pasará será un diccionario con alguna 
# información sobre un programa de televisión. La función debe 
# imprimir la información almacenada en el diccionario, de una 
# manera agradable
def print_show_info(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} seasosns")

tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}
print_show_info(tv_show)

#3. A continuación encontrará una lista que contiene detalles 
# sobre múltiples series de televisión. Utilice su función, y 
# un bucle, para iterar sobre la lista, y llame a su función 
# una vez para cada iteración, pasando en cada diccionario. 
# Debe terminar con cada serie impresa en el formato apropiado
series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
]
for serie in series:
    print_show_info(serie)

#4. Crear una función para probar si una palabra es un palíndromo. 
# Un palíndromo es una cadena de caracteres que son idénticos, ya 
# sea que se lean hacia adelante o hacia atrás. Por ejemplo, 
# "fue un coche o un gato que vi" es un palíndromo.
def is_palindrome(word):
    word = word.strip().lower()
    reversed_word = reversed(word)
    if list(word) == list(reversed_word):
        print(True)
    else:
        print(False)

is_palindrome("hannah")

#Dia 13
print("Dia 13")

#1.  Definir una función que tome dos números. El primero es la 
# base, y el segundo es el poder de elevar la base. La función 
# debe devolver el resultado de esta operación. Recuerde que 
# podemos realizar la exponenciación utilizando el operador.
def exponentiate(a1, a2):
    return a1 ** a2
print(f"El resultado es: {exponentiate(5, 2)}")

#2. Defina una función que tome una cadena y devuelva una nueva 
# cadena que se haya convertido a minúsculas y que haya eliminado 
# cualquier exceso de espacio en blanco.
def process_string(cadena):
    return cadena.lower().strip()
cadena = " CaDEna ProCeSaDa "
print(process_string(cadena))

#3.Escriba una función que tome una tupla que contenga información 
# sobre un actor y devuelva estos datos como un diccionario. Los 
# datos deben estar en el siguiente formato:
def convertidor(tupla):
    return {
        "Nombre": tupla[0],
        "Nacionalidad": tupla[1],
        "Edad": tupla[2]
    }
tupla = ("Tom Hardy", "English", 42)
print(convertidor(tupla))

#4. Escriba una función que tome un solo número y devuelva o 
# dependiendo de si el número es primo o no. Si necesita un repaso 
# sobre cómo calcular si un número es primo, le mostramos un método 
# en el día 8 de la serie.
def Definir(numero):
    if(numero % 2 == 0):
        return True
    return False
numero = int(input("Ingrese un numero: "))
print(Definir(numero))

#Dia 14
print("\nDia 14")

#1.Vuelva a escribir el siguiente fragmento de código mediante un 
# administrador de contexto:
f = open("CSV/hello_world.txt", "w")
f.write("Hello, World!")
f.close()
with open("CSV/hello_world.txt", 'a') as f:
    f.write("\nHow are you?")

#2. ome la lista de diccionarios que creamos a partir del conjunto 
# de datos de iris flower y escríbala en un nuevo archivo en formato 
# CSV.
irises = [
    {'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '4.9', 'sepal_width': '3',   'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '4.7', 'sepal_width': '3.2', 'petal_length': '1.3', 'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '4.6', 'sepal_width': '3.1', 'petal_length': '1.5', 'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '5',   'sepal_width': '3.6', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '7',   'sepal_width': '3.2', 'petal_length': '4.7', 'petal_width': '1.4', 'species': 'Iris-versicolor'},
    {'sepal_length': '6.4', 'sepal_width': '3.2', 'petal_length': '4.5', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
    {'sepal_length': '6.9', 'sepal_width': '3.1', 'petal_length': '4.9', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
    {'sepal_length': '5.5', 'sepal_width': '2.3', 'petal_length': '4',   'petal_width': '1.3', 'species': 'Iris-versicolor'},
    {'sepal_length': '6.5', 'sepal_width': '2.8', 'petal_length': '4.6', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
    {'sepal_length': '6.3', 'sepal_width': '3.3', 'petal_length': '6',   'petal_width': '2.5', 'species': 'Iris-virginica'},
    {'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '5.1', 'petal_width': '1.9', 'species': 'Iris-virginica'},
    {'sepal_length': '7.1', 'sepal_width': '3',   'petal_length': '5.9', 'petal_width': '2.1', 'species': 'Iris-virginica'},
    {'sepal_length': '6.3', 'sepal_width': '2.9', 'petal_length': '5.6', 'petal_width': '1.8', 'species': 'Iris-virginica'},
    {'sepal_length': '6.5', 'sepal_width': '3',   'petal_length': '5.8', 'petal_width': '2.2', 'species': 'Iris-virginica'}
]
with open("CSV/iris2.txt", "w") as g:
    for iris in irises:
        g.write(",".join(iris.values()) + "\n")
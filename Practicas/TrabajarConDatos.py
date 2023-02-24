import random
#Dia 7
print("\nTRABAJAR CON DATOS")
print("Dia 7")

#1.Pida al usuario que introduzca su nombre y apellidos 
# en respuesta a un único mensaje. Utilícelos para extraer 
# los nombres y, a continuación, asigne cada nombre a una 
# variable diferente. Para este ejercicio, puede suponer que 
# el usuario tiene un solo nombre y un solo apellido.
name = input("Cual es su nombre y apellido: ").strip().title()
name = name.split()
nombre = name[0]
apellido = name[1]
print(f"Su nombre es: {nombre} \nSu apellido es: {apellido}")

#2. Imprima la lista, , en el formato utilizando el método. 
# Recuerda que solo puedes unir colecciones de cadenas, por lo 
# que vas a necesitar hacer un poco de procesamiento inicial de la 
# lista de números.[1, 2, 3, 4, 5] 1 | 2 | 3 | 4 | 5
listas = [1, 2, 3, 4, 5]
listaN = []
for lista in listas:
    listaN.append(str(lista))
listaN = " | ".join(listaN)
print(listaN)

#3.A continuación encontrará una breve lista de citas:
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]
 #Cada cita es una cadena, pero cada cadena en realidad contiene 
 # caracteres de comillas al principio y al final. Usando el corte, 
 # extraiga el texto de cada cadena, sin estas comillas adicionales, e 
 # imprima cada cita.
for quote in quotes:
    print(quote[1:-1])

#4. Pídale al usuario que ingrese una palabra y luego imprima la 
# longitud de la palabra. Debe tener en cuenta cualquier exceso de 
# espacio en blanco en la entrada del usuario, por lo que tendrá que 
# procesar la cadena antes de encontrar su longitud.
#Si quieres llevar esto un poco más allá, le pides al usuario un texto 
# largo. A continuación, puede decirles cuántos caracteres hay en el 
# texto en general, y también puede proporcionarles un recuento de 
# palabras.
frase = input("Ingrese una frase: ").strip()
letras = len(frase)
palabras = len(frase.split())
print(f"Cantidad de letras: {letras}\nCantidad de palabras: {palabras}\n")

#Dia 8
print("Dia 8")

#1. Escribe un breve programa de juego de adivinanzas usando un bucle. 
# Se le debe pedir al usuario que adivine un número entre y , y debe 
# decirle si su suposición fue demasiado alta o demasiado baja después 
# de cada suposición. El bucle debe seguir ejecutándose hasta que el 
# usuario adivine el número correctamente.
aleatorio = random.randint(1, 101)
numero = int(input("Ingrese un numero: "))
print(aleatorio)
while numero != aleatorio:
    if(numero > aleatorio):
        print("El numero es mas pequeño.")
        numero = int(input("Ingrese otro numero: "))
    if(numero < aleatorio):
        print("El numero es mas grande.")
        numero = int(input("Ingrese otro numero: "))
else:
    print("Adivinaste ese es el numero!")

#2. Utilice un bucle y la palabra clave para imprimir todos los caracteres 
# de la cadena, excepto el "o"
palabra = "Python"
for i in palabra:
    if(i == "o"):
        continue
    print(i)

#3. Usando uno de los ejemplos anteriores, o una solución completamente 
# propia, cree un programa que imprima cada número primo entre 1 y 100.
primes = []
for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        primes.append(str(dividend))
print(", ".join(primes))

#Dia 9 
print("\nDia 9")

#1.Escriba un bucle for que utilice la desestructuración para que pueda 
# imprimir cada tupla en el siguiente formato:BoJack Horseman is a horse 
# voiced by Will Arnet.
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]
for nombreP, nombreA, especie in main_characters:
    print(f"{nombreP} is a {especie.lower()} voiced by {nombreA}")

#2.Descomprima la siguiente tupla en 4 variables
tupla = ("John Smith", 11743, ("Computer Science", "Mathematics"))
nombre2, identificacion, (estudio, gusto) = tupla
print(f"Nombre: {nombre2}\nIdentificacion: {identificacion}\nEstudio: {estudio}\nGusto: {gusto}")

#3.Investigue lo que sucede cuando intenta comprimir dos iterables de 
# diferentes longitudes. Por ejemplo, intente comprimir una lista que 
# contenga tres elementos y una tupla que contenga cuatro elementos.
longitud1 = ("Paolo", "Oscar", "William", "Carlos")
longitud2 = ["Perro", "Gato", "Leon"]
unidos = zip(longitud1, longitud2)
print(list(unidos))

#Dia 10
print("\nDia 10")

#1.Convierte esta tupla exterior en un diccionario con cuatro teclas.
Albums = {
    "Album": "The Dark Side of the Moon",
    "Banda": "Pink Floyd",
    "Lanzamiento": 1973,
    "Canciones":(
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
}

#2.Itera sobre las claves y valores del diccionario que creas en el 
# ejercicio 1. Para cada clave y valor, debe imprimir el nombre de 
# la clave y, a continuación, el valor junto a ella.
for titulo, texto in Albums.items():
    print(f"[{titulo}: {texto}")

#3. Elimine la lista de canciones y el año de lanzamiento del 
# diccionario que creó. Una vez que haya hecho esto, agregue una 
# nueva clave al diccionario para almacenar la fecha de lanzamiento. 
# La fecha de lanzamiento de The Dark Side of the Moon fue el 1 de marzo 
# de 1973.
del Albums["Lanzamiento"]
del Albums["Canciones"]
Albums["Fecha"] = "1 de marzo de 1973"
for titulo, texto in Albums.items():
    print(f"[{titulo}: {texto}")

#4. Intente recuperar uno de los valores que eliminó del diccionario. 
# Esto debería darle un archivo . Una vez que haya intentado esto, 
# repita el paso usando el método para evitar que se genere la excepción.
print(Albums.get("Lanzamiento", "No se encontro"))

#Dia 11
print("\nDia 11")

#1. Cree un conjunto vacío y asígnelo a una variable.
s = set()


#2. Agregue tres elementos a su conjunto vacío utilizando varias llamadas 
# o una sola llamada
s.update(range(1, 4))

#3. Crear un segundo conjunto que incluya al menos un elemento común con 
# el primer conjunto.
random_values = {"r", 1, 2, ("Python", "C", "Rust")}

#4. Encontrar la unión, la diferencia simétrica y la intersección de los 
# dos conjuntos. Imprima los resultados de cada operación.
print(s.union(random_values))
print(s.symmetric_difference(random_values))
print(s.intersection(random_values))

#5. Cree una secuencia de números usando range, luego pida al usuario que 
# ingrese un número. Informe al usuario si su número estaba o no 
# dentro del rango que especificó.
secuencia = range(23, 57)
valor = int(input("Ingrese un numero: "))
while valor not in secuencia:
    if(valor > int(secuencia[-1])):
        print("Son numeros mas pequeños")
        valor = int(input("Ingrese otro numero: "))
    elif(valor < int(secuencia[0])):
        print("Son numero mas grande")
        valor = int(input("Ingrese otro numero: "))
if(valor in secuencia):
    print(f"El numero {valor} esta en el conjunto!.")

    

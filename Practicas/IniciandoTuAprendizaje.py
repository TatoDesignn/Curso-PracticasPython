
#Dia 1: 
print("INICIANDO TU APRENDIZAJE")
print("Dia 1")

#1. Imprime tu edad en la consola.
print("Mi edad es: 20")

#2.Calcule e imprima el número de días, 
# semanas y meses en 27 años. ¡No te preocupes 
# por los años bisiestos!
print(f"Cantidad de dias: {27 * 365}")
print(f"Cantidad de semanas: {27 * 52}")
print(f"Cantidad de meses: {27 * 12}")

#3.Calcula e imprime el área de un círculo con 
# un radio de 5 unidades. Puedes ser tan preciso 
# como quieras con el valor de pi.
print(f"El area de un circulo con radio de 5 es: {3.14 * 5**2}")
print(f"El area de un circulo con radio de 5 es: {3.14 * pow(5, 2)}\n")

#Dia 2
print("Dia 2")

#1. Pregunte al usuario por su nombre y edad, 
# asigne estos valores a dos variables y luego imprímalos.
name = input("Cual es su nombre: ")
surname = input("Cual es su apellido: ")
print(f"Su nombre es: {name}\nSu apellido es: {surname}\nSu nombre completo es {name} {surname}")

#2. Investigue lo que sucede cuando intenta asignar un valor 
# a una variable que ya ha definido. Intente imprimir la variable 
# antes y después de reutilizar el nombre.
nombre = "Juanito"
print(nombre)
nombre = input("Digite un nombre cualquiera: ")
print(nombre)

#3. A continuación encontrarás un código con una serie de errores. 
# Intente revisar el programa línea por línea y solucione los problemas 
# en el código. Le animo a que intente ejecutar el programa mientras 
# trabaja en él, ya que leer los mensajes de error es una gran práctica
#  para depurar sus propios programas.
hourly_wage = input("Please enter your hourly wage: ") #Cambio de comillas
hours_worked = input("How many hours did you work this week? ")
print("Hourly wage: ") #print mal escrito
print(hourly_wage) #variable mal escrita
print("Hours worked: ") #orden de las funciones 
print(f"{hours_worked}\n")

#Dia 3
print("Dia 3")

#1. Usando la siguiente variable, imprima ."Hello, world!"
greeting = "Hello, world"
print(greeting + "!")

#2.Pida al usuario su nombre y, a continuación, salude al usuario, utilizando 
# su nombre como parte del saludo. El nombre debe estar en mayúsculas y 
# minúsculas y no debe estar rodeado por ningún exceso de espacio en blanco.
name2 = input("Cual es su nombre completo: ")
name2 = name2.strip().title()
print(f"Hola, {name2}!")

#3. Concatenar la cadena y el entero para producir una cadena que diga .
# I am 29
print("I am " + str(29))

#4. Formatee e imprima la siguiente información mediante interpolación de cadenas:
title = "Joker"
director = "Todd Phillips"
release_year = 2019
# El resultado debería verse así: Joker (2019), directed by Todd Phillips
#Opcion 1
texto = "{} {}, direct by {}"
print(texto.format(title, release_year, director))
#Opcion 2
print(f"{title} {release_year}, direct by {director}")





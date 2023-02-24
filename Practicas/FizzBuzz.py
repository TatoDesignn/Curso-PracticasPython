#Dia 4
print("\nUN RETO: FIZZBUZZ")
print("Dia 4")

#1.Cree una lista que contenga una sola tupla. La tupla debe contener 
# un título de película, el nombre del director, el año de estreno de 
# la película y el presupuesto de la película.
movie = [("Spiderman", "Jon Watts", "2022", "$200M" )]

#2. Utilice la función para recopilar información sobre otra película. 
# Necesitas un título, el nombre del director, el año de lanzamiento y 
# el presupuesto.
titulo = input("Nombre de la pelicula: ").strip().title()
director = input("Nombre del director: ").strip().title()
año = int(input("Año de lanzamiento: "))
presupuesto = float(input("Cual fue el presupuesto: "))

#3. Cree una nueva tupla a partir de los valores que recopiló mediante. 
# Asegúrate de que estén en el mismo orden que la tupla que escribiste en 
# la lista.
tupla = (titulo, director, año, presupuesto)

#4. Utilice una cadena f para imprimir el nombre de la película y el año de 
# lanzamiento accediendo a la nueva tupla de película.
print(f"Nombre: {tupla[0]}\nAño: {tupla[2]}")

#5. Agregue la nueva tupla de película a la colección mediante
movie.append(tupla)

#6. Imprime ambas películas en la colección.
print(movie[0])
print(movie[1])

#7. Quitar la primera película de . Usa cualquier método que quieras.
del movie[0]
print(movie)
print("\n")

#Dia 5
print("Dia 5")

#1. Tratar de aproximar el comportamiento del operador utilizando . 
# Recuerde que tenemos la función para encontrar la dirección de 
# memoria para un valor dado, y podemos comparar las direcciones de 
# memoria para verificar la identidad
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(id(lista1) == id(lista2))

#2.  Trate de usar el operador o la función para investigar la 
# diferencia entre esto:
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
# Y esto:
numbers = [1, 2, 3, 4]
numbers.append(5)
print(id(numbers))
print(id(new_numbers))
print(numbers is new_numbers)

#4. Pida al usuario que introduzca un número. Indique al usuario si 
# el número es positivo, negativo o cero.
numero = int(input("Digite un numero: "))
if (numero > 0):
    print(f"El numero {numero} es positivo.")
elif (numero < 0):
    print(f"El numero {numero} es negativo.")
else:   
    print("Tu numero es cero.")

#5. Escriba un programa para determinar si a un empleado se le debe 
# alguna hora extra. Debe preguntar al usuario cuántas horas trabajó el 
# empleado esta semana, así como el salario por hora para este empleado.
nombre = input("Cual es el nombre del empleado: ").strip().title()
salario = float(input("Cual es su salario por hora: "))
horas = int(input("Cuantas horas trabajo: "))
if(horas > 40):
    nuevaHora = horas - 40
    print(f"A {nombre} se le debe un pago adicional del 10% por trabajar {nuevaHora} horas de mas.")
    nuevoSalario = salario * 110 /100
    total = nuevoSalario * horas
    print(f"Su salario queda en: {nuevoSalario} y en total se le debe pagar: {total} \n")
elif(horas <= 40):
    salario = salario * horas
    print(f"A {nombre} se le debe pagar: {salario} \n")

#Dia 6 
print("Dia 6")

#1.A continuación hemos proporcionado una lista de tuplas, donde cada 
# tupla contiene detalles sobre un empleado de una tienda: su nombre, 
# el número de horas trabajadas la semana pasada y su tarifa por hora. 
# Imprima cuánto se le debe pagar a cada empleado al final de la semana 
# en un formato agradable y legible.
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for pago in employees:
    pagofinal = pago[1] * pago[2]
    print(f"A {pago[0]} se le debe pagar: {pagofinal}")

#2.Para los empleados anteriores, imprima aquellos que ganan un salario 
# por hora por encima del promedio.
total2 = 0
for cantidad in employees:
    total2 += cantidad[2]
promedio = total2 / len(employees)
print(f"El promedio es: {promedio}")
for prom in employees:
    if(prom[2] > promedio):
        print(prom[0])
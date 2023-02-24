#1.A continuación encontrará una lista que contiene 
# los datos relevantes sobre una selección de películas. 
# Cada elemento de la lista es una tupla que contiene un 
# nombre de película y un presupuesto de película en ese orden:

#2. Para este proyecto, el programa debe hacer lo siguiente:

#3. Calcule el presupuesto promedio de todas las películas del 
# conjunto de datos.

#4. Imprime cada película que tenga un presupuesto superior al 
# promedio que calculaste. También debe imprimir cuánto más alto 
# que el promedio del presupuesto de la película fue.

#5. Imprime cuántas películas gastaron más que el promedio que 
# calculaste.

#6. Si desea un pequeño desafío adicional, permita que los usuarios 
# agreguen más películas al conjunto de datos antes de ejecutar los 
# cálculos.

#6. Puede hacer esto preguntando al usuario cuántas películas desea 
# agregar, lo que le permitirá usar un bucle y repetir algún código 
# un número determinado de veces. Dentro del bucle, puede escribir 
# algún código que tome alguna entrada del usuario y agregue una 
# tupla de película que contenga los datos recopilados a la lista de 
# películas.
movies = [
    ("Eternal Sunshine of the Spotless Mind", 200),
    ("Memento", 900),
    ("Requiem for a Dream", 450),
    ("Pirates of the Caribbean: On Stranger Tides", 379),
    ("Avengers: Age of Ultron", 365),
    ("Avengers: Endgame", 356),
    ("Incredibles 2", 200)

]

cantidad = int(input("\nCuantas peliculas quiere agregar: "))
suma = 0

for i in range(cantidad):
    nuevaPelicula = input("Ingrese el nombre y el presupuesto de la pelicula separado por espacio: ").title()
    nuevaPelicula = nuevaPelicula.split()
    str(nuevaPelicula[0])
    movies.append(tuple(nuevaPelicula))

for movie in movies:
    suma += int(movie[1])
    promedio = suma / len(movies)
print(f"\nEl promedio es: {promedio}\n")

for calcula in movies:
    if(float(calcula[1]) > promedio):
        demas = int(calcula[1]) - promedio
        print(f"{calcula[0]} su presupuesto tiene {demas} mas que el promedio")



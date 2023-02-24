#1. Los usuarios deben poder agregar un libro a su lista de 
# lectura proporcionando un título de libro, el nombre de un 
# autor y un año de publicación.

#2. El programa debe almacenar información sobre todos estos 
# libros en una lista de Python.

#3. Los usuarios deben poder mostrar todos los libros en su 
# lista de lectura, y estos libros deben imprimirse en un formato 
# fácil de usar.

#4. Los usuarios deben poder seleccionar estas opciones en un menú 
# de texto y deben poder realizar múltiples operaciones sin reiniciar 
# el programa. Puedes ver un ejemplo de un menú de trabajo en el post 
# on while loops (día 8).

listaLibro = []

def Menu():
    opcion = ""
    opcion = input("\nEscriba 'A' para añadir.\nEscriba 'L' para ver los libros.\nEscriba 'S' para salir.\nQue desea hacer: ")
    opcion = opcion.upper().strip()

    while opcion != "S":
        if(opcion == "A"):
            cantidad = int(input("\nCuantos libros desea agregar: "))
            Agregar(cantidad)
            break
        elif(opcion == "L"):
            Visualizacion()
            break
        else:
            opcion = input("\nLa opcion no es valida, intente de nuevo:").upper().strip()

def Agregar(cantidad):
    conteo = 0 
    nuevoLibro = ""

    while conteo < cantidad:
        nuevoLibro = input("Agregue el titulo, el autor y el año separado por comas: ").strip()
        nuevoLibro = nuevoLibro.split(",")

        directorio = {
            "Titulo": nuevoLibro[0],
            "Autor": nuevoLibro[1],
            "Año": nuevoLibro[2]
        }

        listaLibro.append(directorio)
        conteo += 1
        print("\nSe ha añadido correctamente!\n")

    print("te devolveremos al menu...\n")
    Menu()

def Visualizacion():
    print("\nLISTA LIBROS")
    for contador, i in enumerate(listaLibro, start=1):
        title, author, year = i.values()
        title = title.strip().title()
        author = author.strip().title()
        year = year.strip()
        
        print(f"{contador}. Titulo: {title}, Autor: {author}, Año: {year}")

    print("te devolveremos al menu...\n")
    Menu()

print("\nREGISTRO DE LIBROS")
Menu()
print("\nHas salido con exito!.\n")
print("\nCREADO POR TATODESIGN.\n")
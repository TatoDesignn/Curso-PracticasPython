#1. Los usuarios deben poder agregar un libro a su lista de lectura 
# proporcionando un título del libro, el nombre de un autor, un año 
# de publicación y si el libro ha sido leído o no.

#2. El programa debe almacenar información sobre todos estos libros 
# en un archivo llamado , y estos datos deben almacenarse en formato 
# CSV.books.csv

#3. Los usuarios deben poder recuperar los libros en su lista de 
# lectura, y estos libros deben imprimirse en un formato fácil de 
# usar.

#4. Los usuarios deben poder buscar un libro específico proporcionando 
# un título de libro.

#5. Los usuarios deben poder marcar un libro como leído ingresando el 
# título de un libro. Si hay varios libros con el mismo título, puede 
# marcar el primer libro coincidente como leído.

#6. Los usuarios deben poder eliminar libros de su lista de lectura 
# proporcionando el título del libro que desean eliminar. Una vez más, 
# puede eliminar el primer libro coincidente.

#7. Los usuarios deben poder seleccionar estas opciones en un menú de 
# texto y deben poder realizar múltiples operaciones sin reiniciar el 
# programa. Puede ver un ejemplo de un menú de trabajo en la publicación 
# en bucles mientras (día 8).# Día 14 Proyecto: Lista de lectura 

def Menu():
    opcion = ""
    opcion = input("\nEscriba 'A' para añadir.\nEscriba 'L' para ver los libros.\nEscriba 'B' para buscar.\nEscriba 'E' para eliminar.\nEscriba 'M' para marcar o desmarcar un libro como leido.\nEscriba 'S' para salir.\nQue desea hacer: ")
    opcion = opcion.upper().strip()

    while opcion != "S":
        if(opcion == "A"):
            Agregar()
            break
        elif(opcion == "L"):
            Visualizacion(inicio())
            break
        elif(opcion == "B"):
            buscar(inicio())
            break
        elif(opcion == "E"):
            Eliminar(inicio())
            break
        elif(opcion == "M"):
            Marcar(inicio())
            break
        else:
            opcion = input("\nLa opcion no es valida, intente de nuevo:").upper().strip()

def inicio():
    listaLibro = []
    book = open("CSV/book.csv", "r")
    guardado = book.readlines()
    book.close
    guardado[0].strip().split(",")

    for i in guardado[1:]:
        valores1 = i.strip().split(",")
        directorioN = dict(zip(guardado, valores1))
        listaLibro.append(directorioN)

    return listaLibro

def Agregar():
    conteo = 0 
    nuevoLibro = ""

    cantidad = input("\nCuantos libros desea agregar: ")

    while cantidad != cantidad.isdigit():
        print("\nEl dato introducido no es correcto(Debe añadir un numero).")
        cantidad = int(input("\nCuantos libros desea agregar: "))
        break

    cantidad = int(cantidad)

    while conteo < cantidad:
        nuevoLibro = input("Agregue el titulo, el autor, el año y si ha sido leido, separelo por comas: ").strip()
        book = open("CSV/book.csv", "a")
        book.write("\n" + nuevoLibro)
        book.close()
        conteo += 1
        print("\nSe ha añadido correctamente!\n")
    
    print("te devolveremos al menu...\n")
    Menu()

def buscar(listaLibro):
    cantidad = 1
    busqueda = input("\nCual libro desea buscar: ")
    busqueda = busqueda.title().strip()

    for i in listaLibro:
        titulo, autor, año, visto = i.values()
        titulo = titulo.strip().title()

        if(busqueda == titulo):
            print(F"\nTitulo: {titulo}, Autor: {autor}, Año: {año}, Leido: {visto}")
            print("\nte devolveremos al menu...\n")
            Menu()
            break

    print("\nEl libro no esta en su lista.")

    while (respuesta := input("Desea agregarlo(Si/No): ").upper().strip()) != "NO":
        if(respuesta == "SI"):
            Agregar(cantidad)
        else:
            print("\nRespuesta incorrecta escriba'si o no'.")
    print("\nte devolveremos al menu...\n")
    Menu()

def Eliminar(listalibro):
    contador = 0
    busqueda = input("\nQue libro desea eliminar: ")
    busqueda = busqueda.strip().title()

    for buscar in listalibro:
        titulo1, autor1, año1, visto1 = buscar.values()
        titulo1 = titulo1.strip().title()

        if(busqueda == titulo1):
            for actualiza in listalibro:
                titulo, autor, año, visto = actualiza.values()
                titulo = titulo.strip().title()

                if(titulo == busqueda):
                    print("\nLibro eliminado con exito!.")
                else:
                    if(contador < 1):
                        with open("CSV/book.csv", "w") as g:
                            g.write("Titulo,Autor,Ano,visto")
                        contador += 1
                        
                    with open("CSV/book.csv", "a") as g:
                        g.write("\n" + ",".join(actualiza.values())) 
            
            print("\nte devolveremos al menu...\n")
            Menu()
              
    else:
        print(f"\nEl libro {busqueda} no se encuentra en lista!.")
        print("\nte devolveremos al menu...\n")
        Menu()
    
def Marcar(listalibro):
    contador2 = 0
    opcion = input("Que libro desea modificar: ").strip().title()

    for buscar in listalibro:
        titulo, autor, año, visto = buscar.values()
        titulo = titulo.strip().title()

        if(opcion == titulo):
            valor = input(f"\n{opcion} ya lo leiste(SI/NO): ").strip().title()

            for actualizar in listalibro:
                titulo2, autor2, año2, visto2 = actualizar.values()
                titulo2 = titulo2.strip().title()

                if(opcion == titulo2):
                    visto2 = valor
                    if(contador2 < 1):
                        with open("CSV/book.csv", "w") as g:
                            g.write("Titulo,Autor,Ano,visto")
                        contador2 += 1
                    else:
                        with open("CSV/book.csv", "a") as g:
                            g.write(f"\n{titulo2}, {autor2}, {año2}, {visto2}")
                            print("\nEl libro se marco correctamente!.")

                else:
                    if(contador2 < 1):
                        with open("CSV/book.csv", "w") as g:
                            g.write("Titulo,Autor,Ano,visto")

                        contador2 += 1
                
                    with open("CSV/book.csv", "a") as g:
                        g.write("\n" + ",".join(actualizar.values()))

            print("\nte devolveremos al menu...\n")
            Menu()

    else:
        print(f"\nEl libro {opcion} no se encuentra en lista!.")
        print("\nte devolveremos al menu...\n")
        Menu()


def Visualizacion(listaLibro):
    print("\nLISTA LIBROS")
    for contador, i in enumerate(listaLibro, start=1):
        title, author, year, visto= i.values()
        title = title.strip().title()
        author = author.strip().title()
        year = year.strip()
        visto = visto.strip().title()
        
        print(f"{contador}. Titulo: {title}, Autor: {author}, Año: {year}, Visto: {visto}.")

    print("\nte devolveremos al menu...\n")
    Menu()

def Autores():
    libro = input("Que libro deseas mirar: ").strip().title()

print("\nREGISTRO DE LIBROS")
Menu()
print("\nHas salido con exito!.")
print("\nCREADO POR TATODESIGN.\n\n")
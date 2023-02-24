
print("\nMI CALCULADORA")

def Inicio():
    valor1 = 0
    valor2 = 0

    valor1 = int(input("Ingrese el primer numero: "))
    valor2 = int(input("Ingrese el segundo numero: "))
    Menu(valor1, valor2)

def Menu(valor1, valor2):
    while (menu := input("\nIngrese 'S' para sumar.\nIngrese 'R' para restar.\nIngrese 'M' para multiplicar.\nIngrese 'D' para dividir.\nIngrese 'E' para salir.\nQue desea hacer: ")) != "E":
        if(menu == "S"):
            Sumar(valor1, valor2)
            continuar()
            break
        elif(menu == "R"):
            Restar(valor1, valor2)
            continuar()
            break
        elif(menu == "M"):
            Multiplicar(valor1, valor2)
            continuar()
            break
        elif(menu == "D"):
            Dividir(valor1, valor2)
            continuar()
            break
        else:
            print("La palabra no es correcta")

def Sumar(valor1, valor2):
    total = valor1 + valor2
    print(f"\n{valor1} + {valor2} = {total}")

def Restar(valor1, valor2,):
    total = valor1 - valor2
    print(f"\n{valor1} - {valor2} = {total}")

def Multiplicar(valor1, valor2,):
    total = valor1 * valor2
    print(f"{valor1} * {valor2} = {total}")

def Dividir(valor1, valor2,):
    total = valor1 / valor2
    print(f"\n{valor1} / {valor2} = {total}")

def continuar():
    while (menu2 := input("Desea realizar otra operacion: SI/NO ")) != "NO":
        if(menu2 == "SI"):
            Inicio()
            break
        else:
            print("No es Valido")

Inicio()
print("Has salido de la calculadora")

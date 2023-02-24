listaProcesada = []
suma = 0 

print("APLICACION PARA VALIDAR EL NUMERO DE UNA TARJETA.")

tarjeta = list(input("Agregue un numero de tarjeta: ").strip())
ultimo = tarjeta.pop()
tarjeta.reverse()

for cuenta, numero in enumerate(tarjeta):
    if(cuenta % 2 == 0):
        doble = int(numero) * 2
        if(doble > 9):
            procesado = doble - 9
            listaProcesada.append(procesado)
        else: 
            listaProcesada.append(doble)
    else:
        listaProcesada.append(numero)

for lista in listaProcesada:
    suma += int(lista)
suma += int(ultimo)
if (suma % 10 == 0):
    print("Su numero de tarjeta es valido!.")
else:
    print("Su numero de tarjeta no es valido.")
    



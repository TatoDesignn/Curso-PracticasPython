lista = []
lista2 = ""
lista3 = []
lista4 = ""

cero = "0000"
uno = "0001"
dos = "0010"
tres = "0011"
cuatro = "0100"
cinco = "0101"
seis = "0110"
siete = "0111"
ocho = "1000"
nueve = "1001"
letraA = "1010"
letraB = "1011"
letraC = "1100"
letraD = "1101"
letraE = "1110"
letraF = "1111"


print(f"\n \n- CONVERTIDOR DE BINARIO A HEX DE 8 BITS - ")
print(f"- DESARROLLADO POR TATODESIGN - \n")

binario = input("Escribe tu codigo binario: ")

palabra = ""
contador = 0

for k in binario:

    palabra += k
    contador += 1

    if contador == 4:
        contador = 0 
        lista.append(palabra)
        palabra = ""
    


print( f"\n {lista}" )

for i in lista:
    if(i == cero):
        lista2 = lista2 + "0"
    elif(i == uno):
        lista2 = lista2 + "1"
    elif(i == dos):
        lista2 = lista2 + "2"
    elif(i == tres):
        lista2 = lista2 + "3"
    elif(i == cuatro):
        lista2 = lista2 + "4"
    elif(i == cinco):
        lista2 = lista2 + "5"
    elif(i == seis):
        lista2 = lista2 + "6"
    elif(i == siete):
        lista2 = lista2 + "7"
    elif(i == ocho):
        lista2 = lista2 + "8"
    elif(i == nueve):
        lista2 = lista2 + "9"
    elif(i == letraA):
        lista2 = lista2 + "A"
    elif(i == letraB):
        lista2 = lista2 + "B"
    elif(i == letraC):
        lista2 = lista2 + "C"
    elif(i == letraD):
        lista2 = lista2 + "D"
    elif(i == letraE):
        lista2 = lista2 + "E"
    elif(i == letraF):
        lista2 = lista2 + "F"

print(f"\n {lista2}")

print(f"\n \n- CONVERTIDOR DE HEX A ASCII - ")
print(f"- DESARROLLADO POR TATODESIGN - \n")

numeros = ""
contador2 = 0 

for N in lista2:

    numeros += N
    contador2 += 1

    if contador2 == 2:
        contador2 = 0 
        lista3.append(numeros)
        numeros = ""

print(f"\n {lista3}")

for l in lista3:
    if(l == "41" or l == "61"):
        lista4 += "a"
    elif(l == "42" or l == "62"):
        lista4 += "b"
    elif(l == "43" or l == "63"):
        lista4 += "c"
    elif(l == "44" or l == "64"):
        lista4 += "d"
    elif(l == "45" or l == "65"):
        lista4 += "e"
    elif(l == "46" or l == "66"):
        lista4 += "f"
    elif(l == "47" or l == "67"):
        lista4 += "g"
    elif(l == "48" or l == "68"):
        lista4 += "h"
    elif(l == "49" or l == "69"):
        lista4 += "i"
    elif(l == "4A" or l == "6A"):
        lista4 += "j"
    elif(l == "4B" or l == "6B"):
        lista4 += "k"
    elif(l == "4C" or l == "6C"):
        lista4 += "l"
    elif(l == "4D" or l == "6D"):
        lista4 += "m"
    elif(l == "4E" or l == "6E"):
        lista4 += "n"
    elif(l == "4F" or l == "6F"):
        lista4 += "o"
    elif(l == "50" or l == "70"):
        lista4 += "p"
    elif(l == "51" or l == "71"):
        lista4 += "q"
    elif(l == "52" or l == "72"):
        lista4 += "r"
    elif(l == "53" or l == "73"):
        lista4 += "s"
    elif(l == "54" or l == "74"):
        lista4 += "t"
    elif(l == "55" or l == "75"):
        lista4 += "u"
    elif(l == "56" or l == "76"):
        lista4 += "v"
    elif(l == "57" or l == "77"):
        lista4 += "w"
    elif(l == "58" or l == "78"):
        lista4 += "x"
    elif(l == "59" or l == "79"):
        lista4 += "y"
    elif(l == "5A" or l == "7A"):
        lista4 += "z"
    elif(l == "20"):
        lista4 += " "

print(f"\n MENSAJE CONVERTIDO: {lista4} \n \n \n")



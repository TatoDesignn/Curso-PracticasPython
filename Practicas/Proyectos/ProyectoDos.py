#1. Un jugador comienza diciendo el número .1

#2. Luego, cada jugador se turna para decir el siguiente número, 
# contando uno a la vez.

#3. Si el número es divisible por , en lugar de decir el número, 
# el jugador debe decir, "Fizz".3

#4. Si el número es divisible por , en lugar de decir el número, 
# el jugador debe decir: "Buzz".5

#5. Si el número es divisible por y, en lugar de decir el número, 
# el jugador debe decir: "Fizz Buzz".3,5

#6. Si cometes un error, generalmente eres eliminado del juego, 
# y el juego continúa hasta que solo queda un jugador.

print("\n PROYECTO #2")

numeros = list(range(1, 101))
for test in numeros:
    resultado = test % 3
    resultado2 = test % 5 
    resultado3 = resultado + resultado2

    if(resultado != 0 and resultado2 != 0):
        print(test)
    if(resultado == 0 and resultado2 != 0):
        print("Fizz")
    if(resultado2 == 0 and resultado != 0):
        print("Buzz")
    if(resultado3 == 0):
        print("FizzBuzz")
    
#1. El usuario debe recibir tres indicaciones en las que se le pedirá que proporcione 
# información diferente sobre un empleado. Un mensaje debe preguntar por el nombre del 
# empleado, otro debe preguntar por su salario por hora, y el último debe preguntar 
# cuántas horas trabajó el empleado esta semana.

#2. El nombre del empleado debe procesarse para asegurarse de que esté en un formato 
# particular. Todos los nombres de los empleados deben ser despojados de cualquier 
# exceso de espacio en blanco, y deben estar en el caso del título. Esto significa que 
# cada palabra está en mayúsculas y todas las demás letras están en minúsculas. Por 
# ejemplo, si el empleador accidentalmente tiene mayúsculas bloqueadas y escriben, el 
# nombre aún se almacenará correctamente como ."rEGINA gEORGE""Regina George"

#3. Las ganancias totales del empleado para la semana deben calcularse multiplicando 
# las horas trabajadas por su salario por hora.

#4. Recuerda que cualquier entrada de usuario que recibamos va a ser una cadena. Si 
# bien podemos multiplicar cadenas, no hará lo que quieras en este caso. También vale 
# la pena tener en cuenta que el salario del empleado, o el número de horas que trabajó, 
# puede no ser un número entero.

#5. Después de procesar el nombre del empleado y calcular sus ganancias para la semana, 
# el programa debe generar esta información como una sola cadena. Por ejemplo, una 
# salida como esta sería apropiada:

print("PROYECTO #1")

nombre = input("Cual es el nombre del empleado: ").strip().title()
salario = float(input("Cual es su salario: "))
horas = int(input("Cuantas horas trabajo: "))

cantidad = salario * horas

print(f"Las ganacias del empleado {nombre} fueron {cantidad} esta semana")
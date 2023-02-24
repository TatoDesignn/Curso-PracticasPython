employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

total2 = 0

for i in employees:
    total = i[1] * i[2]
    total2 = total2 + i[2]
    print(f"{i[0]} se le debe pagar: {total}")

promedio = total2 / len(employees)

for k in employees:
    if(k[2] > promedio):
        print(f"{k[0]} gana mas del promedio")





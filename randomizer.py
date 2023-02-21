import random

inicio = float(input("introduzca el numero mas bajo del rango: "))
final = float(input("introduzca el numero mas alto del rango: "))
count = int(input("cuantos numeros aleatorios desea: "))

def randomizer(start, end):
    if start < end:
        number = random.uniform(start, end)
        return number
    else:
        print('Error: El número inicial no puede ser mayor o igual que el final')
        inicio = float(input("introduzca el numero mas bajo del rango: "))
        final = float(input("introduzca el numero mas alto del rango: "))
        number = random.uniform(start, end)
        return number

cuenta = 0
while cuenta < count:
    numero = randomizer(inicio, final)
    print("{:.2f}".format(numero))
    cuenta += 1
    
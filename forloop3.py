n = int(input("Ingrese la cantidad de valores "))
suma = 0

for i in range(n):
    x = float(input ("Ingrese el dato: "))
    suma = x+suma
    promedio = suma / n
print   promedio
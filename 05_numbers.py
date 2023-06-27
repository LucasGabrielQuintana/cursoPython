lives = '3'
print(type(lives))  #lives es tipo string
lives = 3
print(type(lives)) #live es tipo int
age = 10
budget = 100

temperatura = 12.12
print(type(temperatura)) # temperatura es tipo float

lives = 2
print(lives)
lives = 1
print(lives)

lives = 12 + 15
print(lives)

lives = lives -1
print(lives)

lives -= 1
print(lives)

lives -= 5
print(lives)

lives += 5
print(lives)

number = 450000000000000000000000000.41
print(number)

number_b = 0.0000000000000000001
print(number_b)

# Actividad calcular el promedio de gastos de 3 meses

budget_january = float(input("Ingresar presupuesto para Enero\n"))
budget_february = float(input("Ingresar presupuesto para Febrero\n"))
budget_march = float(input("Ingresar presupuesto para marzo\n"))

cant_meses = 3

prom = (budget_january + budget_february + budget_march)/cant_meses

print("El promedio es de presupuesto es", prom)
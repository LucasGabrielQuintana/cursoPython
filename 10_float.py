x = 3.3
y = 1.1 + 2.2

print(x)
print(y)

print(x == y) 

y_str = format(y, ".2g") # Convirtio y en String con menos apreciacion

print(y_str)

print(y_str == str(x))

print("*" * 15) # Linea divisoria

print(x, y)

tolerance = 0.0001 # Tolerancia para comparar 
print(abs(x - y) < tolerance)
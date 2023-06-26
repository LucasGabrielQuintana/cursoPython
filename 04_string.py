name = "Lucas"
last_name = "Quintana"
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Lucas"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

quote2 = "She said \"Bye\""
print(quote2)

# Format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template)

edad = 34
complete = f"Hola, mi nombre es {name} {last_name} y tengo {edad} años"
print(complete)
#More Conditional Test 

#Test of equality or inequality with strings

amor = "Laura"
print("Is amor = Laura? I predict True")
print( amor == "Laura")

comida = "arroz"
print("\nIs comida = mole I predict False")
print( comida == "mole")

#Test using lower function
#Test using upper function

auto = 'audi'
print("\n I predict auto.capaitalize == Audi as True")
print(auto.capitalize() == "Audi")

print("\n I predict auto.upper == AUDI as True")
print(auto.upper() == "AUDI")

print("\n I predict auto.lowe() == audi as True")
print(auto.lower() == "audi")

# Numerical test involving equality and inequality, greater than and less than
# greater than or equal to and less than or equal to.

print("\n 5 >= 5 is True")
print(5>=5)

print("\n10 < 8 is False")
print(10<8)

#Test using and keyword and or keyword
print("\n 5 > 10 and 8 < 15 is False")
print(5>10 and 8<15)

print("\n 10 < 15 and 23 < 32 is True")
print( 10<15 and 23<32)

print("\n 5 > 10 or 12 < 25 is True")
print( 5>10 or 12<25 )

print("\n 12 < 10 or 10 > 15 is False")
print( 12<10 or 10>15)

#Test whether an item is in a list

colores = ['azul','rojo','verde','amarillo','blanco', 'negro']
print("\n ¿Esta el naranja en la lista de colores? Falso")
print( 'naranja'in colores)

print("\n ¿Esta azul en la lista de colores? Verdadero")
print('azul' in colores)

#Test whether an item is not in a list

print("\n ¿No esta el rojo en la lista de colores? Falso")
print( 'rojo' not in colores )

print("\n ¿No esta el color rosa en la lista de colores? Verdadero")
print('rosa' not in colores)
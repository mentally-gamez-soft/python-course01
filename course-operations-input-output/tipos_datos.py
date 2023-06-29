# My comments
# integer
edad = 45
print(edad)
print(type(edad))
print(len(str(edad)))

# float
temperatura = 33.5
print(temperatura)
print(type(temperatura))


# string
nombre = "krys"
apellido = "app"
print(nombre)
print(type(nombre))
my_name = nombre + apellido
print(my_name)
print(nombre * 3)
print(my_name[2:5])
print(my_name[2:])
print(len(my_name))


# boolean
exist_algo = False
print(exist_algo)
print(type(exist_algo))


nota_1, nota_2 = 4, 6
print(f'nota_1: {nota_1} - nota_2: {nota_2}')

sum_notes = nota_1 + nota_2 
print("sum:" + str(sum_notes))



esta_lloviendo = True
hace_frio = False
print(hace_frio and esta_lloviendo)
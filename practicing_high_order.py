# EXERCISES FROM PYTHONDIARIO.COM 
# Utilizar la función incorporada map() para crear una función que retorne una lista con la 
# longitud de cada palabra (separas por espacios) de una frase. 
# La función recibe una cadena de texto y retornara una lista.


# def longitud_palabras(frase):
#     palabra_len = list(map(len, frase.split()))
#     return palabra_len
# print(longitud_palabras("El león está en la selva y ruge sin parar despierta a los animales con su rugido singular"))

# Crear una función que tome una lista de dígitos y devuelva al número al que corresponden. 
# Por ejemplo [1,2,3] corresponde a el numero ciento veintitrés (123). Utilizar la función reduce.
# from functools import reduce

# def digitos_a_numero(digitos):
#     return reduce(lambda x,y:x*10 + y,digitos)

# print(digitos_a_numero([4,3,9,2]))

# Darle vuelta a una cadena con lambda
# revertir = lambda cadena: cadena[::-1]

# print(revertir("El león está en la selva y ruge sin parar"))

# EXCECISES FROM ASABENEH 30-DAYS-OF-PYTHON
# Explain the difference between map, filter and reduce
# map is saved in a variable, recibe a function and a iterable and returns the application of that
# function in each variable
# Use map to create a new list by changing each country to uppercase in the countries list
# countries = [
#   'Afghanistan',
#   'Albania',
#   'Algeria',
#   'Andorra',
#   'Angola',
#   'Antigua and Barbuda',
#   'Argentina',
#   'Armenia',
#   'Australia',
#   'Austria',
#   'Azerbaijan',
#   'Bahamas',
#   'Bahrain',
#   'Bangladesh',
#   'Barbados']
# def convert_uppercase(lista):
#   upper_case = list(map(lambda x:x.upper(), lista))
#   return upper_case
# print(convert_uppercase(countries))

# Another way
# def change_to_upper(lista):
#   return lista.upper()
# names_upper_cased = map(change_to_upper, countries)
# print(list(names_upper_cased)) 

# Use map to create a new list by changing each number to its square in the numbers list
# def squares(numbers):
#   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   squares = list(map(lambda x:x**2, numbers))
#   return squares

# Use filter to filter out countries containing 'land'.



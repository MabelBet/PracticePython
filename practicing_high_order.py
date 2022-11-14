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

# Use filter to filter out countries containing 'ia'.
# has_ia = list(filter(lambda country:country.endswith('ia'), countries))
# print(has_ia)

#  Use filter to filter out countries having exactly six characters
# has_six_characters = list(filter(lambda country:len(country) == 6, countries))
# print(has_six_characters)

#  Use filter to filter out countries containing six letters and more in the country list.
# has_six_or_more_characters = list(filter(lambda country:len(country) >= 6, countries))
# print(has_six_or_more_characters)

# Use filter to filter out countries starting with an 'B'
# starts_with_b = list(filter(lambda country:country.startswith('B'), countries))
# print(starts_with_b)

# Declare a function called get_string_lists which takes a list as a parameter 
# and then returns a list containing only string items.
# def get_string_lists(lista):
#   string_returned = ' '.join(str(element) for element in lista)
#   return string_returned
# lista = ['El', 'león', 'está', 'en', 'la', 'selva']
# print(get_string_lists(lista))

# Use reduce to sum all the numbers in the numbers list
from functools import reduce
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def sum_numbers(a, b):
#   return a + b
# total = reduce(sum_numbers, numbers)
# print(total)

# Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
countries_list = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

concatenate_countries = reduce(lambda element:element.split(), countries_list)

print(concatenate_countries)
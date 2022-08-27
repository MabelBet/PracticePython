def sum_of_numbers(num):
    lista = []
    for i in range (0,num+1):
        lista.append(i)
        suma = sum(lista)
    return suma
print(sum_of_numbers(5))
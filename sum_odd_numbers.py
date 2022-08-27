def sum_odd_numbers(num):
    lista = []
    for i in range (0,num+1):
        if i % 2 != 0:
            lista.append(i)
            suma = sum(lista)
    return suma
print(sum_odd_numbers(5))
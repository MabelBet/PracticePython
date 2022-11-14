#Asabeneh_30_Days_Of_Python
# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_number = [i for i in numbers if i <= 0]
print(filter_number)
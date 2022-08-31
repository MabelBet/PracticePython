#Asabeneh_30_Days_Of_Python
#Flatten the following list of lists of lists to a one dimensional list

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for row in list_of_lists for number in row]
#Since the initial list has double "[]", I used list comprehension twice
reflatened_list = [i for row in flattened_list for i in row]
print(reflatened_list)

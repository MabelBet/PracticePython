# def sum_of_numbers(num):
#     lista = []
#     for i in range (0,num+1):
#         lista.append(i)
#         suma = sum(lista)
#     return suma
# print(sum_of_numbers(5))
def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    print(max_num)
    for num in nums:
        if num > max_num:
            max_num += num
    return print(max_num, num)
find_max([3, 5, 3, 67])
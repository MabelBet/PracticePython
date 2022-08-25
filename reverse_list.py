def reverse_list(arr = []):
    new_arr = []
    for i in arr[::-1]:
        new_arr.append(i)
    return new_arr
arr_num = ["banana", "orange", "mango", "lemon"]

print(reverse_list(arr_num))

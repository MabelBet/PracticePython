def miniMaxSum(arr):
    arr = [9, 3, 5, 7, 1]
    sorted_arr = sorted(arr)
    print(sorted_arr)
    min_sum = sum(sorted_arr[0:4])
    reversed_sorted_arr = (sorted(arr,reverse=True))
    max_sum = sum(reversed_sorted_arr[0: 4])
    return print(min_sum, max_sum, sep=" ")
arri = [9, 3, 5, 7, 1]
miniMaxSum(arri)
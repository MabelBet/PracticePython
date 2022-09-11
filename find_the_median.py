def findMedian(arr):

    sorted_arr = sorted(arr)
    tamaño_muestra = len(sorted_arr)
    mediana = (tamaño_muestra // 2)
    final = sorted_arr[mediana]
    return print(final)
arr = [7,8,9,10,11,12,13]
findMedian(arr)


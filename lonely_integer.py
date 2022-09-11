def findSingle( ar, n):
    
    res = ar[0]
    for i in range(1,n):
        res = res ^ ar[i]
     
    return res


ar = [2, 3, 5, 4, 2, 3, 4]
print("Element occurring once is", findSingle(ar, len(ar)))

# ar = [2, 3, 5, 4, 2, 3, 4]
# n = len(ar)
# res = ar[0]
# for i in range(1,n):
#     res = res ^ ar[i]


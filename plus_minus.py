def plusMinus(arr):

    arr = [1, 1, 0, -1, -1]

    positives = [i for i in arr if i > 0]
    zeros = [k for k in arr if k == 0]
    negatives = [j for j in arr if j < 0]
    ratio_positives = round((len(positives)/len(arr)), 6)
    ratio_zeros = round((len(zeros)/len(arr)), 6)
    ratio_negatives = round((len(negatives)/len(arr)),6)

    return print(ratio_positives, ratio_negatives, ratio_zeros, sep="\n")

arri = [2, 4, 1, -3]
plusMinus(arri)
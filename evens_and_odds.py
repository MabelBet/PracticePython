def evens_and_odds(num):
    odds = []
    for i in range(0,num):
        if i % 2 == 0:
            odds.append(i)
    return len(odds)
print(evens_and_odds(100))
#So exciting, im doing the functions by miself
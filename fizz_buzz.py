def fizzBuzz(n):
    n = 9    
    for i in range (1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            result = "FizzBuzz"
            print(result)
        elif i % 3 == 0 and i % 5 != 0:
            result = "Fizz"
            print(result)
        elif i % 5 == 0 and i % 3 != 0:
            result = "Buzz"
            print(result)
        else:
            result = i
            print(result)
    return result
 
fizzBuzz(23)
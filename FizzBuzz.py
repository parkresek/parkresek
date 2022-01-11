def FizzBuzz (n):
    if(n%5 == 0 and n%3 == 0):
        return "FizzBuzz"
    elif(n%3 == 0):
        return "Fizz"
    elif(n%5 == 0):
        return "Buzz"
    return n
n = int(input('input banyak perulangannya : '))

for i in range(1,n+1):
    print(FizzBuzz(i))

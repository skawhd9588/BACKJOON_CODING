import math

def isPrime(num):
    if num == 1 : False
    else :
        for i in range(2, int(math.sqrt(num)+1)) :
            if num % i == 0 : return False
        return True
    
M, N = map(int, input().split())

for i in range(M, N+1) :
    if isPrime(i) : print(i)
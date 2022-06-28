import math
import sys

array = []
def isPrime(num):
    if num == 1 : False
    else :
        for i in range(2, int(math.sqrt(num)+1)) :
            if num % i == 0 : return False
        return num

for i in range(2, 10001):
    if isPrime(i) != False : array.append(i)

T = int(input())
for _ in range(T) :
    n = int(input())
    a = int(n/2)
    b = int(n/2)

    if a in array : print(a,b)
    else :
        while True :
            a -= 1
            b += 1
            if a in array and b in array :
                print(a, b)
                break
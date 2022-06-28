import math

array = [i for i in range(2*123456+1)]
array[0], array[1] = False, False

for i in range(2, 2*123456+1) :
    for j in range(2, int(math.sqrt(i)+1)) :
        if array[i] % j == 0 : 
            array[i] = False
            break
    else : array[i] = True

while True :
    n = int(input())
    if n == 0 : break

    cnt = 0
    for i in range(n+1, 2*n+1) :
        if array[i] == True : cnt += 1
    print(cnt)
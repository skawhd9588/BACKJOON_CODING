n = int(input())
i = 0
sum = 0
while n > sum :
    i += 1
    sum += i
sum = sum-n
if i % 2 == 0 :
    print(i-sum,'/',sum+1, sep='')
else :
    print(sum+1,'/',i-sum, sep='')
n = int(input())
a = list(map(int, input().split()))
avr = 0
max = max(a)
for i in range(n) :
    a[i] = a[i]/max*100
    avr += a[i]
print(avr/len(a))
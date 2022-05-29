N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(N) :
    for j in range(2, A[i], 1):
        if A[i] % j == 0 : break
        if j == A[i]-1 : cnt += 1
print(cnt)

N = int(input())
for i in range(N) :
    cnt = 0
    a = list(map(int, input().split()))
    for j in a[1:] :
        if j > sum(a[1:])/a[0] :
            cnt += 1
        else : pass
    print('{:.3f}%'.format(cnt/a[0]*100))
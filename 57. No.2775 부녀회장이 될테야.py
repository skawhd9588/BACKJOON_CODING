arr = []
for i in range(int(input())) :
    k = int(input())
    n = int(input())
    for j in range(k) :
        arr.append([1])
    for j in range(n-1) :
        arr[0].append(j+2)
    for a in range(1,k) :
        for b in range(1,n) :
            arr[a].append(arr[a][b-1] + arr[a-1][b])
    print(arr[k][n])
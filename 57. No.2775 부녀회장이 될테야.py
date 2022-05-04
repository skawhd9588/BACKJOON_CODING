for i in range(int(input())) :
    arr = []
    k = int(input())
    n = int(input())
    for j in range(k+1) :
        arr.append([1])
    for j in range(1, n) :
        arr[0].append(j+1)
    for a in range(1,k+1) :
        for b in range(1,n) :
            arr[a].append(arr[a][b-1] + arr[a-1][b])
    print(arr[k][n-1])

for i in range(int(input())) :
    n, s = input().split()
    for j in range(len(s)) : 
        print(s[j]*int(n), end='')
    print('')
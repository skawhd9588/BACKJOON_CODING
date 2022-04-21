a = []
sum = 0
for i in range(int(input())) :
    a = input().split('X')
    
    for j in range(len(a)) :
        sum += int(len(a[j])*(2+(len(a[j])-1))/2)
    print(sum)
    sum = 0
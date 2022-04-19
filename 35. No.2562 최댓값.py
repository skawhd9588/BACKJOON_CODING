arr = []
for i in range(9) : 
    arr.append(int(input()))
print(max(arr),'\n',(arr.index(max(arr))+1), sep='')
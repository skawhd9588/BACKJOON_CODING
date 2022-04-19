arr = []
for i in range(9):
    print(i)
    if int(input())%42 in arr :
        continue
    else :
        arr.append(int(input())%42)

print(len(arr))
print(arr)
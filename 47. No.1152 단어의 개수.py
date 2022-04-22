s = input().split(' ')
cnt = 0
for i in range(len(s)):
    cnt=cnt if len(s[i]) == 0 else cnt+1
print(cnt)
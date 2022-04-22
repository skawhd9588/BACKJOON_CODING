s = input()
cnt = len(s)
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in range(len(s)) :
    if s[i:i+2] in croatia : 
        cnt-=1
    elif s[i:i+3] in croatia : 
        cnt-=1
print(cnt)
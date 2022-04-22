s = input()
cnt = [0]*26
for i in range(len(s)) :
    if ord(s[i]) <= 90 : 
        cnt[ord(s[i]) % 65] += 1
    else : 
        cnt[ord(s[i]) % 97] += 1
if cnt.count(max(cnt)) >= 2 : print('?')
else : print(chr(cnt.index(max(cnt))+65))
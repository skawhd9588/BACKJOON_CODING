S = input()
a = []
for i in range(26):
    a.append(-1)
for i in range(len(S)):
    if a[ord(S[i])%97] != -1 : pass
    else : a[ord(S[i])%97] = i
print(*a)
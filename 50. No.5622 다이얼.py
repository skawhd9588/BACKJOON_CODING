s = input()
num = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
getNum = []
for i in range(len(s)) :
    for j in range(8) : 
        if s[i] in num[j] : getNum.append(j+2)
print(sum(getNum)+len(s))
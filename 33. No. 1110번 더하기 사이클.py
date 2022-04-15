# N = input()
# if int(N) < 10:
#     N = str(int(N)*10)
# # while True : 
# A = str(int(N[0])+int(N[1]))
# a = str(int(N[1]))
# b = str(int(A[1]) if int(A)>10 else int(A))
# i = 1
# temp = 0
# while True :
#     if N == a+b : break
#     else : 
#         temp = a
#         a = b
#         b = str(int(temp)+int(b)) if int(temp)+int(b)<10 else str(int(temp)+int(b))[1]
#         i += 1

# print(i)

N = int(input())
if N < 10 : N *= 10
a = N//10*10
b = N%10
i=1
while True:
    temp = a//10
    a = b*10
    b = temp+b if temp+b<10 else (temp+b)%10    
    if N == a+b : break
    else : i += 1
print(i)
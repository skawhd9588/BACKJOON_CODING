H, M = map(int, input().split())
c = int(input())

# if (c+M)//60 > 0 :
#     H += 1
# H += c//60
# M += c%60
# if M == 60 :
#     M=0

#print(H, M)

print((H+(((c%60+M)//60)>0)+c//60)%24, (M+(c%60))%60)
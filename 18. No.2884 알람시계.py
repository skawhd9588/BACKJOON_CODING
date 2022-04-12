H, M = map(int, input().split())

if M<45 :
    H -= 1
    M += 15
    if H == -1 :
        H = 23
else :
    M -= 45

print(H, M)

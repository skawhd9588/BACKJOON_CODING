a, b, v = map(int, input().split())
cnt = a-b
if (v-a)%cnt == 0 : print((v-a)//cnt+1)
else : print((v-a)//cnt+2)
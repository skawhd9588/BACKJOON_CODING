T = int(input())
for i in range(T) :
    h, w, n = map(int, input().split())
    print(n%h*100+n//h+1) if n%h != 0 else print(h*100+n//h)
a, b, c = map(int, input().split())
print(-1 if c<b else a//(c-b)+1)
n1, n2 = input().split()
print(n1[::-1] if int(n1[::-1]) > int(n2[::-1]) else n2[::-1])
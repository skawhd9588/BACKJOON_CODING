def P(num):
    if num == 0 : return 0
    elif num == 1 : return 1
    return P(num-1) + P(num-2)
print(P(int(input())))
a, b, c = map(int, input().split())
rm = [(a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c]

for i in range(4):
    print("{}".format(rm[i]), sep='\n')
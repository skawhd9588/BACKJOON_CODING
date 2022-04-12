# q1, q2 = map(int, input().split()) 백준 제출 시 런타임 에러남
q1 = int(input())
q2 = int(input())
print('13'[q1<0] if q1*q2>0 else('2' if q1<0 else '4'))
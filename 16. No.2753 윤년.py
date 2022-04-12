year = int(input())
print('01'[(year%4==0 and year%100!=0) or year%400==0])
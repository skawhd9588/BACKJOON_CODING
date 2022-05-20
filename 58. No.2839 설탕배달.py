N = int(input()) 
if N % 5 and N % 3 != 0 :
    print('-1')

for i in range(N//5,0,-1) :
    if N/i%3==0 :
        print(N//i+N//i/3)    
    
        

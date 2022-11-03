'''
VUDE-HCL 1 – 1 2 3 4 5
VUDE-HCL 2 – 1 2 3 4 5
VUDE-HCL 3 – 1 2 3 4 5
VUDE-HCL 4 – 1 2 3 4 5
VUDE-HCL 5 – 1 2 3 4 5
'''
n=int(input('enter a number : '))
for row in range(1,n+1):
    print('VUDE-HCL',row,'- ',end="")
   
    for col in range(1,n+1):
        print(col,end=' ')

    print()
    
    
    

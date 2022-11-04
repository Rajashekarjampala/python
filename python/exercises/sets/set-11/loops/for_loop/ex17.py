'''
 Write a program to print the following pattern.

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''
n=int(input('enter a number : '))
for row in range(1,n+1):
    for col in range(1,row+1):        
        print(col,end=' ')
    print()
'''
Write a program to print the following pattern.
1
22
333
4444
'''
n=int(input('enter a number : '))
for row in range(1,n+1):
    for col in range(1,row+1):        
        print(row,end=' ')
    print()
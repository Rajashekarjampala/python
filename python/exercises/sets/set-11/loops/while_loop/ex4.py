# Print even and odd numbers list from natunaral numbers up to n....

num=int(input("Enter a number: "))
Even_list=[]
Odd_list=[]

i=1
while(i<=num):
    if (i%2==0):
        Even_list.append(i)        

    else:
        Odd_list.append(i)  

    i=i+1        

print(Even_list)
print(Odd_list)
        
        

    
# Write a program to calculate the sum of numbers from starting to ending


start=int(input("Enter a number: "))
end=int(input("Enter a number: "))
Even_list=[]
Odd_list=[]

i=start
while(i<=end):
    if (i%2==0):
        Even_list.append(i)        

    else:
        Odd_list.append(i)  

    i=i+1        

print(Even_list)
print(Odd_list)
        
        
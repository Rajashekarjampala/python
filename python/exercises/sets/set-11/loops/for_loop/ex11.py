# Add numbers between two specific numbers

n1=int(input("enter a first number: "))
n2=int(input("enter a last number: "))
sum=0
for i in range(n1,n2):
  sum=sum+i
 
print(sum)
#1. Write a program using for loop to calcuate the average of first n natural numbers.
#using while loop

n=int(input("enter a number: "))
sum=0
count=0
i=1
while(i<=n):
  sum=sum+i
  count=count+1
  i=i+1
avg=sum/count
print(avg)
#1. Write a program using for loop to calcuate the average of first n natural numbers.
# Using for loop

def check_avg(num):
  sum=0
  count=0
  for i in range(1,num+1):
    sum=sum+i
    count=count+1
  avg=sum/count
  return(avg)

print(check_avg(10))  
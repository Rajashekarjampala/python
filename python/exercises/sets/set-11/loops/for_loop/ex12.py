# write a python program for Sum of even numbers up to n and its count

#n=int(input("Enter a number: "))
def check_num(num):
    sum=0
    count=0
    for i in range(1,num+1):    
        if (i%2==0):
            sum=sum+i
            count=count+1
    return 'sum of {} natural numbers is : {} \nNo.of even numbers present in natural numbers upto {} is : {}'.format(num,sum,num,count)
print(check_num(10))   
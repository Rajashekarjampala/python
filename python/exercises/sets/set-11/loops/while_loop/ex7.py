# print prime 
#num=int(input("Enter a number: "))

'''if (num>=2):
    for i in range (2,num):
        if (num%i==0):
            print("Its not prime")
            break
    else:
        print("Its prime") '''    

num=int(input("enter a number: "))
cof=0
for i in range(1,num+1):
    if (num%i==0):
        cof=cof+1

if (cof==2):
    print("its prime")
else:
    print("not prime")            


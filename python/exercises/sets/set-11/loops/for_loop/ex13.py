# Find prime number
#n=int(input("Enter a number: "))
def check_prime(num):
    if(num>=2):
        for i in range(2,num):
            if(num%i==0):
                return('not a prime') 
                break
        else:
            return("Its Prime")

    else:
        return('not a prime')

print(check_prime(20))        


                        

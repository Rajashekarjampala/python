# Find the prime numbers between two numbers

def check_prime(start,end):
    prime_list=[]
    for num in range(start, end):
        # all prime numbers are greater than 1
        # if number is less than or equal to 1, it is not prime
        if num >= 2:
            for i in range(2, num):
                # check for factors
                if (num % i) == 0:
                    # not a prime number so break inner loop and
                    # look for next number
                    break
            else:
                prime_list.append(num)               
    return prime_list
    
print(check_prime(1,20))                  

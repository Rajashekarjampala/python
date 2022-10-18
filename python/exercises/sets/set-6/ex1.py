'''
1. Write a function to take a list. Filter all the prime numbers, add to new list and return the new list.
    Example :
        org_list=[10,20,30,40,50,60,100,11]
        result=func_exec(org_list)
        print(result)
        Expected Output : [11]
    Example :
        org_list=[10,20,23,30,40,50,60,100,11]
        result=func_exec(org_list)
        print(result)
        Expected Output : [11,23]
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY. 

Solution Steps:
**************
Iterate the the original list
From the list Checking for number is greater than Or equals to 2 
    Checking the co-factors of list (range 2 to original list)
        If number has co_factors :
            loop will break
        else:
            Add to new list    
            loop not breakable the number is prime
Finally return the new list   
'''

#This Function return prime number list
def check_prime(org_list):
    #define new list
    new_mapping=[]
    #iterates original list one by one
    for i in org_list:
        #checking for number is greater than Or equals to 2
        if(i>=2):        
            #every prime has 2 co-factors 1 and it self number, we are taking range from 2 to one less the number 
            # if we found any co-factors between these range this is a prime number        
            for j in range(2,i):
                #checking for Divisiblity if condition true loop will break
                if(i%j==0):
                    #breakdown loop
                    break         
            else:
                    #if loop not breakable the number is prime and adds to new list
                    new_mapping.append(i)     
    #finally return                         
    return new_mapping

# Execution
#calling function
#Testcase 1
result=check_prime([10,20,30,40,50,60,100,11])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_prime([10,20,23,30,40,50,60,100,11])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_prime([77,44,72,84,98,17,13,78])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_prime([12,6,24,42,8,26,62,76])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_prime([32,64,101,74,103,86,105,58])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_prime([11,22,33,44,55,66,77,88])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_prime([99,88,77,66,55,44,33,22])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_prime([101,2,103,4,104,5,105,6])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_prime([78,24,23,76,89,44,22,88])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_prime([24,36,48,50,62,74,86,98])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
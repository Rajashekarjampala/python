'''write a function to takes argument as list .
   iterate the list and find the greatest prime number from the list.
   add to new list and return the new list.

   Example:
   listA=[1,19,25,37,97,40,100,103,20,15]
   expected output : [103]   
'''
def check_prime(listA):
    new_list=[]
    for i in listA:
        if (i>=2):
            for j in range (2,i):
                if (i%j==0):
                    break
            else:
                new_list.append(i)             

    return max(new_list)
print(check_prime([1,19,25,37,97,40,100,103,20,15]))                
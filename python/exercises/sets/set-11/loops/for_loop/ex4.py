# numbers in range
# print 20 numbers using range function

# by default starting number is take 0
#for i in range(10): 
#    print(i)
from hashlib import new


def check_range(n1,n2,stp):
    new_list=[]
# Range with step size(2)
    for i in range (n1,n2,stp):
        new_list.append(i) 
    return new_list        

print(check_range(0,10,2))        

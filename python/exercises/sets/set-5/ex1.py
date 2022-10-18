'''
1. Write a function to take a list. Reverse and return the new list.
    Example :
        listA=[10,20,30,40,50,60,100]
        result=func_exec(listA)
        print(result)
        Expected Output : [100,60,50,40,30,20,10]
        :param org_list: Original list passed by the User
        :return: return new list with org_list arg

Solution Steps:
**************
Define the the function  
  We can take one empty list
  Iterate the original list 
  Reverse the Ogiginal list 
  Reversed list is add to the empty list 
  Return the empty list 
Print the empty list
'''
# function define the reverse the list
from unittest import TestCase


def check_reverse(org_list):

  # define empty list
  new_mapper = [] 
  # itearate the orginal list
  for i in reversed(org_list): 
    # add elements in to new list
    new_mapper.append(i) 
  # finally return the new list
  return new_mapper 

#calling function
#Testcase 1
result=check_reverse([10,20,30,40,50,60,70,80,90,100])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_reverse([20,40,60,80,100,120,140,160,180,200])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_reverse([11,12,13,14,15,16,17,18,19,20])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_reverse([1,2,3,4,5,6,7,8,9,10])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_reverse([100,200,300,400,500,600,700,800,900,1000])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_reverse([21,22,23,24,25,26,27,28,29,30])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_reverse([90,91,92,93,94,95,96,97,98,99,100])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_reverse([11,22,33,44,55,66,77,88,99,100])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_reverse([25,35,45,55,65,75,85,95,105,115])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_reverse([121,221,321,421,521,621,721,821,921])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#

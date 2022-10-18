'''
2. Write a function to take a list. Sort and return the new list.
    Example :
        listA=[100,20,300,40,50,60,100]
        result=func_exec(listA)
        print(result)
        Expected Output : [20,40,50,60,100,100,300]
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY
Solution Steps:
**************
Define the the function 
  We can take one empty list
  Iterate the original list 
  Sort the Ogiginal list 
  Sorted list is add to the empty list 
  Return the empty list 
print empty list    
'''   

#This function gives a new sorted list
def check_sort(org_list):

    #define new list
    new_mapper=[]
    # sort the orginal list as listA
    for i in sorted(org_list):
        #adds to new list
        new_mapper.append(i)
    #Finally return new sorted list           
    return new_mapper
    
# Execution
#calling function
#Testcase 1
result=check_sort([21,14,56,78,56,35,89,40,44,100])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_sort([10,78,45,23,12,67,89,90,23,25,21])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_sort([11,44,33,77,88,99,55,33,22,66])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_sort([1,10,8,7,4,3,6,2,9,5])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_sort([1000,800,300,500,700,100,600,400,900])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_sort([21,34,57,87,54,32,23,29,55,80])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_sort([90,100,98,93,95,91,96,92,97,99])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_sort([1,100,300,800,50,39,75,67,894])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_sort([25,45,65,75,95,105,25,15,85])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_sort([121,22,456,2337,980,432,666,77,9])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#

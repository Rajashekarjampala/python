'''
3. Write a function to take a list. Select the number that is greater than product of all other numbers.
    Example :
        listA=[1,2,30,4,2]
        result=func_exec(listA)
        print(result)
        Expected Output : 30
        Reason: 30 is greater than product of [1,2,4,2] -> 16
    Example :
        listA=[1,2,3,4,2]
        result=func_exec(listA)
        print(result)
        Expected Output : []
        :param org_list: Original list passed by the User        
        :return: New list with filtered values ONLY
Solution Steps:
**************
Iiterate the original list
    Find the current number, store in a variable currNumber
        Find the product of remaining numbers and store in a variable sumList
        Check if currNumber is >er productList:
            If yes:
                return currNumber
            else:
                continue the LOOP  
Finally return the new list             
'''
# This function is define pick greater number sum of all the list       
def check_greater(org_list):

    # iterate the orginal list
    for i in org_list:
        # assigning org list to another variable like new_mapper 
        new_mapper=org_list
        # remove a selected element from the New list
        new_mapper.remove(i)
        # logic for product
        list_pro=1
        for j in new_mapper:            
            list_pro*=j
        # To check the condition whether the selected element is greater than the product of other remaining elements in the list,
        # if condition true the selected element is greatest    
        if (i>list_pro):
            # Finally return the greater value from list
            return i
# Examples            
#Testcase 1
result=check_greater([1,3,35,5,2])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_greater([2,1,25,2,3])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_greater([2,3,1,5,45,2])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_greater([3,5,50,1,3])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_greater([4,5,3,80,1])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_greater([5,2,45,2,2])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_greater([20,2,5,650,3])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_greater([5,3,4,90,1])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_greater([2,5,6,100,5])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_greater([1,5,10,2,110])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
'''
2. Write a function to take a list. Select the number that is greater than sum of all other numbers.
    Example :
        listA=[1,2,13,4,5]
        result=func_exec(listA)
        print(result)
        Expected Output : 13
        Reason: 13 is greater than sum of [1,2,4,5] -> 12
    Example :
        listA=[100,20,300,40,1000,50,60,100]
        result=func_exec(listA)
        print(result)
        Expected Output : 1000
        Reason: 1000 is greater than sum of [100,20,300,40,50,60,100] -> 670
        :param org_list: Original list passed by the User        
        :return: New list with filtered values ONLY

Solution Steps:
**************
Iterate the list -> listA:
    Find the current number, store in a variable currNumber
    Find the sum of remaining numbers and store in a variable sumList
    Check if currNumber is >er sumList:
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
        # To check the condition whether the selected element is greater than the sum of other remaining elements in the list,
        # if condition true the selected element is greatest
        if (i>sum(new_mapper)):
            # Finally return the greater value from list
            return i
# Execution
#Testcase 1
result=check_greater([4,6,20,3,5])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_greater([5,10,6,4,25])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_greater([10,15,5,3,35])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_greater([5,9,1,25,8])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_greater([5,3,7,20,10])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_greater([20,10,60,150,40])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_greater([50,20,60,120,140])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_greater([5,10,15,30,10])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_greater([5,10,6,4,26])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_greater([10,20,15,5,603])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
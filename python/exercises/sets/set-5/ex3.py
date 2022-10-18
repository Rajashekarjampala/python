'''
3. Write a function to take 2 lists. Use zip function to iterate the list and pick values that
   are common at both indexes.
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,20,1300,40,50,160,1000]
        result=func_exec(listA,listB)
        print(result)
        # 20 -> listA[1] == listB[1]
        # 40 -> listA[3] == listB[3]
        # 50 -> listA[4] == listB[4]
        Expected Output : [20,40,50]
        :param org_list: Original list(org_listA, org_listB) passed by the User
        :return: New list with filtered values ONLY
Solution Steps:
**************
Define the the function 
  We can take one empty list
  Iterate the original lists by using zip 
  Check the comman elements in both lists list 
  Comman elements are add to the empty list 
  Return the empty list 
print empty list             
'''   
        
# function gives comman elements in listA and listB
def check_list(org_listA, org_listB):  

    #define empty list
    new_mapper=[]
    #iterates 2 list Simanatanously using the zip
    for listA_var, listB_var in zip(org_listA, org_listB):
            #checking for both the elements from 2 lists are equal if condition true element adds to    new_mapper
            if(listA_var==listB_var):
                    #adding element to new list
                    new_mapper.append(listA_var)
    #finally return the new list        
    return  new_mapper
    
#calling function
#Testcase 1
result=check_list([100,20,300,40,50,60,100],[100,20,1300,40,50,160,1000])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_list([10,78,45,23,12,67,89,90,23,25,21],[28,42,45,38,40,72,89,92,78,85,25])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_list([11,44,33,77,88,99,55,33,22,66],[14,21,75.77,82,31,52,25,22,35])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_list([1,10,8,7,4,3,6,2,9,5],[32,12,8,23,27,3,62,32,21,5])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_list([1000,800,300,500,700,100,600,400,900],[77,42,67,500,787,100,672,48,900])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_list([21,34,57,87,54,32,23,29,55,80],[21,13,72,87,54,43,78,90,55,88])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_list([90,100,98,93,95,91,96,92,97,99],[76,42,67,66,34,59,42,57,63,48])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_list([1,100,300,800,50,39,75,67,894],[1,88,76,82,35,39,75,79,86])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_list([25,45,65,75,95,105,25,15,85],[14,35,75,88,95,78,25,71,85])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_list([121,22,456,2337,980,432,666,77,9],[34,75,78,64,980,463,777,72,48])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
'''
1. Write a function to take a list, numX, numY as arguments.
Filter all the numbers from the list that are >numX and <numY and add to new list.
Finally return the new list.

    Example 1 :
        listA=[10,20,30,40,50,60,100,11,12,13]
        numX=45
        numY=55
        result=func_exec(listA)
        print(result)
        Expected Output : [50]
        Reason: 50 is >er than numX 45 and <er than numY 55

    Example 2 :
        listA=[10,20,30,46,52,60,54,11,12,13]
        numX=45
        numY=55
        result=func_exec(listA)
        print(result)
        Expected Output : [46,52,54]
        Reason: 46 is >er than numX 45 and <er than numY 55
        Reason: 52 is >er than numX 45 and <er than numY 55
        Reason: 54 is >er than numX 45 and <er than numY 55

    Example 3 :
        listA=[10,20,30,46,52,60,54,11,12,13]
        numX=450
        numY=550
        result=func_exec(listA)
        print(result)
        Expected Output : []
        
        :param org_list: Original list passed by the User
        :param numx: Numberx passed by the User. Type is INT.
        :param numy: Numbery passed by the User. Type is INT.
        :return: New list with filtered values ONLY.  

    Solution Steps:
    **************
    Take a original list and iterate original list     
    Check if number is greater than number X and number less than number Y
        if yes:
            add to new list
        else:
            continue loop  
    Finally return new list              
'''
#define function
def check_num(org_list,numX,numY):
    #define new list
    new_list=[]
    #iterate elements from original list one by one
    for i in org_list:
        #checking for element is greater than x and less than y
        if(i>numX and i<numY):
            #adding element to new list
            new_list.append(i)
    #finally return new list
    return new_list

#calling function
#calling function
#Testcase 1
result=check_num([10,20,30,40,50,60,100,11,12,13],45,55)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_num([10,20,30,46,52,60,54,11,12,13],45,55)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_num([10,20,30,46,52,60,54,11,12,13],450,550)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_num([10,20,30,46,52,60,54,11,12,13],20,30)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_num([10,20,30,46,52,60,54,11,12,13,500],20,30)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_num([23,25,23,24,25,26,27,28,25,30],23,28)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_num([90,91,92,93,94,95,96,97,98,99,100],100,150)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_num([44,22,33,44,55,66,44,88,44,100],11,80)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_num([25,35,45,55,65,75,85,95,105,115],1,50)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_num([121,221,321,421,521,621,121,821,921],500,800)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#


